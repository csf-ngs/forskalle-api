import typing
import click
import click_log
import json
import logging
import shutil
from forskalle_api.auto.models import Run, RunUnit, Sample, SequencedSample, plainToRequest, serializeMultiplex, serializeOntFlowcellRun, serializeOntRun, serializePacbioRun, serializeRequest, serializeRunUnit, serializeSample, serializeSequencedBarcode, serializeSequencedSample, serializeSmrtCell, Request, serializeRequestsSample
from forskalle_api.fsk_api import FskApi

from forskalle_api.fsk_query import FskPagedQuery, FskQuery
from forskalle_api.auto.queryparams import SampleFilters, SequencedSampleFilters, MultiplexFilters, RequestFilters

logger = logging.getLogger(__name__)
click_log.basic_config(logger)

def make_query(filters, limit, page):
  if page != 0:
    query = FskPagedQuery(filters=filters, page=page, limit=limit)
  else:
    query = FskQuery(filters=filters)
  return query

def parse_id(id: str, prefix: str) -> int:
  if id.startswith(prefix):
    return int(id[1:])
  else:
    return int(id)

@click.group()
@click_log.simple_verbosity_option(logger)
@click.option('--base', '-b', help='API Base URL')
@click.option('--key', '-k', help='API Key')
@click.pass_context
def cli(ctx, base, key):
    """Fsk3 CLI - sequencing metadata made easy."""
    ctx.obj = FskApi(base=base, key=key)
    pass

@cli.command(short_help='who am i')
@click.pass_obj
def whoami(obj: FskApi):
  me = obj.current_account()
  click.echo(f"You are: {me.username}/{'admin' if me.is_admin else 'user'}")

@cli.command(short_help="suggest a few xkcd passphrases")
@click.pass_obj
def generate_passwords(obj: FskApi):
  click.echo(json.dumps(obj.generate_passwords(), indent=2, sort_keys=True))

@cli.command(short_help='get barcodes for a lane/smrtcell/nanopore run')
@click.argument('identifier')
@click.option('--platform', '-p', default='Illumina', help='Illumina, Pacbio or ONT')
@click.pass_obj
def get_barcodes(obj: FskApi, identifier, platform='Illumina'):
  """Get Barcodes for a Sequencing Run. 

  The value for IDENTIFIER depends on the platform. It is [flowcell]_[lane] for Illumina, and the UUID for other platforms.

  If you are a user, at least one sample on the lane must belong to you."""
  if platform == 'Illumina':
    (flowcell, _, lane) = identifier.partition('_')
    ret = obj.get_illumina_barcodes(flowcell, lane)
  elif platform == 'Pacbio':
    ret = obj.get_smrtcell_barcodes(identifier)
  elif platform == 'ONT':
    ret = obj.get_nanopore_barcodes(identifier)
  else:
    raise click.ClickException(f"Invalid platform {platform}")
  click.echo(json.dumps([ serializeSequencedBarcode(r) for r in ret ], indent=2, sort_keys=True))
    

@cli.command(short_help='list sequenced samples')
@click.option('--sample', '-s', help='sample id (can be specified multiple times)', multiple=True)
@click.option('--multi', '-m', help='multiplex id (can be specified multiple times)', multiple=True)
@click.option('--request', '-r', help='request id (can be specified multiple times)', multiple=True)
@click.option('--limit', '-l', help='max rows', type=int, default=100)
@click.option('--page', '-p', help='Page (to return next [limit] rows', type=int, default=1)
@click.option('--csv', is_flag=True)
@click.option('--admin', is_flag=True, help='Show all users, available only with API key')
@click.pass_obj
def list_sequenced_samples(obj: FskApi, sample, multi, request, limit, page, csv, admin):
  filters = SequencedSampleFilters(sample_id=sample, multi_id=multi, request_id=request)
  ret = FskApi().list_sequenced_samples(make_query(filters, limit, page), csv, admin)
  if csv:
    click.echo(ret)
  else:
    click.echo(json.dumps([ serializeSequencedSample(s) for s in ret if type(s) is SequencedSample ], indent=2, sort_keys=True))


@cli.command(short_help='update sequencing run status for a sample (admin only)')
@click.argument('sample_id')
@click.option('--status', '-s', type=click.Choice(['Ok', 'Repeat', 'Failed'], case_sensitive=False), default="Ok")
@click.option('--vendor_id', help='Flowcell ID when there are multiple runs for a sample')
@click.pass_obj
def set_sequencing_status(obj: FskApi, sample_id, status='Ok', vendor_id=None):
  seqsamps = obj.get_sample_sequencing_runs(sample_id)
  runs: dict[str, typing.Tuple[Run, typing.List[SequencedSample]]] = {}
  for seqsamp in seqsamps:
    if type(seqsamp) is not SequencedSample:
      continue
    if not seqsamp.run_unit or not seqsamp.run_unit.run:
      raise click.ClickException(f"Invalid return")

    v_id = seqsamp.run_unit.run.vendor_id
    if not v_id:
      raise click.ClickException(f"no vendor id")
    if not v_id in runs:
      runs[v_id] = (seqsamp.run_unit.run, [])
    runs[v_id][1].append(seqsamp)
  
  if len(runs) > 1 and not vendor_id:
    logger.info("Multiple runs found:")
    for vendor_id in runs.keys():
      logger.info(f"- {vendor_id}")
    raise click.ClickException("Please to tell me which run to fiddle with (hint: --vendor_id)")
  run, seqsamps = runs.popitem()[1] if not vendor_id else runs.get(vendor_id, (None, None))
  if not run or not seqsamps:
    raise click.ClickException(f"Run {vendor_id} not found!")
  if not run.platform:
    raise click.ClickException(f"Invalid run")
  
  unit_name = 'lanes' if run.platform == 'Illumina' else 'smrtcells' if run.platform == 'Pacbio' else 'ont_flowcell_runs' if run.platform == 'ONT' else None
  db_run = obj.get(f"/api/runs/{run.platform.lower()}/{run.vendor_id}")
  for db_unit in db_run[unit_name]:
    for seqsamp in seqsamps:
      if seqsamp.unit_id == db_unit['unit_id']:
        for db_ss in db_unit['sequenced_samples']:
          if db_ss['reqsamp_id'] == seqsamp.reqsamp_id:
            logger.debug(f"seqsamp {db_ss['id']} found on unit {db_unit['unit_id']}, setting status to {status}")
            db_ss['status']=status
  ret = obj.post(f"/api/runs/{run.platform.lower()}/{run.vendor_id}", db_run)
  logger.info(f"Run {ret['vendor_id']} updated, new status: {ret['status']}")



@cli.group(short_help='multiplexes')
def multis():
  pass

@multis.command(short_help='list multiplexes', name='list')
@click.option('--scientist', help="Scientist name, only useful with admin query")
@click.option('--group', help="Group name, only useful with admin query")
@click.option('--limit', '-l', help='max rows', type=int, default=100)
@click.option('--page', '-p', help='Page (to return next [limit] rows', type=int, default=1)
@click.option('--csv', is_flag=True)
@click.option('--admin', is_flag=True, help='Show all users, available only with admin key')
@click.pass_obj
def list_multis(obj: FskApi, scientist, group, limit, page, csv, admin):
  filters = MultiplexFilters(scientist=scientist, group=group)
  ret = FskApi().list_multis(make_query(filters, limit, page), csv, admin)
  if csv:
    click.echo(ret)
  else:
    click.echo(json.dumps(ret, indent=2))

  
@multis.command(short_help='get multiplex metadata', name='get')
@click.argument('multi_id')
@click.option('--out', '-o', type=click.File("w"), default='-')
@click.pass_obj
def get_multi(obj: FskApi, multi_id, out):
  ret = FskApi().get_multi(parse_id(multi_id, 'M'))
  out.write(json.dumps(serializeMultiplex(ret), indent=2, sort_keys=True))


@cli.group(short_help='request related commands')
def requests():
  pass

@requests.command(short_help='list requests', name='list')
@click.option('--scientist', help="Scientist name, only useful with admin query")
@click.option('--group', help="Group name, only useful with admin query")
@click.option('--limit', '-l', help='max rows', type=int, default=100)
@click.option('--page', '-p', help='Page (to return next [limit] rows', type=int, default=1)
@click.option('--csv', is_flag=True)
@click.option('--admin', is_flag=True, help='Show all users, available only with admin key')
@click.pass_obj
def list_requests(obj: FskApi, scientist, group, limit, page, csv, admin):
  filters = RequestFilters(scientist=scientist, group=group)
  ret = FskApi().list_requests(make_query(filters, limit, page), csv, admin)
  if csv:
    click.echo(ret)
  else:
    click.echo(json.dumps([ serializeRequest(r) for r in ret if type(r) is Request ], indent=2, sort_keys=True))

@requests.command(short_help='get metadata', name='get')
@click.argument('id')
@click.option('--out', '-o', type=click.File("w"), default='-')
@click.pass_obj
def get_request_data(obj: FskApi, id, out):
  req = obj.get_request(parse_id(id, 'R'))
  out.write(json.dumps(serializeRequest(req), indent=2, sort_keys=True))

@requests.command(short_help='update request', name='update')
@click.argument('id')
@click.option('--json', '-j', 'input',  type=click.File("r"), default='-')
@click.pass_obj
def set_request_data(obj: FskApi, id, input):
  """Update a request from a JSON file. Intended usage is to retrieve the current request JSON with "get", edit it and then use "update"."""
  req = obj.get_request(parse_id(id, 'R'))
  update=json.load(input)
  ret = obj.post(f"/api/requests/{req.id}", update)
  logger.info(f"Update request {ret['id']}")

@requests.command(short_help='set status (admin only)')
@click.argument('id')
@click.argument('status', type=click.Choice(['Submitted', 'Completed', 'Aborted', 'Accepted'], case_sensitive=False))
@click.pass_obj
def set_status(obj: FskApi, id, status):
  req = obj.get_request(parse_id(id, 'R'))
  req.status = status
  req = plainToRequest(obj.post(f"/api/requests/{req.id}", serializeRequest(req)))
  logger.info(f"Updated request {req.id}, new status {req.status}")
  for rl in req.request_lanes:
    logger.info(f" lane {rl.num} status {rl.status}")

@cli.group(short_help='samples')
def samples():
  pass

@samples.command(short_help='list samples', name='list')
@click.option('--id_from', help='min id', type=int)
@click.option('--id_to', help='max id', type=int)
@click.option('--scientist', help="Scientist name, only useful with admin query")
@click.option('--group', help="Group name, only useful with admin query")
@click.option('--limit', '-l', help='max rows', type=int, default=100)
@click.option('--page', '-p', help='Page (to return next [limit] rows', type=int, default=1)
@click.option('--csv', is_flag=True)
@click.option('--admin', is_flag=True, help='Show all users, available only with admin key')
@click.pass_obj
def list_samples(obj: FskApi, id_from, id_to, scientist, group, limit, page, csv, admin):
  filters = SampleFilters(id_from=id_from, id_to=id_to, scientist=scientist, group=group)
  ret = FskApi().list_samples(make_query(filters, limit, page), csv, admin)
  if csv:
    click.echo(ret)
  else:
    click.echo(json.dumps([ serializeSample(s) for s in ret if type(s) is Sample ], indent=2, sort_keys=True))

@samples.command(short_help='list samples of all groups you belong to', name='list-group')
@click.option('--id_from', help='min id', type=int)
@click.option('--id_to', help='max id', type=int)
@click.option('--scientist', help="Scientist name")
@click.option('--group', help="Group name, useful if you belong to many groups.")
@click.option('--limit', '-l', help='max rows', type=int, default=100)
@click.option('--page', '-p', help='Page (to return next [limit] rows', type=int, default=1)
@click.option('--csv', is_flag=True)
@click.pass_obj
def list_group_samples(obj: FskApi, id_from, id_to, scientist, group, limit, page, csv):
  filters = SampleFilters(id_from=id_from, id_to=id_to, scientist=scientist, group=group)
  ret = FskApi().list_group_samples(make_query(filters, limit, page), csv)
  if csv:
    click.echo(ret)
  else:
    click.echo(json.dumps([ serializeSample(s) for s in ret if type(s) is Sample ], indent=2, sort_keys=True))


@samples.command(short_help='get sample metadata', name='get')
@click.argument('sample_id')
@click.option('--out', '-o', type=click.File("w"), default='-')
@click.pass_obj
def get_sample(obj: FskApi, sample_id, out):
  ret = FskApi().get_sample(sample_id)
  out.write(json.dumps(serializeSample(ret), indent=2, sort_keys=True))

@samples.command(short_help='get sequencing runs for a sample', name='sequencing')
@click.argument('sample_id')
@click.option('--csv', is_flag=True)
@click.option('--out', '-o', type=click.File("w"), default='-')
@click.pass_obj
def get_sample_sequencing(obj: FskApi, sample_id, out, csv=False):
  ret = FskApi().get_sample_sequencing_runs(sample_id, csv)
  if csv:
    out.write(ret)
  else:
    out.write(json.dumps([ serializeSequencedSample(r) for r in ret if type(r) is SequencedSample ], indent=2, sort_keys=True))

@samples.command(short_help='get request information for a sample', name='requests')
@click.argument('sample_id')
@click.option('--out', '-o', type=click.File("w"), default='-')
@click.pass_obj
def get_sample_requests(obj: FskApi, sample_id, out):
  ret = FskApi().get_sample_requests(sample_id)
  out.write(json.dumps([ serializeRequestsSample(r) for r in ret ], indent=2, sort_keys=True))

@cli.group(short_help='pacbio stuff (admin only)')
def pacbio():
  pass

@pacbio.command(short_help='register smrtcell report URL in Forskalle', name='post-report')
@click.argument('unique_id')
@click.argument('url')
@click.pass_obj
def post_pacbio_report_url(obj: FskApi, unique_id, url):
  ret = FskApi().publish_smrtcell_report(unique_id, url)
  click.echo(json.dumps(serializeSmrtCell(ret), indent=2, sort_keys=True))

@pacbio.command(short_help='register smrtcell data download link in Forskalle', name='post-download')
@click.argument('unique_id')
@click.argument('path')
@click.option('--link', '-l', help='explicit link name (full URL)')
@click.option('--size', '-s', help='explicit file size')
@click.option('--md5', '-m', help='DEPRECATED, use hash instead -- explicit md5 sum (taken from [path].md5 otherwise)')
@click.option('--hash', '-h', help='explicit md5 sum (taken from [path].md5 otherwise)')
@click.pass_obj
def publish_pacbio_download(obj: FskApi, unique_id, path, link, size, md5, hash):
  if md5:
    logger.warn(f"The --hash paramter is the new --md5 parameter")
    hash=f"md5.{md5}"
  ret = FskApi().publish_smrtcell_download(unique_id, path, link=link, size=size, hash=hash)
  click.echo(json.dumps(serializeSmrtCell(ret), indent=2, sort_keys=True))

@pacbio.command(short_help='import a pacbio run from subreadset.xml', name='import')
@click.argument('path')
@click.pass_obj
def import_subreadset(obj: FskApi, path):
  with open(path, 'r') as fh:
    subreadset = fh.read()
  ret = FskApi().import_subreadset(subreadset)
  click.echo(json.dumps(serializePacbioRun(ret), indent=2, sort_keys=True))

@cli.group(short_help='Nanopore (admin only)')
def ont():
  pass

@ont.command(short_help='import a nanopore run from metadata.json', name='import')
@click.argument('path')
@click.option('--update-meta/--no-update-meta', help='write back fsk_vendor_id to metadata.json', default=True)
@click.pass_obj
def import_ont_meta(obj: FskApi, path, update_meta):
  with open(path, 'r') as fh:
    meta = json.load(fh)
  ret = FskApi().import_nanopore_run(meta)
  if update_meta:
    meta['fsk_vendor_id']=ret.vendor_id
    for run in ret.ont_flowcell_runs:
      if run.unique_id==meta['run_id']:
        meta['fsk_unit_id']=run.unit_id
    with open(f"{path}.new", 'w') as fh:
      json.dump(meta, fh, sort_keys=True)
      shutil.move(f"{path}.new", path)
  click.echo(json.dumps(serializeOntRun(ret), indent=2, sort_keys=True))

@ont.command(short_help='register nanopore report URL in Forskalle', name='post-report')
@click.argument('unique_id')
@click.argument('url')
@click.pass_obj
def post_nanopore_report_url(obj: FskApi, unique_id, url):
  ret = FskApi().publish_nanopore_report(unique_id, url)
  click.echo(json.dumps(serializeOntFlowcellRun(ret), indent=2, sort_keys=True))

@ont.command(short_help='register nanopore data download link in Forskalle', name='post-download')
@click.argument('unique_id')
@click.argument('path')
@click.option('--link', '-l', help='explicit link name (full URL)')
@click.option('--size', '-s', help='explicit file size')
@click.option('--md5', '-m', help='DEPRECATED, use hash instead -- explicit md5 sum (taken from [path].md5 otherwise)')
@click.option('--hash', '-h', help='explicit md5 sum (taken from [path].md5 otherwise)')
@click.pass_obj
def publish_nanopore_download(obj: FskApi, unique_id, path, link=None, size=None, md5=None, hash=None):
  if md5:
    logger.warn(f"The --hash paramter is the new --md5 parameter")
    hash=f"md5.{md5}"
  ret = FskApi().publish_nanopore_download(unique_id, path, link=link, size=size, hash=hash)
  click.echo(json.dumps(serializeOntFlowcellRun(ret), indent=2, sort_keys=True))

@cli.group(short_help='seqmate filemanager (admin only)')
def datafile():
  pass

@datafile.command(short_help='post datafile to seqmate', name='post')
@click.argument('path')
@click.option('--url', '-u', help="Override automatically generated URL")
@click.option('--size', '-s', help="Override automatically determined size")
@click.option('--md5', '-m', help='DEPRECATED, use hash instead -- explicit md5 sum (taken from [path].md5 otherwise)')
@click.option('--hash', '-h', help='explicit md5 sum (taken from [path].md5 otherwise)')
@click.option('--filetype', '-f', help="Filetype", default="Misc")
@click.pass_obj
def post_datafile(obj: FskApi, path, url=None, size=None, md5=None, filetype='Misc', hash=None):
  if md5:
    logger.warn(f"The --hash paramter is the new --md5 parameter")
    hash=f"md5.{md5}"
  ret = FskApi().post_datafile(path=path, link=url, size=size, hash=hash, filetype=filetype)
  click.echo(json.dumps(ret, indent=2))

@datafile.command(short_help='delete datafile', name='delete')
@click.argument('path')
@click.pass_obj
def delete_datafile(obj: FskApi, path):
  ret = FskApi().delete_datafile(path)
  if ret['msg'] == 'Deleted.':
    logger.info("Deleted.")
  else:
    logger.warning("Weird?")

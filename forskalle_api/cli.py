import click
import click_log
import json
import logging
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


@click.group()
@click_log.simple_verbosity_option(logger)
def cli():
    """Fsk3 CLI - sequencing metadata made easy."""
    pass

@cli.command(short_help="suggest a few xkcd passphrases")
def generate_passwords():
  print(json.dumps(FskApi().generate_passwords(), indent=2))

@cli.command(short_help='get barcodes for a lane/smrtcell/nanopore run')
@click.argument('identifier')
@click.option('--platform', '-p', default='Illumina', help='Illumina, Pacbio or ONT')
def get_barcodes(identifier, platform='Illumina'):
  """Get Barcodes for a Sequencing Run. 

  The value for IDENTIFIER depends on the platform. It is [flowcell]_[lane] for Illumina, and the UUID for other platforms.

  If you are a user, at least one sample on the lane must belong to you."""
  if platform == 'Illumina':
    (flowcell, _, lane) = identifier.partition('_')
    ret = FskApi().get_illumina_barcodes(flowcell, lane)
  elif platform == 'Pacbio':
    ret = FskApi().get_smrtcell_barcodes(identifier)
  elif platform == 'ONT':
    ret = FskApi().get_nanopore_barcodes(identifier)
  print(json.dumps(ret, indent=2))
    

@cli.command(short_help='register smrtcell report URL in Forskalle (admin only)')
@click.argument('unique_id')
@click.argument('url')
def post_pacbio_report_url(unique_id, url):
  ret = FskApi().publish_smrtcell_report(unique_id, url)
  print(json.dumps(ret, indent=2))

@cli.command(short_help='register smrtcell data download link in Forskalle (admin only')
@click.argument('unique_id')
@click.argument('path')
@click.option('--link', '-l', help='explicit link name (last part of URL)')
@click.option('--size', '-s', help='explicit file size')
@click.option('--md5', '-m', help='explicit md5 sum (taken from [path].md5 otherwise)')
def publish_pacbio_download(unique_id, path, link=None, size=None, md5=None):
  ret = FskApi().publish_smrtcell_download(unique_id, path, link=link, size=size, md5=md5)
  print(json.dumps(ret, indent=2))

@cli.command(short_help='import a pacbio run from subreadset.xml')
@click.argument('path')
def import_subreadset(path):
  with open(path, 'r') as fh:
    subreadset = fh.read()
  ret = FskApi().import_subreadset(subreadset)
  print(json.dumps(ret, indent=2))

@cli.command(short_help='register nanopore report URL in Forskalle (admin only)')
@click.argument('unique_id')
@click.argument('url')
def post_nanopore_report_url(unique_id, url):
  ret = FskApi().publish_nanopore_report(unique_id, url)
  print(json.dumps(ret, indent=2))

@cli.command(short_help='register nanopore data download link in Forskalle (admin only')
@click.argument('unique_id')
@click.argument('path')
@click.option('--link', '-l', help='explicit link name (last part of URL)')
@click.option('--size', '-s', help='explicit file size')
@click.option('--md5', '-m', help='explicit md5 sum (taken from [path].md5 otherwise)')
def publish_nanopore_download(unique_id, path, link=None, size=None, md5=None):
  ret = FskApi().publish_nanopore_download(unique_id, path, link=link, size=size, md5=md5)
  print(json.dumps(ret, indent=2))


@cli.command(short_help='list sequenced samples')
@click.option('--sample', '-s', help='sample id (can be specified multiple times)', multiple=True)
@click.option('--multi', '-m', help='multiplex id (can be specified multiple times)', multiple=True)
@click.option('--request', '-r', help='request id (can be specified multiple times)', multiple=True)
@click.option('--limit', '-l', help='max rows', type=int, default=100)
@click.option('--page', '-p', help='Page (to return next [limit] rows', type=int, default=1)
@click.option('--csv', is_flag=True)
@click.option('--admin', is_flag=True, help='Show all users, available only with API key')
def list_sequenced_samples(sample, multi, request, limit, page, csv, admin):
  filters = SequencedSampleFilters(sample_id=sample, multi_id=multi, request_id=request)
  ret = FskApi().list_sequenced_samples(make_query(filters, limit, page), csv, admin)
  if csv:
    print(ret)
  else:
    print(json.dumps(ret, indent=2))


@cli.command(short_help='list samples')
@click.option('--id_from', help='min id', type=int)
@click.option('--id_to', help='max id', type=int)
@click.option('--scientist', help="Scientist name, only useful with admin query")
@click.option('--group', help="Group name, only useful with admin query")
@click.option('--limit', '-l', help='max rows', type=int, default=100)
@click.option('--page', '-p', help='Page (to return next [limit] rows', type=int, default=1)
@click.option('--csv', is_flag=True)
@click.option('--admin', is_flag=True, help='Show all users, available only with admin key')
def list_samples(id_from, id_to, scientist, group, limit, page, csv, admin):
  filters = SampleFilters(id_from=id_from, id_to=id_to, scientist=scientist, group=group)
  ret = FskApi().list_samples(make_query(filters, limit, page), csv, admin)
  if csv:
    print(ret)
  else:
    print(json.dumps(ret, indent=2))

@cli.command(short_help='list samples of all groups you belong to')
@click.option('--id_from', help='min id', type=int)
@click.option('--id_to', help='max id', type=int)
@click.option('--scientist', help="Scientist name")
@click.option('--group', help="Group name, useful if you belong to many groups.")
@click.option('--limit', '-l', help='max rows', type=int, default=100)
@click.option('--page', '-p', help='Page (to return next [limit] rows', type=int, default=1)
@click.option('--csv', is_flag=True)
def list_group_samples(id_from, id_to, scientist, group, limit, page, csv):
  filters = SampleFilters(id_from=id_from, id_to=id_to, scientist=scientist, group=group)
  ret = FskApi().list_group_samples(make_query(filters, limit, page), csv)
  if csv:
    print(ret)
  else:
    print(json.dumps(ret, indent=2))


@cli.command(short_help='get sample metadata')
@click.argument('sample_id')
def get_sample(sample_id):
  ret = FskApi().get_sample(sample_id)
  print(json.dumps(ret, indent=2))

@cli.command(short_help='get sequencing runs for a sample')
@click.argument('sample_id')
@click.option('--csv', is_flag=True)
def get_sample_sequencing(sample_id, csv=False):
  ret = FskApi().get_sample_sequencing_runs(sample_id, csv)
  if csv:
    print(ret)
  else:
    print(json.dumps(ret, indent=2))

@cli.command(short_help='update sequencing run status for a sample')
@click.argument('sample_id')
@click.option('--status', '-s', type=click.Choice(['Ok', 'Repeat', 'Failed'], case_sensitive=False), default="Ok")
@click.option('--vendor_id', help='Flowcell ID when there are multiple runs for a sample')
def set_sequencing_status(sample_id, status='Ok', vendor_id=None):
  api = FskApi()
  seqsamps = api.get_sample_sequencing_runs(sample_id)
  runs = {}
  for seqsamp in seqsamps:
    v_id = seqsamp['run_unit']['run']['vendor_id']
    if not v_id in runs:
      runs[v_id] = seqsamp['run_unit']['run']
      runs[v_id]['seqsamps']=[]
    runs[v_id]['seqsamps'].append(seqsamp)
  
  if len(runs) > 1 and not vendor_id:
    logger.info("Multiple runs found:")
    for vendor_id in runs.keys():
      logger.info(f"- {vendor_id}")
    raise click.ClickException("Please to tell me which run to fiddle with (hint: --vendor_id)")
  run = runs.popitem()[1] if not vendor_id else runs.get(vendor_id)
  if not run:
    raise click.ClickException(f"Run {vendor_id} not found!")
  
  unit_name = 'lanes' if run['platform'] == 'Illumina' else 'smrtcells' if run['platform'] == 'Pacbio' else 'ont_flowcell_runs' if run['platform'] == 'ONT' else None
  db_run = api.get(f"/api/runs/{run['platform'].lower()}/{run['vendor_id']}")
  for db_unit in db_run[unit_name]:
    for seqsamp in run['seqsamps']:
      if seqsamp['unit_id'] == db_unit['unit_id']:
        for db_ss in db_unit['sequenced_samples']:
          if db_ss['reqsamp_id'] == seqsamp['reqsamp_id']:
            logger.debug(f"seqsamp {db_ss['id']} found on unit {db_unit['unit_id']}, setting status to {status}")
            db_ss['status']=status
  ret = api.post(f"/api/runs/{run['platform'].lower()}/{run['vendor_id']}", db_run)
  logger.info(f"Run {ret['vendor_id']} updated, new status: {ret['status']}")



@cli.command(short_help='list multiplexes')
@click.option('--scientist', help="Scientist name, only useful with admin query")
@click.option('--group', help="Group name, only useful with admin query")
@click.option('--limit', '-l', help='max rows', type=int, default=100)
@click.option('--page', '-p', help='Page (to return next [limit] rows', type=int, default=1)
@click.option('--csv', is_flag=True)
@click.option('--admin', is_flag=True, help='Show all users, available only with admin key')
def list_multis(scientist, group, limit, page, csv, admin):
  filters = MultiplexFilters(scientist=scientist, group=group)
  ret = FskApi().list_multis(make_query(filters, limit, page), csv, admin)
  if csv:
    print(ret)
  else:
    print(json.dumps(ret, indent=2))

@cli.command(short_help='get multiplex metadata')
@click.argument('multi_id')
def get_multi(multi_id):
  if multi_id.startswith('M'):
    multi_id = multi_id[1:]
  ret = FskApi().get_multi(multi_id)
  print(json.dumps(ret, indent=2))

@cli.command(short_help='list requests')
@click.option('--scientist', help="Scientist name, only useful with admin query")
@click.option('--group', help="Group name, only useful with admin query")
@click.option('--limit', '-l', help='max rows', type=int, default=100)
@click.option('--page', '-p', help='Page (to return next [limit] rows', type=int, default=1)
@click.option('--csv', is_flag=True)
@click.option('--admin', is_flag=True, help='Show all users, available only with admin key')
def list_requests(scientist, group, limit, page, csv, admin):
  filters = RequestFilters(scientist=scientist, group=group)
  ret = FskApi().list_requests(make_query(filters, limit, page), csv, admin)
  if csv:
    print(ret)
  else:
    print(json.dumps(ret, indent=2))

@cli.command(short_help='get request metadata (DEPRECATED, use `request [id] get` instead')
@click.argument('request_id')
def get_request(request_id):
  if request_id.startswith('R'):
    request_id = request_id[1:]
  ret = FskApi().get_request(request_id)
  print(json.dumps(ret, indent=2))

@cli.command(short_help='post datafile to seqmate')
@click.argument('path')
@click.option('--url', '-u', help="Override automatically generated URL")
@click.option('--size', '-s', help="Override automatically determined size")
@click.option('--md5', '-m', help="MD5 sum, read from [path].md5 if not specified")
@click.option('--filetype', '-f', help="Filetype", default="Misc")
def post_datafile(path, url=None, size=None, md5=None, filetype='Misc'):
  ret = FskApi().post_datafile(path, url, size, md5, filetype)
  print(json.dumps(ret, indent=2))

@cli.command(short_help='delete datafile')
@click.argument('path')
def delete_datafile(path):
  ret = FskApi().delete_datafile(path)
  if ret['msg'] == 'Deleted.':
    logger.info("Deleted.")
  else:
    logger.warning("Weird?")
  

@cli.group(short_help='request related commands')
@click.argument('id')
@click.pass_context
def request(ctx, id):
  if id.startswith('R'):
    id = id[1:]
  ctx.ensure_object(dict)
  ctx.obj['api']=FskApi()
  ctx.obj['request']=ctx.obj['api'].get_request(id)

@request.command(short_help='get metadata', name='get')
@click.option('--out', '-o', type=click.File("w"), default='-')
@click.pass_context
def get_request_data(ctx, out):
  out.write(json.dumps(ctx.obj['request'], indent=2))

@request.command(short_help='update request', name='update')
@click.option('--json', '-j', 'input',  type=click.File("r"), default='-')
@click.pass_context
def set_request_data(ctx, input):
  update=json.load(input)
  ret = ctx.obj['api'].post(f"/api/requests/{ctx.obj['request']['id']}", update)
  logger.info(f"Update request {ret['id']}")

@request.command(short_help='set status')
@click.argument('status', type=click.Choice(['Completed', 'Aborted', 'Accepted'], case_sensitive=False))
@click.pass_context
def set_status(ctx, status):
  ctx.obj['request']['status']=status
  ret = ctx.obj['api'].post(f"/api/requests/{ctx.obj['request']['id']}", ctx.obj['request'])
  logger.info(f"Updated request {ret['id']}, new status {ret['status']}")
  for rl in ret['request_lanes']:
    logger.info(f" lane {rl['num']} status {rl['status']}")
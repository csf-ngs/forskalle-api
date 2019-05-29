from __future__ import print_function

import click
import json
from forskalle_api.fsk_api import FskApi

def parse_paging(params, limit, page):
  if limit > 0 and page > 0:
    params['page']=page
    params['limit']=limit
  return params


@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    """Fsk3 CLI - sequencing metadata made easy."""
    pass

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
    

@cli.command(short_help='register smrtcell report URL in Forskalle')
@click.argument('unique_id')
@click.argument('url')
def post_report_url(unique_id, url):
  ret = FskApi().publish_smrtcell_report(unique_id, url)
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
  params = parse_paging({}, limit, page)
  if sample != None:
    params['filter.sample_id']=sample
  if admin:
    ret = FskApi().admin_list_sequenced_samples(params, csv)
  else:
    ret = FskApi().list_sequenced_samples(params, csv)
  if csv:
    print(ret)
  else:
    print(json.dumps(ret, indent=2))


@cli.command(short_help='list samples')
@click.option('--id_from', help='min id', type=int)
@click.option('--id_to', help='max id', type=int)
@click.option('--limit', '-l', help='max rows', type=int, default=100)
@click.option('--page', '-p', help='Page (to return next [limit] rows', type=int, default=1)
@click.option('--csv', is_flag=True)
@click.option('--admin', is_flag=True, help='Show all users, available only with API key')
def list_samples(id_from, id_to, limit, page, csv, admin):
  params = parse_paging({}, limit, page)
  if page != 0:
    params['limit']=limit
    params['page']=page
  if id_from != None:
    params['filter.id_from']=id_from
  if id_to != None:
    params['filter.id_to']=id_to
  if admin:
    ret = FskApi().admin_list_samples(params, csv)
  else:
    ret = FskApi().list_samples(params, csv)
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

@cli.command(short_help='get multiplex metadata')
@click.argument('multi_id')
def get_multi(multi_id):
  if multi_id.startswith('M'):
    multi_id = multi_id[1:]
  ret = FskApi().get_multi(multi_id)
  print(json.dumps(ret, indent=2))

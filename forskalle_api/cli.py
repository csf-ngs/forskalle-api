from __future__ import print_function

import click
import json
from forskalle_api.fsk_api import FskApi

@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    """Fsk3 CLI - sequencing metadata made easy."""
    pass

@cli.command(short_help='get sample metadata')
@click.argument('sample_id')
def get_sample(sample_id):
  ret = FskApi().get_sample(sample_id)
  print(json.dumps(ret, indent=2))

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

@cli.command(short_help='get sequencing runs for a sample')
@click.argument('sample_id')
@click.option('--csv', is_flag=True)
def get_sample_sequencing(sample_id, csv=False):
  ret = FskApi().get_sample_sequencing_runs(sample_id, csv)
  if csv:
    print(ret)
  else:
    print(json.dumps(ret, indent=2))
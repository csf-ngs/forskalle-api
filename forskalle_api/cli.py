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

@cli.command(short_help='register smrtcell report URL in Forskalle')
@click.argument('unique_id')
@click.argument('url')
def post_report_url(unique_id, url):
  ret = FskApi().publish_smrtcell_report(unique_id, url)
  print(json.dumps(ret, indent=2))

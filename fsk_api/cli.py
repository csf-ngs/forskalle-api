from __future__ import print_function

import click
import json
from fsk_api.fsk_api import FskApi

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
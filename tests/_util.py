from contextlib import contextmanager
import os
import unittest
from click.testing import CliRunner

from unittest import mock
import typing
from forskalle_api.fsk_api import FskApi


dummy_cfg = {
  'fsk_api_base': 'http://testha.se/fsk',
  'fsk_api_key': 'fsk-geheim',
}

dummy_env = {
  'FSK_API_BASE': dummy_cfg['fsk_api_base'],
  'FSK_API_KEY': dummy_cfg['fsk_api_key'],
}

@contextmanager
def _gen_mocks(obj, meths) -> typing.Generator[typing.Dict[str, mock.MagicMock], None, None]:
  mocks = {}
  mocked = {}
  for meth in meths:
    mocks[meth] = mock.patch.object(obj, meth)
    mocked[meth] = mocks[meth].start()

  yield mocked

  for k in mocks:
    mocks[k].stop()

@contextmanager
def mock_fsk_api() -> typing.Generator[typing.Dict[str, mock.MagicMock], None, None]:
  with _gen_mocks(FskApi, ['get', 'post', 'delete']) as mocked:
    yield mocked

class TestBase(unittest.TestCase):
  def setUp(self):
    for k in dummy_env:
      os.environ[k]=dummy_env[k]
    self.runner = CliRunner()

  def tearDown(self):
    for k in dummy_env:
      os.environ.pop(k)
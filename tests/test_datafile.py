from ._util import mock_fsk_api, TestBase
from unittest import mock
import os.path

from forskalle_api.cli import cli

class TestDatafile(TestBase):
  def test_help_post_datafile(self):
    result = self.runner.invoke(cli, ['post-datafile', '--help'], catch_exceptions=False)
    self.assertEqual(result.exit_code, 0)

  def test_post(self):
    with mock_fsk_api() as mock_api, self.runner.isolated_filesystem():
      mock_api['post'].return_value = '{ "allt", "är bra"}'
      with open('datafile', 'w') as fh:
        fh.write("testdata\n")
      with open('datafile.md5', 'w') as fh:
        fh.write("testsum\n")
      fullpath = os.path.abspath('datafile')
      result = self.runner.invoke(cli, ['post-datafile',
        'datafile'
      ], catch_exceptions=False)
    self.assertEqual(result.exit_code, 0)
    mock_api['post'].assert_called_with(
      '/api/datafiles', {
        'path': fullpath,
        'url': mock.ANY,
        'size': 9,
        'hash': 'md5.testsum',
        'filetype': 'Misc'
      }
    )

  def test_post_hash_ignore_file(self):
    with mock_fsk_api() as mock_api, self.runner.isolated_filesystem():
      mock_api['post'].return_value = '{ "allt", "är bra"}'
      with open('datafile', 'w') as fh:
        fh.write("testdata\n")
      with open('datafile.md5', 'w') as fh:
        fh.write("testsum\n")
      fullpath = os.path.abspath('datafile')
      result = self.runner.invoke(cli, ['post-datafile',
        'datafile',
        '--hash', 'blurb'
      ], catch_exceptions=False)
    self.assertEqual(result.exit_code, 0)
    mock_api['post'].assert_called_with(
      '/api/datafiles', {
        'path': fullpath,
        'url': mock.ANY,
        'size': 9,
        'hash': 'blurb',
        'filetype': 'Misc'
      }
    )

  def test_post_hash(self):
    with mock_fsk_api() as mock_api, self.runner.isolated_filesystem():
      mock_api['post'].return_value = '{ "allt", "är bra"}'
      with open('datafile', 'w') as fh:
        fh.write("testdata\n")
      fullpath = os.path.abspath('datafile')
      result = self.runner.invoke(cli, ['post-datafile',
        'datafile',
        '--hash', 'blurb'
      ], catch_exceptions=False)
    self.assertEqual(result.exit_code, 0)
    mock_api['post'].assert_called_with(
      '/api/datafiles', {
        'path': fullpath,
        'url': mock.ANY,
        'size': 9,
        'hash': 'blurb',
        'filetype': 'Misc'
      }
    )

  def test_post_md5(self):
    with mock_fsk_api() as mock_api, self.runner.isolated_filesystem():
      mock_api['post'].return_value = '{ "allt", "är bra"}'
      with open('datafile', 'w') as fh:
        fh.write("testdata\n")
      fullpath = os.path.abspath('datafile')
      result = self.runner.invoke(cli, ['post-datafile',
        'datafile',
        '--md5', 'blurb'
      ], catch_exceptions=False)
    self.assertEqual(result.exit_code, 0)
    mock_api['post'].assert_called_with(
      '/api/datafiles', {
        'path': fullpath,
        'url': mock.ANY,
        'size': 9,
        'hash': 'md5.blurb',
        'filetype': 'Misc'
      }
    )

  def test_post_url(self):
    with mock_fsk_api() as mock_api, self.runner.isolated_filesystem():
      mock_api['post'].return_value = '{ "allt", "är bra"}'
      with open('datafile', 'w') as fh:
        fh.write("testdata\n")
      with open('datafile.md5', 'w') as fh:
        fh.write("testsum\n")
      fullpath = os.path.abspath('datafile')
      result = self.runner.invoke(cli, ['post-datafile',
        'datafile',
        '--url', 'http://da.ham/'
      ], catch_exceptions=False)
    self.assertEqual(result.exit_code, 0)
    mock_api['post'].assert_called_with(
      '/api/datafiles', {
        'path': fullpath,
        'url': 'http://da.ham/',
        'size': 9,
        'hash': 'md5.testsum',
        'filetype': 'Misc'
      }
    )
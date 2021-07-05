from ._util import mock_fsk_api, TestBase
from unittest import mock
import os.path

from forskalle_api.cli import cli

class TestDatafile(TestBase):
  def test_help_post_datafile(self):
    result = self.runner.invoke(cli, ['datafile', 'post', '--help'], catch_exceptions=False)
    self.assertEqual(result.exit_code, 0)

  def test_post(self):
    with mock_fsk_api() as mock_api, self.runner.isolated_filesystem():
      mock_api['post'].return_value = '{ "allt", "är bra"}'
      with open('datafile', 'w') as fh:
        fh.write("testdata\n")
      with open('datafile.md5', 'w') as fh:
        fh.write("testsum\n")
      fullpath = os.path.abspath('datafile')
      result = self.runner.invoke(cli, ['datafile', 'post',
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
    self.assertRegex(mock_api['post'].call_args[0][1]['url'], r'^[\w\d]+_datafile$')

  def test_post_hash_ignore_file(self):
    with mock_fsk_api() as mock_api, self.runner.isolated_filesystem():
      mock_api['post'].return_value = '{ "allt", "är bra"}'
      with open('datafile', 'w') as fh:
        fh.write("testdata\n")
      with open('datafile.md5', 'w') as fh:
        fh.write("testsum\n")
      fullpath = os.path.abspath('datafile')
      result = self.runner.invoke(cli, ['datafile', 'post',
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
      result = self.runner.invoke(cli, ['datafile', 'post',
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
      result = self.runner.invoke(cli, ['datafile', 'post',
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
      result = self.runner.invoke(cli, ['datafile', 'post',
        'datafile',
        '--url', 'http://da.ham/'
      ], catch_exceptions=False)
    self.assertEqual(result.exit_code, 1)
    self.assertRegex(result.output, r'absolute URLs')
    
  def test_post_url_path(self):
    with mock_fsk_api() as mock_api, self.runner.isolated_filesystem():
      mock_api['post'].return_value = '{ "allt", "är bra"}'
      with open('datafile', 'w') as fh:
        fh.write("testdata\n")
      with open('datafile.md5', 'w') as fh:
        fh.write("testsum\n")
      fullpath = os.path.abspath('datafile')
      result = self.runner.invoke(cli, ['datafile', 'post',
        'datafile',
        '--url', 'oink'
      ], catch_exceptions=False)
    self.assertEqual(result.exit_code, 0)
    mock_api['post'].assert_called_with(
      '/api/datafiles', {
        'path': fullpath,
        'url': 'oink',
        'size': 9,
        'hash': 'md5.testsum',
        'filetype': 'Misc'
      }
    )
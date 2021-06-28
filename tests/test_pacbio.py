from ._util import mock_fsk_api, TestBase
from unittest import mock
import os.path

from forskalle_api.cli import cli

class TestPacbio(TestBase):
  def test_help_publish_donwload(self):
    result = self.runner.invoke(cli, ['publish-pacbio-download', '--help'], catch_exceptions=False)
    self.assertEqual(result.exit_code, 0)

  def test_help_import_subreadset(self):
    result = self.runner.invoke(cli, ['import-subreadset', '--help'], catch_exceptions=False)
    self.assertEqual(result.exit_code, 0)

  def test_help_post_report(self):
    result = self.runner.invoke(cli, ['post-pacbio-report-url', '--help'], catch_exceptions=False)
    self.assertEqual(result.exit_code, 0)

  def test_publish_download(self):
    with mock_fsk_api() as mock_api, self.runner.isolated_filesystem():
      mock_api['post'].return_value = "{ 'allet': 'jut' }"
      with open('testdata', 'w') as fh:
        fh.write("testdata\n")
      with open('testdata.md5', 'w') as fh:
        fh.write('checksum\n')
      fullpath = os.path.abspath('testdata')
      result = self.runner.invoke(cli, ['publish-pacbio-download',
        'unique',
        'testdata'
      ], catch_exceptions=False)
    self.assertEqual(result.exit_code, 0)
    mock_api['post'].assert_called_with(
      '/api/runs/pacbio/smrtcells/unique', {
        'datafiles_path': fullpath,
        'datafiles_url': mock.ANY,
        'datafiles_size': 9,
        'datafiles_link': None,
        'datafiles_hash': 'md5.checksum'
      }
    )
    self.assertRegex(mock_api['post'].call_args[0][1]['datafiles_url'], r'^https://ngs\.vbcf\.ac\.at/filemanager/byurl/[\w\d]+_testdata$')

  def test_publish_download_md5(self):
    with mock_fsk_api() as mock_api, self.runner.isolated_filesystem():
      mock_api['post'].return_value = "{ 'allet': 'jut' }"
      with open('testdata', 'w') as fh:
        fh.write("testdata\n")
      fullpath = os.path.abspath('testdata')
      result = self.runner.invoke(cli, ['publish-pacbio-download',
        'unique',
        'testdata',
        '--md5', 'oink',
      ], catch_exceptions=False)
    self.assertEqual(result.exit_code, 0)
    mock_api['post'].assert_called_with(
      '/api/runs/pacbio/smrtcells/unique', {
        'datafiles_path': fullpath,
        'datafiles_url': mock.ANY,
        'datafiles_size': 9,
        'datafiles_link': None,
        'datafiles_hash': 'md5.oink'
      }
    )

  def test_publish_download_hash_ignore_file(self):
    with mock_fsk_api() as mock_api, self.runner.isolated_filesystem():
      mock_api['post'].return_value = "{ 'allet': 'jut' }"
      with open('testdata', 'w') as fh:
        fh.write("testdata\n")
      with open('testdata.md5', 'w') as fh:
        fh.write('checksum\n')
      fullpath = os.path.abspath('testdata')
      result = self.runner.invoke(cli, ['publish-pacbio-download',
        'unique',
        'testdata',
        '--hash', 'oink',
      ], catch_exceptions=False)
    self.assertEqual(result.exit_code, 0)
    mock_api['post'].assert_called_with(
      '/api/runs/pacbio/smrtcells/unique', {
        'datafiles_path': fullpath,
        'datafiles_url': mock.ANY,
        'datafiles_size': 9,
        'datafiles_link': None,
        'datafiles_hash': 'oink'
      }
    )

  def test_publish_download_hash(self):
    with mock_fsk_api() as mock_api, self.runner.isolated_filesystem():
      mock_api['post'].return_value = "{ 'allet': 'jut' }"
      with open('testdata', 'w') as fh:
        fh.write("testdata\n")
      fullpath = os.path.abspath('testdata')
      result = self.runner.invoke(cli, ['publish-pacbio-download',
        'unique',
        'testdata',
        '--hash', 'oink',
      ], catch_exceptions=False)
    self.assertEqual(result.exit_code, 0)
    mock_api['post'].assert_called_with(
      '/api/runs/pacbio/smrtcells/unique', {
        'datafiles_path': fullpath,
        'datafiles_url': mock.ANY,
        'datafiles_size': 9,
        'datafiles_link': None,
        'datafiles_hash': 'oink'
      }
    )

  def test_publish_download_link(self):
    with mock_fsk_api() as mock_api, self.runner.isolated_filesystem():
      mock_api['post'].return_value = "{ 'allet': 'jut' }"
      with open('testdata', 'w') as fh:
        fh.write("testdata\n")
      with open('testdata.md5', 'w') as fh:
        fh.write('checksum\n')
      fullpath = os.path.abspath('testdata')
      result = self.runner.invoke(cli, ['publish-pacbio-download',
        'unique',
        'testdata',
        '--link', 'http://da.ham/',
      ], catch_exceptions=False)
    self.assertEqual(result.exit_code, 0)
    mock_api['post'].assert_called_with(
      '/api/runs/pacbio/smrtcells/unique', {
        'datafiles_path': fullpath,
        'datafiles_url': 'http://da.ham/',
        'datafiles_size': 9,
        'datafiles_link': None,
        'datafiles_hash': 'md5.checksum'
      }
    )

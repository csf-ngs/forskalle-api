import typing
import click
import requests
import yaml
import os
import os.path
import datetime
from uuid import uuid4

import logging
logger = logging.getLogger()

class FskError(Exception):
  def __init__(self, code, detail, status=None, doclink=None, line=None, **kwargs):
    self.status = status
    self.code = code
    self.detail = detail
    self.doclink = doclink
    self.line = line
    self.args = kwargs
  
  def __str__(self):
    return "FSK-ERROR: {status} {code} {detail}".format(status=self.status, code=self.code, detail=self.detail)

class FskApi:
  config_file = '~/.fsk_api.yml'

  def __init__(self, base=None, key=None):
    if not base:
      base = os.environ.get('FSK_API_BASE')
    if not key:
      key = os.environ.get('FSK_API_KEY')
    self.config_file = os.environ.get('FSK_API_CFG', self.config_file)
    try:
      with open(os.path.expanduser(self.config_file), 'r') as yml:
        cfg = yaml.load(yml, Loader=yaml.SafeLoader)
    except FileNotFoundError:
      cfg = {}

    if not base:
      base=cfg.get('fsk_api_base')
    if not key:
      key=cfg.get('fsk_api_key')
    if not base or not key:
      raise Exception("Please configure FSK_API_BASE and FSK_API_KEY!")
    if base.endswith('/'):
      base = base[:-1]

    self.base: str = base
    self.key: str = key
    self.username: typing.Optional[str] = None

  def handle_error(self, r):
    try:
      json = r.json()
    except:
      r.raise_for_status()
    if 'errors' in json:
      raise FskError(**json['errors'][0])
    else:
      r.raise_for_status()

  def make_headers(self):
    return { 'X-API-Key': self.key, 'Accept': 'application/json' }
  
  def get(self, route, params=None):
    if params and type(params).__name__ != 'dict':
      params = params.generate_params()
    r = requests.get(self.base+route, headers=self.make_headers(), params=params)
    if r.status_code != requests.codes.ok:
      self.handle_error(r)
    return r.json()

  def get_csv(self, route, params=None):
    headers = self.make_headers()
    headers['Accept']='text/csv'
    r = requests.get(self.base+route, headers=headers, params=params)
    if r.status_code != requests.codes.ok:
      self.handle_error(r)
    return r.text


  def post(self, route, data):
    r = requests.post(self.base+route, headers=self.make_headers(), json=data)
    if r.status_code != requests.codes.ok:
      self.handle_error(r)
    return r.json()

  def post_file(self, route, files, data=None):
    r = requests.post(self.base+route, headers=self.make_headers(), data=data, files=files)
    if r.status_code != requests.codes.ok:
      self.handle_error(r)
    return r.json()

  def post_csv(self, route, files, data=None):
    headers = self.make_headers()
    headers['Accept']='text/csv'
    r = requests.post(self.base+route, headers=headers, data=data, files=files)
    if r.status_code != requests.codes.ok:
      self.handle_error(r)
    return r.text

  def put(self, route, data):
    r = requests.put(self.base+route, headers=self.make_headers(), json=data)
    if r.status_code != requests.codes.ok:
      self.handle_error(r)
    return r.json()

  def delete(self, route, data=None):
    r = requests.delete(self.base+route, headers=self.make_headers(), json=data)
    if r.status_code != requests.codes.ok:
        self.handle_error(r)
    return r.json()

  def current_account(self):
    json = self.get("/api/account")
    self.username=json['username']
    return json
  
  def current_key(self):
    json = self.get("/api/key")
    self.username = json['user']['username']
    return json

  def list_scientists(self, params=None):
    return self.get("/api/scientists", params=params)
  
  def get_scientist(self, id):
    return self.get("/api/scientists/{id}".format(id=id))

  def list_groups(self, params=None):
    return self.get("/api/groups", params=params)
  
  def get_group(self, id):
    return self.get("/api/groups/{id}".format(id=id))
 
  def list_runs_illumina(self, params=None):
    return self.get("/api/runs/illumina", params=params)

  def get_run_illumina(self, id):
    return self.get("/api/runs/illumina/{id}".format(id=id))
  
  def get_smrtcell_info(self, run: str, well: str):
    return self.get(f"/api/runs/pacbio/{run}/{well}")
  
  def get_ont_flowcell_info(self, run: str):
    return self.get(f"/api/runs/ont/flowcell_runs/{run}")
 
  def generate_passwords(self):
    return self.get("/api/scientists/generate_passwords")

  def _prepare_datafile(self, path: str, link: typing.Optional[str]=None, size: typing.Optional[int]=None, hash: typing.Optional[str]=None) -> typing.Tuple[str, str, str, int, str]:
    path = os.path.abspath(path)
    if not link:
      uuid = str(uuid4())[0:8]
      link = f'{uuid}_{os.path.basename(path)}'

    absolute_link = link
    if not absolute_link.startswith('http'):
      absolute_link = f'https://ngs.vbcf.ac.at/filemanager/byurl/{link}'

    if not size:
      size = os.path.getsize(path)
    if not hash:
      if not os.path.exists(path + '.md5'):
        raise Exception("md5 not provided and {path}.md5 not found.".format(path=path))
      with open(path + '.md5') as md5fh:
        hash="md5."+md5fh.readline().strip().split()[0]
    
    return (path, link, absolute_link, size, hash)

  def _publish_download(self, where, unique_id, path, link=None, size=None, hash=None, hinkskalle=None):
    if path:
      (path, link, absolute_link, size, hash) = self._prepare_datafile(path, link, size, hash)
    else:
      absolute_link = link
      if not absolute_link.startswith('http'):
        absolute_link = f"https://ngs.vbcf.ac.at/filemanager/byurl/{absolute_link}"
    
    cell_base = 'smrtcells' if where == 'pacbio' else 'flowcell_runs'
    return self.post(f"/api/runs/{where}/{cell_base}/{unique_id}", {
      'datafiles_path': path,
      'datafiles_url': absolute_link,
      'datafiles_size': size,
      'datafiles_link': hinkskalle,
      'datafiles_hash': hash,
    })
  
  def publish_smrtcell_report(self, unique_id, report_url):
    return self.post("/api/runs/pacbio/smrtcells/{unique_id}".format(unique_id=unique_id), { 'report_url': report_url })
  
  def post_smrtcell_results(self, unique_id, results):
    return self.post("/api/runs/pacbio/smrtcells/{unique_id}/results".format(unique_id=unique_id), results)

  def publish_smrtcell_download(self, unique_id, path, **kwargs):
    return self._publish_download(where='pacbio', unique_id=unique_id, path=path, **kwargs)

  def import_subreadset(self, subreadset):
    return self.post("/api/runs/pacbio/subreadset", { 'xml': subreadset })
  
  def get_illumina_barcodes(self, flowcell_id, lane):
    return self.get("/api/runs/illumina/{flowcell_id}/{lane}/barcodes".format(flowcell_id=flowcell_id, lane=lane))
  
  def get_smrtcell_barcodes(self, unique_id):
    return self.get("/api/runs/pacbio/smrtcells/{unique_id}/barcodes".format(unique_id=unique_id))



  def import_nanopore_run(self, metadata):
    return self.post("/api/runs/ont/flowcell_runs/import", metadata)

  def publish_nanopore_download(self, run_id, path, **kwargs):
    return self._publish_download(where='ont', unique_id=run_id, path=path, **kwargs)

  def post_nanopore_results(self, run_id, results):
    return self.post("/api/runs/ont/flowcell_runs/{run_id}/results".format(run_id=run_id), results)
  
  def publish_nanopore_report(self, run_id, report_url):
    return self.post("/api/runs/ont/flowcell_runs/{run_id}".format(run_id=run_id), { 'report_url': report_url })
  
  def get_nanopore_barcodes(self, run_id):
    return self.get("/api/runs/ont/flowcelL_runs/{run_id}/barcodes".format(run_id=run_id))

  def list_sequenced_samples(self, params=None, csv=False, admin=False):
    base = "/api/sequenced_samples"
    if admin:
      base += "/admin"
    if csv:
      return self.get_csv(base+".csv", params=params)
    else:
      return self.get(base, params=params)

  def admin_list_sequenced_samples(self, params=None, csv=False):
    return self.list_sequenced_samples(params, csv, admin=True)

  def get_sequenced_sample(self, id):
    return self.get("/api/sequenced_samples/{id}".format(id=id))

  def list_samples(self, params=None, csv=False, admin=False):
    base = "/api/samples"
    if admin:
      base += "/admin"
    if csv:
      return self.get_csv(base+".csv", params=params)
    else:
      return self.get(base, params=params)
  
  def list_group_samples(self, params=None, csv=False):
    if csv:
      return self.get_csv("/api/samples/group", params=params)
    else:
      return self.get("/api/samples/group", params=params)
  
  def admin_list_samples(self, params=None, csv=False):
    return self.list_samples(params, csv, admin=True)

  def get_sample(self, id):
    return self.get("/api/samples/{id}".format(id=id))

  def get_sample_sequencing_runs(self, sample_id, csv=False):
    url = "/api/samples/{sample_id}/sequencing".format(sample_id=sample_id)
    if csv:
      return self.get_csv(url+'.csv')
    else:
      return self.get(url)
  
  def get_multi(self, id):
    return self.get('/api/multiplexes/{multi_id}'.format(multi_id=id))
  
  def list_multis(self, params=None, csv=False, admin=False):
    base = "/api/multiplexes"+("/admin" if admin else "")
    if csv:
      return self.get_csv(base+".csv", params=params)
    else:
      return self.get(base, params=params)
    
  def get_request(self, id):
    return self.get("/api/requests/{request_id}".format(request_id=id))
    
  def admin_list_multis(self, params=None, csv=False):
    return self.list_multis(params, csv, admin=True)
  
  def list_requests(self, params=None, csv=False, admin=False):
    base = "/api/requests"+("/admin" if admin else "")
    if csv:
      return self.get_csv(base+".csv", params=params)
    else:
      return self.get(base, params=params)
  
  def post_datafile(self, path, link=None, size=None, md5=None, hash=None, filetype='Misc'):
    if md5:
      logger.warn(f"using deprecated md5 parameter, should be hash")
      hash = md5
    if link and link.startswith('http'):
      raise click.ClickException(f"absolute URLs will not work")
    (path, link, absolute_link, size, hash) = self._prepare_datafile(path, link, size, hash)
    return self.post('/api/datafiles', {
      'path': path,
      'url': link,
      'size': size,
      'hash': hash,
      'filetype': filetype,
    })
  
  def delete_datafile(self, path):
    path = os.path.abspath(path)
    return self.delete('/api/datafiles', {
      'path': path
    })

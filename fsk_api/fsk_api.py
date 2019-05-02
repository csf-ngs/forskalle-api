import requests
import yaml
import os
import os.path
import yaml
import datetime

class FskApi:
  default_file_name = '~/.fsk_api.yml'

  def __init__(self, base=os.environ.get('FSK_API_BASE', None), key=os.environ.get('FSK_API_KEY', None), api_conf=default_file_name):
    if not base or not key:
      with open(os.path.expanduser(api_conf), 'rb') as yml:
        cfg = yaml.load(yml, Loader=yaml.SafeLoader)
      if not base:
        base=cfg['fsk_api_base']
      if not key:
        key=cfg['fsk_api_key']
    if not base or not key:
      raise Exception("Please configure FSK_API_BASE and FSK_API_KEY!")
    self.base=base
    self.key=key
    self.username=None

  def handle_error(self, r):
    try:
      json = r.json()
    except:
      r.raise_for_status()
    if 'message' in json:
      raise Exception("FSK-ERROR: {message}".format(message=json['message']))
    else:
      r.raise_for_status()

  def make_headers(self):
    return { 'X-API-Key': self.key, 'Accept': 'application/json' }

  def get(self, route, params=None):
    r = requests.get(self.base+route, headers=self.make_headers(), params=params)
    if r.status_code != requests.codes.ok:
      self.handle_error(r)
    return r.json()

  def post(self, route, data):
    r = requests.post(self.base+route, headers=self.make_headers(), json=data)
    if r.status_code != requests.codes.ok:
      self.handle_error(r)
    return r.json()

  def post_file(self, route, files, data=None):
    r = requests.post(self.base+route, headers=self.make_headers(), data=data, files=files)
    if r.status_code != requests.codes.ok:
      self.handle_error(r)

  def put(self, route, data):
    r = requests.put(self.base+route, headers=self.make_headers(), json=data)
    if r.status_code != requests.codes.ok:
      self.handle_error(r)
    return r.json()

  def delete(self, route):
    r = requests.delete(self.base+route, headers=self.make_headers())
    if r.status_code != requests.codes.ok:
        self.handle_error(r)
    return r.json()

  def list_samples(self, params=None):
    return self.get("/api/samples", params=params)
  
  def admin_list_samples(self, params=None):
    return self.get("/api/samples/admin", params=params)
  
  def get_sample(self, id):
    return self.get("/api/samples/{id}".format(id=id))
  
  def current_account(self):
    json = self.get("/api/account")
    self.username=json['username']
    return json
  
  def current_key(self):
    json = self.get("api/key")
    self.username = json['user']['username']
    return json

  def list_scientists(self, params=None):
    return self.get("/api/scientists", params=params)
  
  def get_scientist(self, id):
    return self.get("/api/scientists/{id}")

  def list_groups(self, params=None):
    return self.get("/api/groups", params=params)
  
  def get_group(self, id):
    return self.get("/api/groups/{id}")

  def _publish_download(self, where, unique_id, path, link, size, md5):
    return self.post("/api/runs/{where}/smrtcells/{unique_id}".format(where=where, unique_id=unique_id), {
      'datafiles_path': path,
      'datafiles_url': link,
      'datafiles_size': size,
      'datafiles_md5': md5
    })
  
  def publish_smrtcell_report(self, unique_id, report_url):
    return self.post("/api/runs/pacbio/smrtcells/{unique_id}".format(unique_id=unique_id), { 'report_url': report_url })
  
  def post_smrtcell_results(self, unique_id, results):
    return self.post("/api/runs/pacbio/smrtcells/{unique_id}/results".format(unique_id=unique_id), results)

  def publish_smrtcell_download(self, **kwargs):
    return self._publish_download(where='pacbio', **kwargs)

  def import_subreadset(self, subreadset):
    return self.post("/api/runs/pacbio/subreadset", { 'xml': subreadset })
  
  def get_smrtcell_barcodes(self, unique_id):
    return self.get("/api/runs/pacbio/smrtcells/{unique_id}/barcodes".format(unique_id=unique_id))



  def import_nanopore_run(self, metadata):
    return self.post("/api/runs/ont/flowcell_runs/import", metadata)

  def post_nanopore_basecalls(self, run_id, path, basecalls, basecaller, basecalled=None, copied=None):
    if not basecalled:
      basecalled=datetime.now().isoformat()
    if not copied:
      copied = datetime.now().isoformat()
    
    return self.post("/api/runs/ont/flowcell_runs/{run_id}".format(run_id=run_id), {
      'basecalled': basecalled.replace('Z', '+00:00'),
      'basecaller': basecaller,
      'fastq_path': path,
      'copied': copied.replace('Z', '+00:00')
    })

  def publish_nanopore_download(self, run_id, **kwargs):
    return self._publish_download(where='ont', unique_id=run_id, **kwargs)

  def post_ont_results(self, run_id, results):
    return self.post("/api/runs/ont/flowcell_runs/{run_id}/results".format(run_id=run_id), results)
  
  def publish_nanopore_report(self, run_id, report_url):
    return self.post("/api/runs/ont/flowcell_runs/{run_id}".format(run_id=run_id), { 'report_url': report_url })
  
  def get_nanopore_barcodes(self, run_id):
    return self.get("/api/runs/ont/flowcelL_runs/{run_id}/barcodes".format(run_id=run_id))

  




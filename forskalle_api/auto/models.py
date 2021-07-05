from __future__ import annotations
from dataclasses import dataclass
import typing
from .queryparams import RequestLaneFilters


@dataclass
class AdaptorType:
  available: bool
  category: typing.Any
  description: str
  group: str
  group_id: typing.Union[int, float]
  multiplexing: bool
  name: str
  platform: str
  pos: str
  sequence: str

  
  group_ref: Group
  multiplexes: list[Multiplex]
  platform_ref: Platform
  samples: list[Sample]
  tags: list[Tag]


# ---

@dataclass
class ApiKey:
  active: bool
  created: str
  description: str
  expiration: str
  id: typing.Union[int, float]
  internal: bool
  key: str
  role: str
  scientist_id: typing.Union[int, float]

  
  routes: list[ApiKeyRoute]
  scientist_ref: Scientist


# ---

@dataclass
class ApiKeyRoute:
  api_key_id: typing.Union[int, float]
  method: str
  path: str

  
  api_key: ApiKey


# ---

@dataclass
class Attachment:
  description: str
  download: str
  filename: str
  id: typing.Union[int, float]
  internal: bool
  mimetype: str
  request_id: typing.Union[int, float]
  size: typing.Union[int, float]

  
  request: Request


# ---

@dataclass
class BarcodeScratch:
  comment: str
  data: str
  date: str
  form: str
  id: typing.Union[int, float]
  username: str

  
  form_ref: Form
  user_ref: Scientist


# ---

@dataclass
class Changeset:
  date: str
  deleted: bool
  form: str
  id: typing.Union[int, float]
  last_change: str
  last_change_username: str
  measurement_data_id: typing.Union[int, float]
  username: str

  
  data_entries: list[DataEntry]
  form_ref: Form
  last_change_user_ref: Scientist
  user_ref: Scientist


# ---

@dataclass
class ControlSample:
  control_sample_id: typing.Union[int, float]
  sample_id: typing.Union[int, float]

  
  control_sample: Sample
  sample: Sample


# ---

@dataclass
class DataEntry:
  changeset_id: typing.Union[int, float]
  comment_text: str
  control: str
  deleted: bool
  entry_date: str
  flag: str
  form: str
  id: typing.Union[int, float]
  last_change: str
  last_change_username: str
  multi_id: typing.Union[int, float]
  notified: bool
  obj_id: typing.Union[int, float]
  obj_type: str
  request_id: typing.Union[int, float]
  resolved: bool
  row_number: typing.Union[int, float]
  username: str
  values: dict

  
  changeset: Changeset
  form_ref: Form
  last_change_user_ref: Scientist
  multi: Multiplex
  multiplex: Multiplex
  request: Request
  run_unit: RunUnit
  sample: Sample
  user_ref: Scientist


# ---

@dataclass
class Fastqc:
  barcode: str
  basecalls: str
  basic_result: str
  count_q30: typing.Any
  count_q33: typing.Any
  count_q35: typing.Any
  count_q37: typing.Any
  date: str
  duplication_levels: str
  duplication_percent: typing.Any
  duplication_result: str
  flowcell: str
  id: typing.Union[int, float]
  lane: typing.Union[int, float]
  over_illumina: typing.Any
  over_no_hit: typing.Any
  over_other: typing.Any
  over_result: str
  path: str
  read: str
  result_check_id: typing.Union[int, float]
  run_id: typing.Union[int, float]
  total_count: typing.Any

  
  result_check: ResultCheck


# ---

@dataclass
class Form:
  config: FormConfig
  fields: list[DataEntryField]
  id: typing.Union[int, float]
  name: str
  ordering: typing.Union[int, float]
  platform: str

  
  changesets: list[Changeset]
  data_entries: list[DataEntry]
  platform_ref: Platform


# ---

@dataclass
class Group:
  active: bool
  announce_subscribed: bool
  billing_address: str
  billing_atu: str
  billing_institute: str
  billing_type: str
  created: str
  email: str
  id: typing.Union[int, float]
  imp_storage: bool
  institute: str
  last_change: str
  miseq_selfservice: bool
  name: str
  obj_id: typing.Union[int, float]
  obj_type: str

  
  billing_type_ref: PricingCategory
  projects: list[Project]
  requests: list[Request]
  scientists: list[Scientist]


# ---

@dataclass
class IlluminaRun:
  cbot: str
  clustering_kit_lot: str
  clustering_kit_version: str
  clusterkit_box_1: str
  clusterkit_box_2: str
  comments: str
  description: str
  draft: bool
  group: typing.Any
  group_id: typing.Union[int, float]
  id: typing.Union[int, float]
  index_length: typing.Union[int, float]
  last_change: str
  machine: str
  name: str
  obj_type: str
  platform: str
  preparation_date: str
  read1_length: typing.Union[int, float]
  read2_length: typing.Union[int, float]
  readmode: Readmode
  readmode_id: typing.Union[int, float]
  report_url: str
  run_folder: str
  run_id: typing.Union[int, float]
  sbs_minus_20: str
  sbs_plus_4: str
  scientist: typing.Any
  scientist_id: typing.Union[int, float]
  secondary_index_length: typing.Union[int, float]
  selfservice: bool
  sequencing_date: str
  status: str
  username: str
  vendor_id: str
  xp_enabled: bool

  
  inventory_changes: list[InventoryChange]
  lanes: list[Lane]
  run: Run


# ---

@dataclass
class InventoryChange:
  change: typing.Union[int, float]
  comment: str
  date: str
  draft: bool
  id: typing.Union[int, float]
  item: str
  run_id: typing.Union[int, float]
  username: str

  
  inventory_item: InventoryItem
  run: Run
  user_ref: Scientist


# ---

@dataclass
class InventoryItem:
  active: bool
  cat: str
  count: typing.Union[int, float]
  description: str
  item: str
  link: str
  pricing_item_name: str
  threshold: typing.Union[int, float]
  type: str

  
  inventory_changes: list[InventoryChange]
  pricing_item: PricingItem


# ---

@dataclass
class ItemCategoryPrice:
  category: str
  item_id: typing.Union[int, float]
  price: typing.Union[int, float]

  
  category_ref: PricingCategory
  item: PriceListItem


# ---

@dataclass
class Lane:
  comments: str
  conc: typing.Any
  discount: typing.Union[int, float]
  group: typing.Any
  invoice_status: str
  is_saved: bool
  lane_checks: list[ResultCheck]
  last_change: str
  needs_demultiplexing: bool
  num: str
  phix: typing.Union[int, float]
  primer: str
  run_id: typing.Union[int, float]
  sample_fields: SampleFields
  sampnum: typing.Union[int, float]
  scientist: typing.Any
  status: str
  unassigned_checks: list[ResultCheck]
  unit_id: typing.Union[int, float]
  username: str

  
  flowcell: IlluminaRun
  primer_ref: Primer
  run_ref: Run
  run_unit: RunUnit
  sequenced_samples: list[SequencedSample]


# ---

@dataclass
class Machine:
  active: bool
  celltypes: list[Celltype]
  description: str
  model: str
  name: str
  platform: str
  readmodes: list[Readmode]
  run_folder: str
  vendor_id: str

  
  platform_ref: Platform


# ---

@dataclass
class Multiplex:
  _imp_storage: bool
  adaptor_type: str
  description: str
  group: typing.Any
  group_id: typing.Union[int, float]
  id: typing.Union[int, float]
  lab_count: typing.Union[int, float]
  lab_steps: list[LabStep]
  measurement_count: typing.Union[int, float]
  notes_count: typing.Union[int, float]
  obj_id: typing.Union[int, float]
  obj_type: str
  platform: str
  pooled: bool
  received: str
  request_count: typing.Union[int, float]
  sampcount: typing.Union[int, float]
  sample_fields: SampleFields
  scientist: typing.Any
  scientist_id: typing.Union[int, float]
  sequencing_count: typing.Union[int, float]

  
  adaptor_type_ref: AdaptorType
  data_entries: list[DataEntry]
  group_ref: Group
  multi_data_entries: list[DataEntry]
  multiplex_samples: list[MultiplexSample]
  notes: list[Note]
  platform_ref: Platform
  preparation_type_ref: PreparationType
  request_lanes: list[RequestLane]
  scientist_ref: Scientist
  versions: list[ObjectVersion]


# ---

@dataclass
class MultiplexSample:
  multi_id: typing.Union[int, float]
  ratio: typing.Union[int, float]
  sample_id: typing.Union[int, float]

  
  multi: Multiplex
  sample: Sample
  versions: list[ObjectVersion]


# ---

@dataclass
class Nanostat:
  active_channels: typing.Union[int, float]
  barcode: str
  basecalls: str
  basepairs: typing.Any
  bc_best_filter: str
  bc_best_unique_rate: typing.Any
  bc_hit_rate: typing.Any
  created: str
  flowcell_unique_id: str
  id: typing.Union[int, float]
  last_change: str
  mean_gc: typing.Any
  mean_length: typing.Any
  mean_qual: typing.Any
  median_length: typing.Any
  median_qual: typing.Any
  n50_length: typing.Any
  path: str
  q10_basepairs: typing.Any
  q10_reads: typing.Any
  q12_basepairs: typing.Any
  q12_reads: typing.Any
  q15_basepairs: typing.Any
  q15_reads: typing.Any
  q5_basepairs: typing.Any
  q5_reads: typing.Any
  q7_basepairs: typing.Any
  q7_reads: typing.Any
  reads: typing.Any
  result_check_id: typing.Union[int, float]
  run_id: typing.Union[int, float]
  run_unique_id: str
  unit_id: typing.Union[int, float]

  
  ont_flowcell_run: OntFlowcellRun
  ont_run: OntRun
  result_check: ResultCheck
  run: Run
  run_unit: RunUnit


# ---

@dataclass
class Note:
  comment_date: str
  comment_text: str
  flag: str
  id: typing.Union[int, float]
  last_change: str
  last_change_username: str
  note_type: str
  notified: bool
  obj_id: typing.Union[int, float]
  obj_type: str
  resolved: bool
  username: str

  
  last_change_user_ref: Scientist
  multiplex: Multiplex
  request: Request
  run: Run
  sample: Sample
  scientist: Scientist
  user_ref: Scientist


# ---

@dataclass
class Notification:
  additional: str
  attach_reqsheet: bool
  body: str
  cc_recipients: str
  date: str
  done: bool
  grouped_with: typing.Union[int, float]
  id: typing.Union[int, float]
  message_type: str
  message_type_id: typing.Union[int, float]
  obj_id: str
  obj_type: str
  parameters: dict
  state: str
  subject: str

  
  grouped_notifications: list[Notification]
  grouped_with_ref: Notification
  multiplex: Multiplex
  request: Request
  request_lane: RequestLane
  run: Run
  run_unit: RunUnit
  sample: Sample
  user: Scientist


# ---

@dataclass
class ObjectVersion:
  date: str
  id: typing.Union[int, float]
  obj_data: dict
  obj_id: typing.Union[int, float]
  obj_type: str
  op: str
  username: str
  version: typing.Union[int, float]

  
  scientist_ref: Scientist


# ---

@dataclass
class OntFlowcellRun:
  basecalled: str
  basecaller: str
  basecalls: str
  comments: str
  conc: typing.Any
  copied: str
  datafiles_created: str
  datafiles_hash: str
  datafiles_id: typing.Union[int, float]
  datafiles_link: str
  datafiles_path: str
  datafiles_size: typing.Any
  datafiles_url: str
  demultiplexed: str
  discount: typing.Union[int, float]
  experiment_name: str
  fastq_path: str
  group: typing.Any
  invoice_status: str
  is_saved: bool
  kit: str
  lane_checks: list[ResultCheck]
  last_change: str
  loading: typing.Union[int, float]
  multiplexing: bool
  needs_demultiplexing: bool
  output_path: str
  processed: str
  report_url: str
  run_id: typing.Union[int, float]
  run_length: typing.Union[int, float]
  sample_fields: SampleFields
  sample_type: str
  sampnum: typing.Union[int, float]
  scientist: typing.Any
  software_version: str
  start_time: str
  status: str
  unassigned_checks: list[ResultCheck]
  unique_id: str
  unit_id: typing.Union[int, float]
  username: str

  
  flowcell: OntRun
  run_ref: Run
  run_unit: RunUnit
  sequenced_samples: list[SequencedSample]


# ---

@dataclass
class OntRun:
  comments: str
  description: str
  device_id: str
  draft: bool
  flowcell_type: str
  group: typing.Any
  group_id: typing.Union[int, float]
  id: typing.Union[int, float]
  last_change: str
  machine: str
  mux_scan_pores: typing.Union[int, float]
  name: str
  obj_type: str
  platform: str
  preparation_date: str
  qc_pores: typing.Union[int, float]
  readmode: Readmode
  readmode_id: typing.Union[int, float]
  report_url: str
  run_folder: str
  run_id: typing.Union[int, float]
  scientist: typing.Any
  scientist_id: typing.Union[int, float]
  selfservice: bool
  sequencing_date: str
  status: str
  unique_id: str
  username: str
  vendor_id: str

  
  ont_flowcell_runs: list[OntFlowcellRun]
  run: Run


# ---

@dataclass
class PacbioRun:
  comments: str
  description: str
  draft: bool
  group: typing.Any
  group_id: typing.Union[int, float]
  id: typing.Union[int, float]
  instrument_sw_version: str
  last_change: str
  machine: str
  name: str
  obj_type: str
  platform: str
  preparation_date: str
  primary_analysis_version: str
  readmode: Readmode
  readmode_id: typing.Union[int, float]
  report_url: str
  run_folder: str
  run_id: typing.Union[int, float]
  scientist: typing.Any
  scientist_id: typing.Union[int, float]
  selfservice: bool
  sequencing_date: str
  status: str
  unique_id: str
  username: str
  vendor_id: str

  
  run: Run
  smrtcells: list[SmrtCell]
  subreadstats: list[Subreadstat]


# ---

@dataclass
class Platform:
  analysis_pipelines: list[AnalysisPipeline]
  description: str
  name: str
  readmodes: list[Readmode]
  vendor: str

  
  adaptor_types: list[AdaptorType]
  forms: list[Form]
  machines: list[Machine]
  preparation_types: list[PreparationType]
  primers: list[Primer]
  requests: list[Request]
  samples: list[Sample]


# ---

@dataclass
class PreparationKit:
  adaptor_type: str
  additional_qc_item_name: str
  available: bool
  description: str
  kit: str
  min_samples: typing.Union[int, float]
  multiplexing: bool
  needs_review: bool
  own_risk: bool
  plate_submission: typing.Union[int, float]
  platform: str
  prep_per_sample: bool
  prep_volume: typing.Any
  preparation_type: str
  pricing_item_name: str
  qc_per_sample: bool
  samples_per_plate: typing.Union[int, float]
  strand_specific: bool

  
  adaptor_type_ref: AdaptorType
  additional_qc_item: PricingItem
  platform_ref: Platform
  preparation_type_ref: PreparationType
  pricing_item: PricingItem
  samples: list[Sample]


# ---

@dataclass
class PreparationStep:
  form: str
  ordering: typing.Union[int, float]
  platform: str
  preparation_type: str

  
  form_ref: Form
  preparation_type_ref: PreparationType


# ---

@dataclass
class PreparationType:
  description: str
  name: str
  platform: str
  watchdog_time: typing.Union[int, float]

  
  platform_ref: Platform
  preparation_kits: list[PreparationKit]
  preparation_steps: list[PreparationStep]
  samples: list[Sample]


# ---

@dataclass
class PriceList:
  description: str
  id: typing.Union[int, float]
  valid_from: str

  
  items: list[PriceListItem]


# ---

@dataclass
class PriceListItem:
  category: str
  code: str
  count: typing.Union[int, float]
  description: typing.Any
  id: typing.Union[int, float]
  item: str
  ordering: typing.Union[int, float]
  price: typing.Union[int, float]
  price_list_id: typing.Union[int, float]
  show: bool
  sort_order: typing.Any
  total: typing.Union[int, float]

  
  category_prices: list[ItemCategoryPrice]
  price_list: PriceList
  pricing_item: PricingItem


# ---

@dataclass
class PricingCategory:
  code: str
  description: str
  name: str

  
  category_prices: list[ItemCategoryPrice]
  groups: list[Group]


# ---

@dataclass
class PricingItem:
  base_item: str
  count_bracket_max: typing.Union[int, float]
  count_bracket_min: typing.Union[int, float]
  description: str
  foreign_billing: bool
  heading: str
  item: str
  unit: str

  
  base_item_ref: PricingItem
  inventory_items: list[InventoryItem]
  preparation_kits: list[PreparationKit]
  price_list_items: list[PriceListItem]
  staggered_items: list[PricingItem]


# ---

@dataclass
class Primer:
  available: bool
  conc: typing.Union[int, float]
  create_date: str
  description: str
  group: typing.Any
  group_id: typing.Union[int, float]
  id: typing.Union[int, float]
  name: str
  number: typing.Union[int, float]
  platform: str
  read: str
  sequence: str
  volume: typing.Union[int, float]

  
  group_ref: Group
  platform_ref: Platform
  samples: list[Sample]


# ---

@dataclass
class Project:
  completed: str
  cost_assignment: str
  created: str
  description: str
  group: typing.Any
  group_id: typing.Union[int, float]
  history: list[TimelineEvent]
  id: typing.Union[int, float]
  last_change: str
  last_request: str
  name: str
  obj_id: typing.Union[int, float]
  obj_type: str
  request_count: typing.Union[int, float]
  sample_count: typing.Union[int, float]
  scientist: typing.Any
  scientist_id: typing.Union[int, float]
  sequencing_count: typing.Union[int, float]
  status: str

  
  data_entries: list[DataEntry]
  group_ref: Group
  notes: list[Note]
  requests: list[Request]
  scientist_ref: Scientist


# ---

@dataclass
class Report:
  created: str
  id: typing.Union[int, float]
  json_data: dict
  raw_data: dict
  report_html: str
  report_path: str
  title: str
  type: str

  
  

# ---

@dataclass
class Request:
  _imp_storage: bool
  accepted: str
  attachment_count: typing.Union[int, float]
  comments: str
  completed: str
  cost_assignment: str
  custom_readlength: typing.Union[int, float]
  demultiplexing: bool
  duration: typing.Union[int, float]
  external_analysis: str
  group: typing.Any
  group_id: typing.Union[int, float]
  history: list[TimelineEvent]
  id: typing.Union[int, float]
  is_control: bool
  lab_count: typing.Union[int, float]
  lab_steps: list[LabStep]
  last_change: str
  long_seqtype: typing.Any
  measurement_count: typing.Union[int, float]
  needs_review: bool
  notes_count: typing.Union[int, float]
  obj_id: typing.Union[int, float]
  obj_type: str
  parent_request_id: typing.Union[int, float]
  plate_submission_required: bool
  platform: str
  priority: typing.Union[int, float]
  project_id: typing.Union[int, float]
  readmode: Readmode
  readmode_id: typing.Union[int, float]
  reviewed: bool
  sample_fields: SampleFields
  sampnum: typing.Union[int, float]
  scientist: typing.Any
  scientist_id: typing.Union[int, float]
  selfservice: bool
  sequencing_count: typing.Union[int, float]
  short_seqtype: typing.Any
  status: str
  submitted: str
  xp_workflow_enabled: bool

  
  attachments: list[Attachment]
  cost_estimate_items: list[RequestCostEstimateItem]
  data_entries: list[DataEntry]
  group_ref: Group
  invoice_items: list[RequestInvoiceItem]
  notes: list[Note]
  parent_request_ref: Request
  platform_ref: Platform
  project: Project
  request_lanes: list[RequestLane]
  scientist_ref: Scientist
  shadow_requests: list[Request]
  versions: list[ObjectVersion]


# ---

@dataclass
class RequestCostEstimateItem:
  category: str
  code: str
  count: typing.Union[int, float]
  description: str
  discount: typing.Union[int, float]
  heading: str
  id: typing.Union[int, float]
  item_id: typing.Union[int, float]
  manual: bool
  price: typing.Union[int, float]
  request_id: typing.Union[int, float]
  sort_order: str
  total: typing.Union[int, float]

  
  item: PriceListItem
  request: Request


# ---

@dataclass
class RequestDraft:
  create_date: str
  group: typing.Any
  group_id: typing.Union[int, float]
  id: typing.Union[int, float]
  last_change: str
  name: str
  request_data: Request
  scientist: typing.Any
  scientist_id: typing.Union[int, float]
  valid: bool

  
  group_ref: Group
  scientist_ref: Scientist


# ---

@dataclass
class RequestInvoiceItem:
  category: str
  code: str
  count: typing.Union[int, float]
  description: str
  discount: typing.Union[int, float]
  heading: str
  id: typing.Union[int, float]
  item_id: typing.Union[int, float]
  manual: bool
  price: typing.Union[int, float]
  reason: str
  request_id: typing.Union[int, float]
  sent_date: str
  sort_order: str
  status: str
  total: typing.Union[int, float]

  
  item: PriceListItem
  request: Request


# ---

@dataclass
class RequestLane:
  control_for: list[ControlSample]
  custom_primer: typing.Any
  days_to_dismiss: typing.Union[int, float]
  days_to_warn: typing.Union[int, float]
  duration: typing.Union[int, float]
  extra_phix: str
  id: typing.Union[int, float]
  is_control: bool
  lab_steps: list[LabStep]
  last_change: str
  low_complexity: bool
  multi_id: typing.Union[int, float]
  num: typing.Union[int, float]
  onhold_notified: str
  onhold_started: str
  parent_lane: RequestLane
  pooled: bool
  pooling_strategy: typing.Any
  request_id: typing.Union[int, float]
  required_reads: typing.Union[int, float]
  sample_fields: SampleFields
  sampnum: typing.Union[int, float]
  sequencing_runs: list[RunUnit]
  shadow_lanes: list[RequestLane]
  share_required_ratio: typing.Any
  share_status: typing.Any
  show_id: typing.Any
  show_obj_id: str
  status: str
  super_multi_id: typing.Union[int, float]
  time_to_watchdog: typing.Union[int, float]
  watchdog_notified: str

  
  multi: Multiplex
  request: Request
  requests_samples: list[RequestsSample]
  super_multi: SuperMulti
  versions: list[ObjectVersion]


# ---

@dataclass
class RequestsSample:
  analysis_pipeline: str
  duration: typing.Union[int, float]
  id: typing.Union[int, float]
  lane: typing.Union[int, float]
  last_change: str
  obj_id: typing.Union[int, float]
  obj_type: str
  onhold_started: str
  ratio: typing.Union[int, float]
  request_id: typing.Union[int, float]
  required_ratio: typing.Any
  required_reads: typing.Union[int, float]
  resubmission: bool
  sample_id: typing.Union[int, float]
  status: str
  time_to_watchdog: typing.Union[int, float]

  
  _request: Request
  request_lane: RequestLane
  sample: Sample
  sequenced_samples: list[SequencedSample]
  versions: list[ObjectVersion]


# ---

@dataclass
class ResultCheck:
  actual_ratio: typing.Any
  actual_reads: typing.Any
  barcode: str
  basecalls: str
  checked_by_user: typing.Union[int, float]
  checked_on: str
  checking_by_date: str
  checking_by_user: typing.Union[int, float]
  comment: str
  deleted_on: str
  downloaded: bool
  file_status: str
  id: typing.Union[int, float]
  md5: str
  nanostat: Nanostat
  notified_on: str
  reqsamp_id: typing.Union[int, float]
  required_bloom_filter: typing.Any
  required_ratio: typing.Any
  required_reads: typing.Any
  result: str
  run_id: typing.Union[int, float]
  samplestat: Samplestat
  subreadstat: Subreadstat
  sync_time: str
  unit_id: typing.Union[int, float]
  vendor_id: str

  
  fastqcs: list[Fastqc]
  nanostats: list[Nanostat]
  run_unit: RunUnit
  samplestats: list[Samplestat]
  sequenced_sample: SequencedSample
  subreadstats: list[Subreadstat]


# ---

@dataclass
class Run:
  comments: str
  description: str
  draft: bool
  group: typing.Any
  group_id: typing.Union[int, float]
  id: typing.Union[int, float]
  last_change: str
  machine: str
  name: str
  obj_type: str
  platform: str
  preparation_date: str
  readmode: Readmode
  readmode_id: typing.Union[int, float]
  report_url: str
  run_folder: str
  scientist: typing.Any
  scientist_id: typing.Union[int, float]
  selfservice: bool
  sequencing_date: str
  status: str
  username: str
  vendor_id: str

  
  group_ref: Group
  illumina_run_ref: IlluminaRun
  inventory_changes: list[InventoryChange]
  machine_ref: Machine
  ont_run_ref: OntRun
  pacbio_run_ref: PacbioRun
  platform_ref: Platform
  run_units: list[RunUnit]
  scientist_ref: Scientist
  user_ref: Scientist


# ---

@dataclass
class RunUnit:
  comments: str
  conc: typing.Any
  discount: typing.Union[int, float]
  group: typing.Any
  invoice_status: str
  is_saved: bool
  lane_checks: list[ResultCheck]
  last_change: str
  needs_demultiplexing: bool
  run_id: typing.Union[int, float]
  sample_fields: SampleFields
  sampnum: typing.Union[int, float]
  scientist: typing.Any
  status: str
  unassigned_checks: list[ResultCheck]
  unit_id: typing.Union[int, float]
  username: str

  
  data_entries: list[DataEntry]
  lane: Lane
  ont_flowcell_run: OntFlowcellRun
  result_checks: list[ResultCheck]
  run: Run
  sequenced_samples: list[SequencedSample]
  smrtcell: SmrtCell
  user_ref: Scientist


# ---

@dataclass
class Sample:
  _imp_storage: bool
  adaptor_inline_number: typing.Union[int, float]
  adaptor_inline_tag: str
  adaptor_number: typing.Union[int, float]
  adaptor_secondary_number: typing.Union[int, float]
  adaptor_secondary_tag: str
  adaptor_tag: str
  adaptor_type: str
  antibody: str
  celltype: str
  comments: str
  conc: typing.Any
  control_for_count: typing.Union[int, float]
  control_type: str
  cutout_size: str
  cutout_size_max: typing.Any
  cutout_size_min: typing.Any
  description: str
  exptype: str
  external_link: str
  fragment_size: str
  fragmented: bool
  genotype: str
  group: typing.Any
  group_id: typing.Union[int, float]
  history: list[TimelineEvent]
  id: typing.Union[int, float]
  is_control: typing.Any
  lab_count: typing.Union[int, float]
  lab_steps: list[LabStep]
  last_change: str
  measurement_count: typing.Union[int, float]
  notes_count: typing.Union[int, float]
  obj_id: typing.Union[int, float]
  obj_type: str
  organism: str
  own_risk: bool
  platform: str
  preparation_kit: str
  preparation_type: str
  primer: str
  ready: str
  received: str
  request_count: typing.Union[int, float]
  scientist: typing.Any
  scientist_id: typing.Union[int, float]
  sequencing_count: typing.Union[int, float]
  status: str
  stranded: bool
  tissue_type: str
  treatment: str
  user_preparation_kit: str
  volume: typing.Any

  
  adaptor_type_ref: AdaptorType
  control_for: list[ControlSample]
  control_samples: list[ControlSample]
  controls: list[Sample]
  data_entries: list[DataEntry]
  group_ref: Group
  inline_adaptor: Tag
  multiplex_samples: list[MultiplexSample]
  notes: list[Note]
  platform_ref: Platform
  pool_tags: list[SampleTag]
  preparation_kit_ref: PreparationKit
  preparation_type_ref: PreparationType
  primary_adaptor: Tag
  primer_ref: Primer
  requests_samples: list[RequestsSample]
  scientist_ref: Scientist
  secondary_adaptor: Tag
  trash_notes: list[Note]
  versions: list[ObjectVersion]


# ---

@dataclass
class SampleList:
  created: str
  id: typing.Union[int, float]
  ids: dict
  last_change: str
  last_change_username: str
  title: str
  username: str

  
  last_change_user_ref: Scientist
  user_ref: Scientist


# ---

@dataclass
class SampleTag:
  adaptor_inline_number: typing.Union[int, float]
  adaptor_number: typing.Union[int, float]
  adaptor_secondary_number: typing.Union[int, float]
  adaptor_secondary_tag: str
  adaptor_tag: str
  adaptor_type: str
  description: str
  id: typing.Union[int, float]
  ratio: typing.Union[int, float]
  sample_id: typing.Union[int, float]

  
  inline_adaptor: Tag
  primary_adaptor: Tag
  sample: Sample
  secondary_adaptor: Tag


# ---

@dataclass
class Samplestat:
  alignment_rate: typing.Any
  barcode: str
  basecalls: str
  bc_best_filter: str
  bc_best_unique_rate: typing.Any
  bc_hit_rate: typing.Any
  date: str
  file: str
  flowcell: str
  id: typing.Union[int, float]
  lane: typing.Union[int, float]
  library_diversity: typing.Any
  library_saturation: typing.Any
  path: str
  result_check_id: typing.Union[int, float]
  run_id: typing.Union[int, float]
  taxo_guess: str

  
  result_check: ResultCheck


# ---

@dataclass
class Scientist:
  active: bool
  announce_subscribed: bool
  created: str
  delivery: str
  email: str
  firstname: str
  id: typing.Union[int, float]
  imp_galaxy_username: str
  last_change: str
  last_login: str
  lastname: str
  login_failed: typing.Union[int, float]
  login_ok: typing.Union[int, float]
  obj_id: typing.Union[int, float]
  obj_type: str
  previous_login: str
  primary_group_id: typing.Union[int, float]
  reviewed: bool
  username: str

  
  api_keys: list[ApiKey]
  multiplexes: list[Multiplex]
  notes: list[Note]
  primary_group: Group
  projects: list[Project]
  request_drafts: list[RequestDraft]
  requests: list[Request]
  samples: list[Sample]


# ---

@dataclass
class SequencedSample:
  comments: str
  conc: typing.Union[int, float]
  id: typing.Union[int, float]
  is_repetition: bool
  is_spikein: bool
  last_change: str
  multi_id: typing.Union[int, float]
  reqsamp_id: typing.Union[int, float]
  run_id: typing.Union[int, float]
  status: str
  unit_id: typing.Union[int, float]

  
  multi: Multiplex
  request_sample: RequestsSample
  result_checks: list[ResultCheck]
  run: Run
  run_unit: RunUnit


# ---

@dataclass
class SmrtCell:
  binding_kit: str
  cell_pac: str
  comments: str
  conc: typing.Any
  concentration: typing.Union[int, float]
  context: str
  control_kit: str
  datafiles_created: str
  datafiles_hash: str
  datafiles_id: typing.Union[int, float]
  datafiles_link: str
  datafiles_path: str
  datafiles_size: typing.Any
  datafiles_url: str
  demultiplexed: str
  discount: typing.Union[int, float]
  extend_first: bool
  extension_time: typing.Union[int, float]
  group: typing.Any
  immobilization_time: typing.Union[int, float]
  insert_size: typing.Union[int, float]
  invoice_status: str
  is_saved: bool
  lane_checks: list[ResultCheck]
  last_change: str
  magbead_loading: bool
  movie_time: typing.Union[int, float]
  name: str
  needs_demultiplexing: bool
  output_folder: str
  processed: str
  report_url: str
  run_id: typing.Union[int, float]
  sample_fields: SampleFields
  sampnum: typing.Union[int, float]
  scientist: typing.Any
  sequencing_kit: str
  status: str
  subreads: str
  template_prep_kit: str
  unassigned_checks: list[ResultCheck]
  unique_id: str
  unit_id: typing.Union[int, float]
  username: str
  well: str

  
  pacbio_run: PacbioRun
  run_ref: Run
  run_unit: RunUnit
  sequenced_samples: list[SequencedSample]


# ---

@dataclass
class Subreadstat:
  barcode: str
  basepairs: typing.Any
  bc1: str
  bc2: str
  bc_best_filter: str
  bc_best_unique_rate: typing.Any
  bc_hit_rate: typing.Any
  bq_hqreads: typing.Any
  bq_mode: typing.Any
  created: str
  id: typing.Union[int, float]
  last_change: str
  loading_p0: typing.Any
  loading_p1: typing.Any
  loading_p2: typing.Any
  mean_gc: typing.Any
  mean_length: typing.Any
  median_length: typing.Any
  n50_length: typing.Any
  path: str
  reads: typing.Any
  result_check_id: typing.Union[int, float]
  run_id: typing.Union[int, float]
  run_unique_id: str
  smrtcell_unique_id: str
  unit_id: typing.Union[int, float]

  
  pacbio_run: PacbioRun
  result_check: ResultCheck
  run: Run
  run_unit: RunUnit
  smrtcell: SmrtCell


# ---

@dataclass
class SuperMulti:
  description: str
  id: typing.Union[int, float]

  
  request_lanes: list[RequestLane]


# ---

@dataclass
class Tag:
  adaptor_type: str
  available: bool
  name: str
  num: typing.Union[int, float]
  pos: str
  seq: str
  unique_combination: typing.Union[int, float]

  
  adaptor_type_ref: AdaptorType
  samples_adaptor_type_adaptor_numbers: list[Sample]
  samples_adaptor_type_adaptor_secondary_numbers: list[Sample]


# ---

@dataclass
class LabStep:
  fails: list[LabStep]
  flag: str
  form: str
  have: typing.Union[int, float]
  obj_id: typing.Union[int, float]
  obj_type: str
  ordering: typing.Union[int, float]
  should: typing.Union[int, float]
  warnings: list[LabStep]

  


# ---

@dataclass
class SampleFields:
  adaptor_type: dict
  antibody: dict
  celltype: dict
  cutout_size: dict
  exptype: dict
  fragment_size: dict
  genotype: dict
  organism: dict
  own_risk: dict
  preparation_kit: dict
  preparation_type: dict
  primer: dict
  ready: dict
  received: dict
  status: dict
  stranded: dict
  tissue_type: dict
  treatment: dict

  


# ---

@dataclass
class Celltype:
  available: bool
  custom_readlengths: bool
  description: str
  flowcell_count: typing.Union[int, float]
  lane_count: typing.Union[int, float]
  name: str
  read_minimum: typing.Union[int, float]
  read_typical: str
  selfservice: bool

  


# ---

@dataclass
class EstimateRequest:
  accepted: str
  completed: str
  cost_assignment: str
  group: str
  id: typing.Union[int, float]
  long_seqtype: str
  pricing_category: str
  project_name: str
  scientist: str
  status: str
  submitted: str

  


# ---

@dataclass
class CostEstimate:
  category_totals: dict
  items: list[RequestCostEstimateItem]
  price_list: PriceList
  request: EstimateRequest
  total: typing.Union[int, float]

  


# ---

@dataclass
class Invoice:
  category_totals: dict
  items: list[RequestInvoiceItem]
  price_list: PriceList
  request: EstimateRequest
  status: str
  total: typing.Union[int, float]

  


# ---

@dataclass
class VirtualBill:
  category_totals: dict
  invoices: list[Invoice]
  total: typing.Union[int, float]

  


# ---

@dataclass
class FormConfig:
  control_samples: bool
  expand_multis: bool
  filters: RequestLaneFilters

  


# ---

@dataclass
class TimelineEvent:
  date: str
  description: str
  event_type: str
  ids: str
  newstatus: str
  obj_type: str
  oldstatus: str

  


# ---

@dataclass
class SequencedBarcode:
  adaptor_number: typing.Union[int, float]
  adaptor_secondary_number: typing.Union[int, float]
  adaptor_secondary_tag: str
  adaptor_secondary_tagname: str
  adaptor_tag: str
  adaptor_tagname: str
  adaptor_type: str
  is_pool: bool
  is_spikein: bool
  multi_id: typing.Union[int, float]
  pool_ratio: typing.Union[int, float]
  pooled_by_user: bool
  request_id: typing.Union[int, float]
  requested_ratio: typing.Union[int, float]
  required_ratio: typing.Union[int, float]
  required_reads: typing.Union[int, float]
  sample_id: typing.Union[int, float]
  share_status: str
  unit_id: typing.Union[int, float]
  vendor_id: str

  


# ---

@dataclass
class ZammadTicket:
  created_at: str
  customer: str
  group: str
  id: typing.Union[int, float]
  multi: str
  note: str
  number: typing.Union[int, float]
  organization: str
  owner: str
  request: str
  sample: str
  state: str
  title: str
  updated_at: str
  url: str

  


# ---

@dataclass
class AnalysisPipeline:
  available: bool
  description: str
  external: bool
  id: typing.Union[int, float]
  long_description: str
  name: str
  platform: str
  pricing_item_name: str

  


# ---

@dataclass
class DataEntryField:
  id: typing.Union[int, float]
  name: str
  type: typing.Any

  


# ---

@dataclass
class DataEntryFlag:
  id: typing.Union[int, float]
  name: str
  severity: typing.Union[int, float]

  


# ---

@dataclass
class Exptype:
  description: str
  exptype: str

  


# ---

@dataclass
class MessageType:
  admin_cc: bool
  admin_message: bool
  attach_report: bool
  attach_reqsheet: bool
  configurable: bool
  deferred: bool
  groupable: bool
  id: typing.Union[int, float]
  name: str
  sensitive: bool
  template: str

  


# ---

@dataclass
class NoteFlag:
  id: typing.Union[int, float]
  name: str
  severity: typing.Union[int, float]

  


# ---

@dataclass
class ObjType:
  db_table: str
  id: typing.Union[int, float]
  name: str

  


# ---

@dataclass
class Organism:
  bloom_filter_name: str
  common_name: str
  sci_name: str
  taxonomy_id: typing.Union[int, float]

  


# ---

@dataclass
class Readmode:
  asym: bool
  available: bool
  celltype: str
  celltype_description: str
  custom_readlengths: bool
  duration: typing.Union[int, float]
  flowcell_type: str
  id: typing.Union[int, float]
  lane_count: typing.Union[int, float]
  long_seqtype: str
  movielength: typing.Union[int, float]
  ontcell_type: str
  paired: bool
  platform: str
  prep_duration: typing.Union[int, float]
  pricing_item_name: str
  rapid_mode: bool
  read_minimum: typing.Union[int, float]
  read_typical: str
  readlen: typing.Union[int, float]
  selfservice: bool
  sharable: bool
  short_seqtype: str
  smrtcell_type: str

  


# ---

@dataclass
class Status:
  description: str
  obj_type: str
  ord: typing.Union[int, float]
  status: str

  


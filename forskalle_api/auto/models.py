from __future__ import annotations
from dataclasses import dataclass, field
import typing
from .queryparams import RequestLaneFilters
from datetime import datetime


def plainToAdaptorType(json: dict) -> AdaptorType:
  obj = AdaptorType()
  obj.available = bool(json.get('available'))
  obj.category = json.get('category')
  obj.description = json.get('description')
  obj.group = json.get('group')
  obj.group_id = json.get('group_id')
  obj.multiplexing = bool(json.get('multiplexing'))
  obj.name = json.get('name')
  obj.platform = json.get('platform')
  obj.pos = json.get('pos')
  obj.sequence = json.get('sequence')
  obj.group_ref = plainToGroup(json['group_ref']) if json.get('group_ref') else None
  obj.multiplexes = [ plainToMultiplex(o) for o in json['multiplexes'] ] if json.get('multiplexes') else []
  obj.platform_ref = plainToPlatform(json['platform_ref']) if json.get('platform_ref') else None
  obj.samples = [ plainToSample(o) for o in json['samples'] ] if json.get('samples') else []
  obj.tags = [ plainToTag(o) for o in json['tags'] ] if json.get('tags') else []

  return obj

def serializeAdaptorType(obj: AdaptorType) -> dict:
  json = {}
  json['available'] = obj.available
  json['category'] = obj.category
  json['description'] = obj.description
  json['group'] = obj.group
  json['group_id'] = obj.group_id
  json['multiplexing'] = obj.multiplexing
  json['name'] = obj.name
  json['platform'] = obj.platform
  json['pos'] = obj.pos
  json['sequence'] = obj.sequence
  json['group_ref'] = serializeGroup(obj.group_ref) if obj.group_ref is not None else None
  if obj.multiplexes is not None:
    json['multiplexes'] = [ serializeMultiplex(o) for o in obj.multiplexes ]
  json['platform_ref'] = serializePlatform(obj.platform_ref) if obj.platform_ref is not None else None
  if obj.samples is not None:
    json['samples'] = [ serializeSample(o) for o in obj.samples ]
  if obj.tags is not None:
    json['tags'] = [ serializeTag(o) for o in obj.tags ]

  return json


@dataclass
class AdaptorType:
  available: typing.Optional[bool] = None
  category: typing.Optional[typing.Any] = None
  description: typing.Optional[str] = None
  group: typing.Optional[str] = None
  group_id: typing.Optional[typing.Union[int, float]] = None
  multiplexing: typing.Optional[bool] = None
  name: typing.Optional[str] = None
  platform: typing.Optional[str] = None
  pos: typing.Optional[str] = None
  sequence: typing.Optional[str] = None

  
  group_ref: typing.Optional[Group] = None
  multiplexes: list[Multiplex] = field(default_factory=list)
  platform_ref: typing.Optional[Platform] = None
  samples: list[Sample] = field(default_factory=list)
  tags: list[Tag] = field(default_factory=list)


# ---

def plainToApiKey(json: dict) -> ApiKey:
  obj = ApiKey()
  obj.active = bool(json.get('active'))
  obj.created = datetime.fromisoformat(json.get('created', '')) if json.get('created') else None
  obj.description = json.get('description')
  obj.expiration = datetime.fromisoformat(json.get('expiration', '')) if json.get('expiration') else None
  obj.generated_key = json.get('generated_key')
  obj.id = json.get('id')
  obj.internal = bool(json.get('internal'))
  obj.key_uid = json.get('key_uid')
  obj.role = json.get('role')
  obj.scientist_id = json.get('scientist_id')
  obj.routes = [ plainToApiKeyRoute(o) for o in json['routes'] ] if json.get('routes') else []
  obj.scientist_ref = plainToScientist(json['scientist_ref']) if json.get('scientist_ref') else None

  return obj

def serializeApiKey(obj: ApiKey) -> dict:
  json = {}
  json['active'] = obj.active
  json['created'] = obj.created.isoformat() if obj.created else None
  json['description'] = obj.description
  json['expiration'] = obj.expiration.isoformat() if obj.expiration else None
  json['generated_key'] = obj.generated_key
  json['id'] = obj.id
  json['internal'] = obj.internal
  json['key_uid'] = obj.key_uid
  json['role'] = obj.role
  json['scientist_id'] = obj.scientist_id
  if obj.routes is not None:
    json['routes'] = [ serializeApiKeyRoute(o) for o in obj.routes ]
  json['scientist_ref'] = serializeScientist(obj.scientist_ref) if obj.scientist_ref is not None else None

  return json


@dataclass
class ApiKey:
  active: typing.Optional[bool] = None
  created: typing.Optional[datetime] = None
  description: typing.Optional[str] = None
  expiration: typing.Optional[datetime] = None
  generated_key: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  internal: typing.Optional[bool] = None
  key_uid: typing.Optional[str] = None
  role: typing.Optional[str] = None
  scientist_id: typing.Optional[typing.Union[int, float]] = None

  
  routes: list[ApiKeyRoute] = field(default_factory=list)
  scientist_ref: typing.Optional[Scientist] = None


# ---

def plainToApiKeyRoute(json: dict) -> ApiKeyRoute:
  obj = ApiKeyRoute()
  obj.api_key_id = json.get('api_key_id')
  obj.method = json.get('method')
  obj.path = json.get('path')
  obj.api_key = plainToApiKey(json['api_key']) if json.get('api_key') else None

  return obj

def serializeApiKeyRoute(obj: ApiKeyRoute) -> dict:
  json = {}
  json['api_key_id'] = obj.api_key_id
  json['method'] = obj.method
  json['path'] = obj.path
  json['api_key'] = serializeApiKey(obj.api_key) if obj.api_key is not None else None

  return json


@dataclass
class ApiKeyRoute:
  api_key_id: typing.Optional[typing.Union[int, float]] = None
  method: typing.Optional[str] = None
  path: typing.Optional[str] = None

  
  api_key: typing.Optional[ApiKey] = None


# ---

def plainToAttachment(json: dict) -> Attachment:
  obj = Attachment()
  obj.description = json.get('description')
  obj.download = json.get('download')
  obj.filename = json.get('filename')
  obj.id = json.get('id')
  obj.internal = bool(json.get('internal'))
  obj.mimetype = json.get('mimetype')
  obj.request_id = json.get('request_id')
  obj.size = json.get('size')
  obj.request = plainToRequest(json['request']) if json.get('request') else None

  return obj

def serializeAttachment(obj: Attachment) -> dict:
  json = {}
  json['description'] = obj.description
  json['download'] = obj.download
  json['filename'] = obj.filename
  json['id'] = obj.id
  json['internal'] = obj.internal
  json['mimetype'] = obj.mimetype
  json['request_id'] = obj.request_id
  json['size'] = obj.size
  json['request'] = serializeRequest(obj.request) if obj.request is not None else None

  return json


@dataclass
class Attachment:
  description: typing.Optional[str] = None
  download: typing.Optional[str] = None
  filename: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  internal: typing.Optional[bool] = None
  mimetype: typing.Optional[str] = None
  request_id: typing.Optional[typing.Union[int, float]] = None
  size: typing.Optional[typing.Union[int, float]] = None

  
  request: typing.Optional[Request] = None


# ---

def plainToBarcodeScratch(json: dict) -> BarcodeScratch:
  obj = BarcodeScratch()
  obj.comment = json.get('comment')
  obj.data = json.get('data')
  obj.date = datetime.fromisoformat(json.get('date', '')) if json.get('date') else None
  obj.form = json.get('form')
  obj.id = json.get('id')
  obj.username = json.get('username')
  obj.form_ref = plainToForm(json['form_ref']) if json.get('form_ref') else None
  obj.user_ref = plainToScientist(json['user_ref']) if json.get('user_ref') else None

  return obj

def serializeBarcodeScratch(obj: BarcodeScratch) -> dict:
  json = {}
  json['comment'] = obj.comment
  json['data'] = obj.data
  json['date'] = obj.date.isoformat() if obj.date else None
  json['form'] = obj.form
  json['id'] = obj.id
  json['username'] = obj.username
  json['form_ref'] = serializeForm(obj.form_ref) if obj.form_ref is not None else None
  json['user_ref'] = serializeScientist(obj.user_ref) if obj.user_ref is not None else None

  return json


@dataclass
class BarcodeScratch:
  comment: typing.Optional[str] = None
  data: typing.Optional[str] = None
  date: typing.Optional[datetime] = None
  form: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  username: typing.Optional[str] = None

  
  form_ref: typing.Optional[Form] = None
  user_ref: typing.Optional[Scientist] = None


# ---

def plainToChangeset(json: dict) -> Changeset:
  obj = Changeset()
  obj.date = datetime.fromisoformat(json.get('date', '')) if json.get('date') else None
  obj.deleted = bool(json.get('deleted'))
  obj.form = json.get('form')
  obj.id = json.get('id')
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.last_change_username = json.get('last_change_username')
  obj.measurement_data_id = json.get('measurement_data_id')
  obj.username = json.get('username')
  obj.data_entries = [ plainToDataEntry(o) for o in json['data_entries'] ] if json.get('data_entries') else []
  obj.form_ref = plainToForm(json['form_ref']) if json.get('form_ref') else None
  obj.last_change_user_ref = plainToScientist(json['last_change_user_ref']) if json.get('last_change_user_ref') else None
  obj.user_ref = plainToScientist(json['user_ref']) if json.get('user_ref') else None

  return obj

def serializeChangeset(obj: Changeset) -> dict:
  json = {}
  json['date'] = obj.date.isoformat() if obj.date else None
  json['deleted'] = obj.deleted
  json['form'] = obj.form
  json['id'] = obj.id
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['last_change_username'] = obj.last_change_username
  json['measurement_data_id'] = obj.measurement_data_id
  json['username'] = obj.username
  if obj.data_entries is not None:
    json['data_entries'] = [ serializeDataEntry(o) for o in obj.data_entries ]
  json['form_ref'] = serializeForm(obj.form_ref) if obj.form_ref is not None else None
  json['last_change_user_ref'] = serializeScientist(obj.last_change_user_ref) if obj.last_change_user_ref is not None else None
  json['user_ref'] = serializeScientist(obj.user_ref) if obj.user_ref is not None else None

  return json


@dataclass
class Changeset:
  date: typing.Optional[datetime] = None
  deleted: typing.Optional[bool] = None
  form: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  last_change: typing.Optional[datetime] = None
  last_change_username: typing.Optional[str] = None
  measurement_data_id: typing.Optional[typing.Union[int, float]] = None
  username: typing.Optional[str] = None

  
  data_entries: list[DataEntry] = field(default_factory=list)
  form_ref: typing.Optional[Form] = None
  last_change_user_ref: typing.Optional[Scientist] = None
  user_ref: typing.Optional[Scientist] = None


# ---

def plainToControlSample(json: dict) -> ControlSample:
  obj = ControlSample()
  obj.control_sample_id = json.get('control_sample_id')
  obj.sample_id = json.get('sample_id')
  obj.control_sample = plainToSample(json['control_sample']) if json.get('control_sample') else None
  obj.sample = plainToSample(json['sample']) if json.get('sample') else None

  return obj

def serializeControlSample(obj: ControlSample) -> dict:
  json = {}
  json['control_sample_id'] = obj.control_sample_id
  json['sample_id'] = obj.sample_id
  json['control_sample'] = serializeSample(obj.control_sample) if obj.control_sample is not None else None
  json['sample'] = serializeSample(obj.sample) if obj.sample is not None else None

  return json


@dataclass
class ControlSample:
  control_sample_id: typing.Optional[typing.Union[int, float]] = None
  sample_id: typing.Optional[typing.Union[int, float]] = None

  
  control_sample: typing.Optional[Sample] = None
  sample: typing.Optional[Sample] = None


# ---

def plainToCostEstimate(json: dict) -> CostEstimate:
  obj = CostEstimate()
  obj.category_totals = json.get('category_totals')
  obj.created = datetime.fromisoformat(json.get('created', '')) if json.get('created') else None
  obj.group = json.get('group')
  obj.group_id = json.get('group_id')
  obj.id = json.get('id')
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.price_list = plainToPriceList(json['price_list']) if json.get('price_list') else None
  obj.price_list_id = json.get('price_list_id')
  obj.pricing_category = json.get('pricing_category')
  obj.project_name = json.get('project_name')
  obj.reference = json.get('reference')
  obj.request = plainToEstimateRequest(json['request']) if json.get('request') else None
  obj.request_id = json.get('request_id')
  obj.scientist = json.get('scientist')
  obj.scientist_id = json.get('scientist_id')
  obj.status = json.get('status')
  obj.total = json.get('total')
  obj.cost_estimate_items = [ plainToCostEstimateItem(o) for o in json['cost_estimate_items'] ] if json.get('cost_estimate_items') else []
  obj.group_ref = plainToGroup(json['group_ref']) if json.get('group_ref') else None
  obj.items = [ plainToCostEstimateItem(o) for o in json['items'] ] if json.get('items') else []
  obj.price_list_ref = plainToPriceList(json['price_list_ref']) if json.get('price_list_ref') else None
  obj.pricing_category_ref = plainToPricingCategory(json['pricing_category_ref']) if json.get('pricing_category_ref') else None
  obj.scientist_ref = plainToScientist(json['scientist_ref']) if json.get('scientist_ref') else None

  return obj

def serializeCostEstimate(obj: CostEstimate) -> dict:
  json = {}
  json['category_totals'] = obj.category_totals
  json['created'] = obj.created.isoformat() if obj.created else None
  json['group'] = obj.group
  json['group_id'] = obj.group_id
  json['id'] = obj.id
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['price_list'] = serializePriceList(obj.price_list) if obj.price_list is not None else None
  json['price_list_id'] = obj.price_list_id
  json['pricing_category'] = obj.pricing_category
  json['project_name'] = obj.project_name
  json['reference'] = obj.reference
  json['request'] = serializeEstimateRequest(obj.request) if obj.request is not None else None
  json['request_id'] = obj.request_id
  json['scientist'] = obj.scientist
  json['scientist_id'] = obj.scientist_id
  json['status'] = obj.status
  json['total'] = obj.total
  if obj.cost_estimate_items is not None:
    json['cost_estimate_items'] = [ serializeCostEstimateItem(o) for o in obj.cost_estimate_items ]
  json['group_ref'] = serializeGroup(obj.group_ref) if obj.group_ref is not None else None
  if obj.items is not None:
    json['items'] = [ serializeCostEstimateItem(o) for o in obj.items ]
  json['price_list_ref'] = serializePriceList(obj.price_list_ref) if obj.price_list_ref is not None else None
  json['pricing_category_ref'] = serializePricingCategory(obj.pricing_category_ref) if obj.pricing_category_ref is not None else None
  json['scientist_ref'] = serializeScientist(obj.scientist_ref) if obj.scientist_ref is not None else None

  return json


@dataclass
class CostEstimate:
  category_totals: typing.Optional[dict] = None
  created: typing.Optional[datetime] = None
  group: typing.Optional[typing.Any] = None
  group_id: typing.Optional[typing.Union[int, float]] = None
  id: typing.Optional[typing.Union[int, float]] = None
  last_change: typing.Optional[datetime] = None
  price_list: typing.Optional[PriceList] = None
  price_list_id: typing.Optional[typing.Union[int, float]] = None
  pricing_category: typing.Optional[str] = None
  project_name: typing.Optional[str] = None
  reference: typing.Optional[str] = None
  request: typing.Optional[EstimateRequest] = None
  request_id: typing.Optional[typing.Union[int, float]] = None
  scientist: typing.Optional[typing.Any] = None
  scientist_id: typing.Optional[typing.Union[int, float]] = None
  status: typing.Optional[str] = None
  total: typing.Optional[typing.Union[int, float]] = None

  
  cost_estimate_items: list[CostEstimateItem] = field(default_factory=list)
  group_ref: typing.Optional[Group] = None
  items: list[CostEstimateItem] = field(default_factory=list)
  price_list_ref: typing.Optional[PriceList] = None
  pricing_category_ref: typing.Optional[PricingCategory] = None
  scientist_ref: typing.Optional[Scientist] = None


# ---

def plainToCostEstimateItem(json: dict) -> CostEstimateItem:
  obj = CostEstimateItem()
  obj.category = json.get('category')
  obj.code = json.get('code')
  obj.cost_estimate_id = json.get('cost_estimate_id')
  obj.count = json.get('count')
  obj.description = json.get('description')
  obj.discount = json.get('discount')
  obj.heading = json.get('heading')
  obj.id = json.get('id')
  obj.item_id = json.get('item_id')
  obj.manual = bool(json.get('manual'))
  obj.price = json.get('price')
  obj.sort_order = json.get('sort_order')
  obj.total = json.get('total')
  obj.cost_estimate = plainToCostEstimate(json['cost_estimate']) if json.get('cost_estimate') else None
  obj.item = plainToPriceListItem(json['item']) if json.get('item') else None

  return obj

def serializeCostEstimateItem(obj: CostEstimateItem) -> dict:
  json = {}
  json['category'] = obj.category
  json['code'] = obj.code
  json['cost_estimate_id'] = obj.cost_estimate_id
  json['count'] = obj.count
  json['description'] = obj.description
  json['discount'] = obj.discount
  json['heading'] = obj.heading
  json['id'] = obj.id
  json['item_id'] = obj.item_id
  json['manual'] = obj.manual
  json['price'] = obj.price
  json['sort_order'] = obj.sort_order
  json['total'] = obj.total
  json['cost_estimate'] = serializeCostEstimate(obj.cost_estimate) if obj.cost_estimate is not None else None
  json['item'] = serializePriceListItem(obj.item) if obj.item is not None else None

  return json


@dataclass
class CostEstimateItem:
  category: typing.Optional[str] = None
  code: typing.Optional[str] = None
  cost_estimate_id: typing.Optional[typing.Union[int, float]] = None
  count: typing.Optional[typing.Union[int, float]] = None
  description: typing.Optional[str] = None
  discount: typing.Optional[typing.Union[int, float]] = None
  heading: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  item_id: typing.Optional[typing.Union[int, float]] = None
  manual: typing.Optional[bool] = None
  price: typing.Optional[typing.Union[int, float]] = None
  sort_order: typing.Optional[str] = None
  total: typing.Optional[typing.Union[int, float]] = None

  
  cost_estimate: typing.Optional[CostEstimate] = None
  item: typing.Optional[PriceListItem] = None


# ---

def plainToCutoutSize(json: dict) -> CutoutSize:
  obj = CutoutSize()
  obj.available = bool(json.get('available'))
  obj.cutout_size = json.get('cutout_size')
  obj.kit = json.get('kit')
  obj.platform = json.get('platform')
  obj.prep_type = json.get('prep_type')
  obj.platform_ref = plainToPlatform(json['platform_ref']) if json.get('platform_ref') else None
  obj.preparation_kits_ref = plainToPreparationKit(json['preparation_kits_ref']) if json.get('preparation_kits_ref') else None
  obj.preparation_types_ref = plainToPreparationType(json['preparation_types_ref']) if json.get('preparation_types_ref') else None
  obj.samples = [ plainToSample(o) for o in json['samples'] ] if json.get('samples') else []

  return obj

def serializeCutoutSize(obj: CutoutSize) -> dict:
  json = {}
  json['available'] = obj.available
  json['cutout_size'] = obj.cutout_size
  json['kit'] = obj.kit
  json['platform'] = obj.platform
  json['prep_type'] = obj.prep_type
  json['platform_ref'] = serializePlatform(obj.platform_ref) if obj.platform_ref is not None else None
  json['preparation_kits_ref'] = serializePreparationKit(obj.preparation_kits_ref) if obj.preparation_kits_ref is not None else None
  json['preparation_types_ref'] = serializePreparationType(obj.preparation_types_ref) if obj.preparation_types_ref is not None else None
  if obj.samples is not None:
    json['samples'] = [ serializeSample(o) for o in obj.samples ]

  return json


@dataclass
class CutoutSize:
  available: typing.Optional[bool] = None
  cutout_size: typing.Optional[str] = None
  kit: typing.Optional[str] = None
  platform: typing.Optional[str] = None
  prep_type: typing.Optional[str] = None

  
  platform_ref: typing.Optional[Platform] = None
  preparation_kits_ref: typing.Optional[PreparationKit] = None
  preparation_types_ref: typing.Optional[PreparationType] = None
  samples: list[Sample] = field(default_factory=list)


# ---

def plainToDataEntry(json: dict) -> DataEntry:
  obj = DataEntry()
  obj.changeset_id = json.get('changeset_id')
  obj.comment_text = json.get('comment_text')
  obj.control = json.get('control')
  obj.deleted = bool(json.get('deleted'))
  obj.entry_date = datetime.fromisoformat(json.get('entry_date', '')) if json.get('entry_date') else None
  obj.flag = json.get('flag')
  obj.form = json.get('form')
  obj.id = json.get('id')
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.last_change_username = json.get('last_change_username')
  obj.multi_id = json.get('multi_id')
  obj.notified = bool(json.get('notified'))
  obj.obj_id = json.get('obj_id')
  obj.obj_type = json.get('obj_type')
  obj.request_id = json.get('request_id')
  obj.resolved = bool(json.get('resolved'))
  obj.row_number = json.get('row_number')
  obj.username = json.get('username')
  obj.values = json.get('values')
  obj.changeset = plainToChangeset(json['changeset']) if json.get('changeset') else None
  obj.form_ref = plainToForm(json['form_ref']) if json.get('form_ref') else None
  obj.last_change_user_ref = plainToScientist(json['last_change_user_ref']) if json.get('last_change_user_ref') else None
  obj.multi = plainToMultiplex(json['multi']) if json.get('multi') else None
  obj.multiplex = plainToMultiplex(json['multiplex']) if json.get('multiplex') else None
  obj.request = plainToRequest(json['request']) if json.get('request') else None
  obj.run_unit = plainToRunUnit(json['run_unit']) if json.get('run_unit') else None
  obj.sample = plainToSample(json['sample']) if json.get('sample') else None
  obj.user_ref = plainToScientist(json['user_ref']) if json.get('user_ref') else None

  return obj

def serializeDataEntry(obj: DataEntry) -> dict:
  json = {}
  json['changeset_id'] = obj.changeset_id
  json['comment_text'] = obj.comment_text
  json['control'] = obj.control
  json['deleted'] = obj.deleted
  json['entry_date'] = obj.entry_date.isoformat() if obj.entry_date else None
  json['flag'] = obj.flag
  json['form'] = obj.form
  json['id'] = obj.id
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['last_change_username'] = obj.last_change_username
  json['multi_id'] = obj.multi_id
  json['notified'] = obj.notified
  json['obj_id'] = obj.obj_id
  json['obj_type'] = obj.obj_type
  json['request_id'] = obj.request_id
  json['resolved'] = obj.resolved
  json['row_number'] = obj.row_number
  json['username'] = obj.username
  json['values'] = obj.values
  json['changeset'] = serializeChangeset(obj.changeset) if obj.changeset is not None else None
  json['form_ref'] = serializeForm(obj.form_ref) if obj.form_ref is not None else None
  json['last_change_user_ref'] = serializeScientist(obj.last_change_user_ref) if obj.last_change_user_ref is not None else None
  json['multi'] = serializeMultiplex(obj.multi) if obj.multi is not None else None
  json['multiplex'] = serializeMultiplex(obj.multiplex) if obj.multiplex is not None else None
  json['request'] = serializeRequest(obj.request) if obj.request is not None else None
  json['run_unit'] = serializeRunUnit(obj.run_unit) if obj.run_unit is not None else None
  json['sample'] = serializeSample(obj.sample) if obj.sample is not None else None
  json['user_ref'] = serializeScientist(obj.user_ref) if obj.user_ref is not None else None

  return json


@dataclass
class DataEntry:
  changeset_id: typing.Optional[typing.Union[int, float]] = None
  comment_text: typing.Optional[str] = None
  control: typing.Optional[str] = None
  deleted: typing.Optional[bool] = None
  entry_date: typing.Optional[datetime] = None
  flag: typing.Optional[str] = None
  form: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  last_change: typing.Optional[datetime] = None
  last_change_username: typing.Optional[str] = None
  multi_id: typing.Optional[typing.Union[int, float]] = None
  notified: typing.Optional[bool] = None
  obj_id: typing.Optional[typing.Union[int, float]] = None
  obj_type: typing.Optional[str] = None
  request_id: typing.Optional[typing.Union[int, float]] = None
  resolved: typing.Optional[bool] = None
  row_number: typing.Optional[typing.Union[int, float]] = None
  username: typing.Optional[str] = None
  values: typing.Optional[dict] = None

  
  changeset: typing.Optional[Changeset] = None
  form_ref: typing.Optional[Form] = None
  last_change_user_ref: typing.Optional[Scientist] = None
  multi: typing.Optional[Multiplex] = None
  multiplex: typing.Optional[Multiplex] = None
  request: typing.Optional[Request] = None
  run_unit: typing.Optional[RunUnit] = None
  sample: typing.Optional[Sample] = None
  user_ref: typing.Optional[Scientist] = None


# ---

def plainToFastqc(json: dict) -> Fastqc:
  obj = Fastqc()
  obj.barcode = json.get('barcode')
  obj.basecalls = json.get('basecalls')
  obj.basic_result = json.get('basic_result')
  obj.count_q30 = json.get('count_q30')
  obj.count_q33 = json.get('count_q33')
  obj.count_q35 = json.get('count_q35')
  obj.count_q37 = json.get('count_q37')
  obj.date = datetime.fromisoformat(json.get('date', '')) if json.get('date') else None
  obj.duplication_levels = json.get('duplication_levels')
  obj.duplication_percent = json.get('duplication_percent')
  obj.duplication_result = json.get('duplication_result')
  obj.flowcell = json.get('flowcell')
  obj.id = json.get('id')
  obj.lane = json.get('lane')
  obj.over_illumina = json.get('over_illumina')
  obj.over_no_hit = json.get('over_no_hit')
  obj.over_other = json.get('over_other')
  obj.over_result = json.get('over_result')
  obj.path = json.get('path')
  obj.read = json.get('read')
  obj.result_check_id = json.get('result_check_id')
  obj.run_id = json.get('run_id')
  obj.total_count = json.get('total_count')
  obj.result_check = plainToResultCheck(json['result_check']) if json.get('result_check') else None

  return obj

def serializeFastqc(obj: Fastqc) -> dict:
  json = {}
  json['barcode'] = obj.barcode
  json['basecalls'] = obj.basecalls
  json['basic_result'] = obj.basic_result
  json['count_q30'] = obj.count_q30
  json['count_q33'] = obj.count_q33
  json['count_q35'] = obj.count_q35
  json['count_q37'] = obj.count_q37
  json['date'] = obj.date.isoformat() if obj.date else None
  json['duplication_levels'] = obj.duplication_levels
  json['duplication_percent'] = obj.duplication_percent
  json['duplication_result'] = obj.duplication_result
  json['flowcell'] = obj.flowcell
  json['id'] = obj.id
  json['lane'] = obj.lane
  json['over_illumina'] = obj.over_illumina
  json['over_no_hit'] = obj.over_no_hit
  json['over_other'] = obj.over_other
  json['over_result'] = obj.over_result
  json['path'] = obj.path
  json['read'] = obj.read
  json['result_check_id'] = obj.result_check_id
  json['run_id'] = obj.run_id
  json['total_count'] = obj.total_count
  json['result_check'] = serializeResultCheck(obj.result_check) if obj.result_check is not None else None

  return json


@dataclass
class Fastqc:
  barcode: typing.Optional[str] = None
  basecalls: typing.Optional[str] = None
  basic_result: typing.Optional[str] = None
  count_q30: typing.Optional[typing.Any] = None
  count_q33: typing.Optional[typing.Any] = None
  count_q35: typing.Optional[typing.Any] = None
  count_q37: typing.Optional[typing.Any] = None
  date: typing.Optional[datetime] = None
  duplication_levels: typing.Optional[str] = None
  duplication_percent: typing.Optional[typing.Any] = None
  duplication_result: typing.Optional[str] = None
  flowcell: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  lane: typing.Optional[typing.Union[int, float]] = None
  over_illumina: typing.Optional[typing.Any] = None
  over_no_hit: typing.Optional[typing.Any] = None
  over_other: typing.Optional[typing.Any] = None
  over_result: typing.Optional[str] = None
  path: typing.Optional[str] = None
  read: typing.Optional[str] = None
  result_check_id: typing.Optional[typing.Union[int, float]] = None
  run_id: typing.Optional[typing.Union[int, float]] = None
  total_count: typing.Optional[typing.Any] = None

  
  result_check: typing.Optional[ResultCheck] = None


# ---

def plainToForm(json: dict) -> Form:
  obj = Form()
  obj.config = plainToFormConfig(json['config']) if json.get('config') else None
  obj.fields = [ plainToDataEntryField(o) for o in json['fields'] ] if json.get('fields') else []
  obj.id = json.get('id')
  obj.name = json.get('name')
  obj.ordering = json.get('ordering')
  obj.platform = json.get('platform')
  obj.changesets = [ plainToChangeset(o) for o in json['changesets'] ] if json.get('changesets') else []
  obj.data_entries = [ plainToDataEntry(o) for o in json['data_entries'] ] if json.get('data_entries') else []
  obj.platform_ref = plainToPlatform(json['platform_ref']) if json.get('platform_ref') else None

  return obj

def serializeForm(obj: Form) -> dict:
  json = {}
  json['config'] = serializeFormConfig(obj.config) if obj.config is not None else None
  if obj.fields is not None:
    json['fields'] = [ serializeDataEntryField(o) for o in obj.fields ]
  json['id'] = obj.id
  json['name'] = obj.name
  json['ordering'] = obj.ordering
  json['platform'] = obj.platform
  if obj.changesets is not None:
    json['changesets'] = [ serializeChangeset(o) for o in obj.changesets ]
  if obj.data_entries is not None:
    json['data_entries'] = [ serializeDataEntry(o) for o in obj.data_entries ]
  json['platform_ref'] = serializePlatform(obj.platform_ref) if obj.platform_ref is not None else None

  return json


@dataclass
class Form:
  config: typing.Optional[FormConfig] = None
  fields: list[DataEntryField]=field(default_factory=list)
  id: typing.Optional[typing.Union[int, float]] = None
  name: typing.Optional[str] = None
  ordering: typing.Optional[typing.Union[int, float]] = None
  platform: typing.Optional[str] = None

  
  changesets: list[Changeset] = field(default_factory=list)
  data_entries: list[DataEntry] = field(default_factory=list)
  platform_ref: typing.Optional[Platform] = None


# ---

def plainToGroup(json: dict) -> Group:
  obj = Group()
  obj.active = bool(json.get('active'))
  obj.announce_subscribed = bool(json.get('announce_subscribed'))
  obj.billing_address = json.get('billing_address')
  obj.billing_atu = json.get('billing_atu')
  obj.billing_institute = json.get('billing_institute')
  obj.billing_type = json.get('billing_type')
  obj.created = datetime.fromisoformat(json.get('created', '')) if json.get('created') else None
  obj.email = json.get('email')
  obj.id = json.get('id')
  obj.imp_storage = bool(json.get('imp_storage'))
  obj.institute = json.get('institute')
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.miseq_selfservice = bool(json.get('miseq_selfservice'))
  obj.name = json.get('name')
  obj.obj_id = json.get('obj_id')
  obj.obj_type = json.get('obj_type')
  obj.billing_type_ref = plainToPricingCategory(json['billing_type_ref']) if json.get('billing_type_ref') else None
  obj.projects = [ plainToProject(o) for o in json['projects'] ] if json.get('projects') else []
  obj.requests = [ plainToRequest(o) for o in json['requests'] ] if json.get('requests') else []
  obj.scientists = [ plainToScientist(o) for o in json['scientists'] ] if json.get('scientists') else []

  return obj

def serializeGroup(obj: Group) -> dict:
  json = {}
  json['active'] = obj.active
  json['announce_subscribed'] = obj.announce_subscribed
  json['billing_address'] = obj.billing_address
  json['billing_atu'] = obj.billing_atu
  json['billing_institute'] = obj.billing_institute
  json['billing_type'] = obj.billing_type
  json['created'] = obj.created.isoformat() if obj.created else None
  json['email'] = obj.email
  json['id'] = obj.id
  json['imp_storage'] = obj.imp_storage
  json['institute'] = obj.institute
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['miseq_selfservice'] = obj.miseq_selfservice
  json['name'] = obj.name
  json['obj_id'] = obj.obj_id
  json['obj_type'] = obj.obj_type
  json['billing_type_ref'] = serializePricingCategory(obj.billing_type_ref) if obj.billing_type_ref is not None else None
  if obj.projects is not None:
    json['projects'] = [ serializeProject(o) for o in obj.projects ]
  if obj.requests is not None:
    json['requests'] = [ serializeRequest(o) for o in obj.requests ]
  if obj.scientists is not None:
    json['scientists'] = [ serializeScientist(o) for o in obj.scientists ]

  return json


@dataclass
class Group:
  active: typing.Optional[bool] = None
  announce_subscribed: typing.Optional[bool] = None
  billing_address: typing.Optional[str] = None
  billing_atu: typing.Optional[str] = None
  billing_institute: typing.Optional[str] = None
  billing_type: typing.Optional[str] = None
  created: typing.Optional[datetime] = None
  email: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  imp_storage: typing.Optional[bool] = None
  institute: typing.Optional[str] = None
  last_change: typing.Optional[datetime] = None
  miseq_selfservice: typing.Optional[bool] = None
  name: typing.Optional[str] = None
  obj_id: typing.Optional[typing.Union[int, float]] = None
  obj_type: typing.Optional[str] = None

  
  billing_type_ref: typing.Optional[PricingCategory] = None
  projects: list[Project] = field(default_factory=list)
  requests: list[Request] = field(default_factory=list)
  scientists: list[Scientist] = field(default_factory=list)


# ---

def plainToIlluminaRun(json: dict) -> IlluminaRun:
  obj = IlluminaRun()
  obj.cbot = json.get('cbot')
  obj.clustering_kit_lot = json.get('clustering_kit_lot')
  obj.clustering_kit_version = json.get('clustering_kit_version')
  obj.clusterkit_box_1 = json.get('clusterkit_box_1')
  obj.clusterkit_box_2 = json.get('clusterkit_box_2')
  obj.comments = json.get('comments')
  obj.description = json.get('description')
  obj.draft = bool(json.get('draft'))
  obj.group = json.get('group')
  obj.group_id = json.get('group_id')
  obj.id = json.get('id')
  obj.index_length = json.get('index_length')
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.machine = json.get('machine')
  obj.name = json.get('name')
  obj.obj_type = json.get('obj_type')
  obj.platform = json.get('platform')
  obj.preparation_date = datetime.fromisoformat(json.get('preparation_date', '')) if json.get('preparation_date') else None
  obj.read1_length = json.get('read1_length')
  obj.read2_length = json.get('read2_length')
  obj.readmode = plainToReadmode(json['readmode']) if json.get('readmode') else None
  obj.readmode_id = json.get('readmode_id')
  obj.report_url = json.get('report_url')
  obj.run_folder = json.get('run_folder')
  obj.run_id = json.get('run_id')
  obj.sbs_minus_20 = json.get('sbs_minus_20')
  obj.sbs_plus_4 = json.get('sbs_plus_4')
  obj.scientist = json.get('scientist')
  obj.scientist_id = json.get('scientist_id')
  obj.secondary_index_length = json.get('secondary_index_length')
  obj.selfservice = bool(json.get('selfservice'))
  obj.sequencing_date = datetime.fromisoformat(json.get('sequencing_date', '')) if json.get('sequencing_date') else None
  obj.status = json.get('status')
  obj.username = json.get('username')
  obj.vendor_id = json.get('vendor_id')
  obj.xp_enabled = bool(json.get('xp_enabled'))
  obj.inventory_changes = [ plainToInventoryChange(o) for o in json['inventory_changes'] ] if json.get('inventory_changes') else []
  obj.lanes = [ plainToLane(o) for o in json['lanes'] ] if json.get('lanes') else []
  obj.run = plainToRun(json['run']) if json.get('run') else None

  return obj

def serializeIlluminaRun(obj: IlluminaRun) -> dict:
  json = {}
  json['cbot'] = obj.cbot
  json['clustering_kit_lot'] = obj.clustering_kit_lot
  json['clustering_kit_version'] = obj.clustering_kit_version
  json['clusterkit_box_1'] = obj.clusterkit_box_1
  json['clusterkit_box_2'] = obj.clusterkit_box_2
  json['comments'] = obj.comments
  json['description'] = obj.description
  json['draft'] = obj.draft
  json['group'] = obj.group
  json['group_id'] = obj.group_id
  json['id'] = obj.id
  json['index_length'] = obj.index_length
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['machine'] = obj.machine
  json['name'] = obj.name
  json['obj_type'] = obj.obj_type
  json['platform'] = obj.platform
  json['preparation_date'] = obj.preparation_date.isoformat() if obj.preparation_date else None
  json['read1_length'] = obj.read1_length
  json['read2_length'] = obj.read2_length
  json['readmode'] = serializeReadmode(obj.readmode) if obj.readmode is not None else None
  json['readmode_id'] = obj.readmode_id
  json['report_url'] = obj.report_url
  json['run_folder'] = obj.run_folder
  json['run_id'] = obj.run_id
  json['sbs_minus_20'] = obj.sbs_minus_20
  json['sbs_plus_4'] = obj.sbs_plus_4
  json['scientist'] = obj.scientist
  json['scientist_id'] = obj.scientist_id
  json['secondary_index_length'] = obj.secondary_index_length
  json['selfservice'] = obj.selfservice
  json['sequencing_date'] = obj.sequencing_date.isoformat() if obj.sequencing_date else None
  json['status'] = obj.status
  json['username'] = obj.username
  json['vendor_id'] = obj.vendor_id
  json['xp_enabled'] = obj.xp_enabled
  if obj.inventory_changes is not None:
    json['inventory_changes'] = [ serializeInventoryChange(o) for o in obj.inventory_changes ]
  if obj.lanes is not None:
    json['lanes'] = [ serializeLane(o) for o in obj.lanes ]
  json['run'] = serializeRun(obj.run) if obj.run is not None else None

  return json


@dataclass
class IlluminaRun:
  cbot: typing.Optional[str] = None
  clustering_kit_lot: typing.Optional[str] = None
  clustering_kit_version: typing.Optional[str] = None
  clusterkit_box_1: typing.Optional[str] = None
  clusterkit_box_2: typing.Optional[str] = None
  comments: typing.Optional[str] = None
  description: typing.Optional[str] = None
  draft: typing.Optional[bool] = None
  group: typing.Optional[typing.Any] = None
  group_id: typing.Optional[typing.Union[int, float]] = None
  id: typing.Optional[typing.Union[int, float]] = None
  index_length: typing.Optional[typing.Union[int, float]] = None
  last_change: typing.Optional[datetime] = None
  machine: typing.Optional[str] = None
  name: typing.Optional[str] = None
  obj_type: typing.Optional[str] = None
  platform: typing.Optional[str] = None
  preparation_date: typing.Optional[datetime] = None
  read1_length: typing.Optional[typing.Union[int, float]] = None
  read2_length: typing.Optional[typing.Union[int, float]] = None
  readmode: typing.Optional[Readmode] = None
  readmode_id: typing.Optional[typing.Union[int, float]] = None
  report_url: typing.Optional[str] = None
  run_folder: typing.Optional[str] = None
  run_id: typing.Optional[typing.Union[int, float]] = None
  sbs_minus_20: typing.Optional[str] = None
  sbs_plus_4: typing.Optional[str] = None
  scientist: typing.Optional[typing.Any] = None
  scientist_id: typing.Optional[typing.Union[int, float]] = None
  secondary_index_length: typing.Optional[typing.Union[int, float]] = None
  selfservice: typing.Optional[bool] = None
  sequencing_date: typing.Optional[datetime] = None
  status: typing.Optional[str] = None
  username: typing.Optional[str] = None
  vendor_id: typing.Optional[str] = None
  xp_enabled: typing.Optional[bool] = None

  
  inventory_changes: list[InventoryChange] = field(default_factory=list)
  lanes: list[Lane] = field(default_factory=list)
  run: typing.Optional[Run] = None


# ---

def plainToInventoryChange(json: dict) -> InventoryChange:
  obj = InventoryChange()
  obj.change = json.get('change')
  obj.comment = json.get('comment')
  obj.date = datetime.fromisoformat(json.get('date', '')) if json.get('date') else None
  obj.draft = bool(json.get('draft'))
  obj.id = json.get('id')
  obj.item = json.get('item')
  obj.run_id = json.get('run_id')
  obj.username = json.get('username')
  obj.inventory_item = plainToInventoryItem(json['inventory_item']) if json.get('inventory_item') else None
  obj.run = plainToRun(json['run']) if json.get('run') else None
  obj.user_ref = plainToScientist(json['user_ref']) if json.get('user_ref') else None

  return obj

def serializeInventoryChange(obj: InventoryChange) -> dict:
  json = {}
  json['change'] = obj.change
  json['comment'] = obj.comment
  json['date'] = obj.date.isoformat() if obj.date else None
  json['draft'] = obj.draft
  json['id'] = obj.id
  json['item'] = obj.item
  json['run_id'] = obj.run_id
  json['username'] = obj.username
  json['inventory_item'] = serializeInventoryItem(obj.inventory_item) if obj.inventory_item is not None else None
  json['run'] = serializeRun(obj.run) if obj.run is not None else None
  json['user_ref'] = serializeScientist(obj.user_ref) if obj.user_ref is not None else None

  return json


@dataclass
class InventoryChange:
  change: typing.Optional[typing.Union[int, float]] = None
  comment: typing.Optional[str] = None
  date: typing.Optional[datetime] = None
  draft: typing.Optional[bool] = None
  id: typing.Optional[typing.Union[int, float]] = None
  item: typing.Optional[str] = None
  run_id: typing.Optional[typing.Union[int, float]] = None
  username: typing.Optional[str] = None

  
  inventory_item: typing.Optional[InventoryItem] = None
  run: typing.Optional[Run] = None
  user_ref: typing.Optional[Scientist] = None


# ---

def plainToInventoryItem(json: dict) -> InventoryItem:
  obj = InventoryItem()
  obj.active = bool(json.get('active'))
  obj.cat = json.get('cat')
  obj.count = json.get('count')
  obj.description = json.get('description')
  obj.item = json.get('item')
  obj.link = json.get('link')
  obj.pricing_item_name = json.get('pricing_item_name')
  obj.threshold = json.get('threshold')
  obj.type = json.get('type')
  obj.inventory_changes = [ plainToInventoryChange(o) for o in json['inventory_changes'] ] if json.get('inventory_changes') else []
  obj.pricing_item = plainToPricingItem(json['pricing_item']) if json.get('pricing_item') else None

  return obj

def serializeInventoryItem(obj: InventoryItem) -> dict:
  json = {}
  json['active'] = obj.active
  json['cat'] = obj.cat
  json['count'] = obj.count
  json['description'] = obj.description
  json['item'] = obj.item
  json['link'] = obj.link
  json['pricing_item_name'] = obj.pricing_item_name
  json['threshold'] = obj.threshold
  json['type'] = obj.type
  if obj.inventory_changes is not None:
    json['inventory_changes'] = [ serializeInventoryChange(o) for o in obj.inventory_changes ]
  json['pricing_item'] = serializePricingItem(obj.pricing_item) if obj.pricing_item is not None else None

  return json


@dataclass
class InventoryItem:
  active: typing.Optional[bool] = None
  cat: typing.Optional[str] = None
  count: typing.Optional[typing.Union[int, float]] = None
  description: typing.Optional[str] = None
  item: typing.Optional[str] = None
  link: typing.Optional[str] = None
  pricing_item_name: typing.Optional[str] = None
  threshold: typing.Optional[typing.Union[int, float]] = None
  type: typing.Optional[str] = None

  
  inventory_changes: list[InventoryChange] = field(default_factory=list)
  pricing_item: typing.Optional[PricingItem] = None


# ---

def plainToInvoice(json: dict) -> Invoice:
  obj = Invoice()
  obj.category_totals = json.get('category_totals')
  obj.created = datetime.fromisoformat(json.get('created', '')) if json.get('created') else None
  obj.group = json.get('group')
  obj.group_id = json.get('group_id')
  obj.id = json.get('id')
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.price_list = plainToPriceList(json['price_list']) if json.get('price_list') else None
  obj.price_list_id = json.get('price_list_id')
  obj.pricing_category = json.get('pricing_category')
  obj.project_name = json.get('project_name')
  obj.reference = json.get('reference')
  obj.request = plainToEstimateRequest(json['request']) if json.get('request') else None
  obj.request_id = json.get('request_id')
  obj.scientist = json.get('scientist')
  obj.scientist_id = json.get('scientist_id')
  obj.status = json.get('status')
  obj.total = json.get('total')
  obj.group_ref = plainToGroup(json['group_ref']) if json.get('group_ref') else None
  obj.invoice_items = [ plainToInvoiceItem(o) for o in json['invoice_items'] ] if json.get('invoice_items') else []
  obj.items = [ plainToInvoiceItem(o) for o in json['items'] ] if json.get('items') else []
  obj.price_list_ref = plainToPriceList(json['price_list_ref']) if json.get('price_list_ref') else None
  obj.pricing_category_ref = plainToPricingCategory(json['pricing_category_ref']) if json.get('pricing_category_ref') else None
  obj.scientist_ref = plainToScientist(json['scientist_ref']) if json.get('scientist_ref') else None

  return obj

def serializeInvoice(obj: Invoice) -> dict:
  json = {}
  json['category_totals'] = obj.category_totals
  json['created'] = obj.created.isoformat() if obj.created else None
  json['group'] = obj.group
  json['group_id'] = obj.group_id
  json['id'] = obj.id
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['price_list'] = serializePriceList(obj.price_list) if obj.price_list is not None else None
  json['price_list_id'] = obj.price_list_id
  json['pricing_category'] = obj.pricing_category
  json['project_name'] = obj.project_name
  json['reference'] = obj.reference
  json['request'] = serializeEstimateRequest(obj.request) if obj.request is not None else None
  json['request_id'] = obj.request_id
  json['scientist'] = obj.scientist
  json['scientist_id'] = obj.scientist_id
  json['status'] = obj.status
  json['total'] = obj.total
  json['group_ref'] = serializeGroup(obj.group_ref) if obj.group_ref is not None else None
  if obj.invoice_items is not None:
    json['invoice_items'] = [ serializeInvoiceItem(o) for o in obj.invoice_items ]
  if obj.items is not None:
    json['items'] = [ serializeInvoiceItem(o) for o in obj.items ]
  json['price_list_ref'] = serializePriceList(obj.price_list_ref) if obj.price_list_ref is not None else None
  json['pricing_category_ref'] = serializePricingCategory(obj.pricing_category_ref) if obj.pricing_category_ref is not None else None
  json['scientist_ref'] = serializeScientist(obj.scientist_ref) if obj.scientist_ref is not None else None

  return json


@dataclass
class Invoice:
  category_totals: typing.Optional[dict] = None
  created: typing.Optional[datetime] = None
  group: typing.Optional[typing.Any] = None
  group_id: typing.Optional[typing.Union[int, float]] = None
  id: typing.Optional[typing.Union[int, float]] = None
  last_change: typing.Optional[datetime] = None
  price_list: typing.Optional[PriceList] = None
  price_list_id: typing.Optional[typing.Union[int, float]] = None
  pricing_category: typing.Optional[str] = None
  project_name: typing.Optional[str] = None
  reference: typing.Optional[str] = None
  request: typing.Optional[EstimateRequest] = None
  request_id: typing.Optional[typing.Union[int, float]] = None
  scientist: typing.Optional[typing.Any] = None
  scientist_id: typing.Optional[typing.Union[int, float]] = None
  status: typing.Optional[str] = None
  total: typing.Optional[typing.Union[int, float]] = None

  
  group_ref: typing.Optional[Group] = None
  invoice_items: list[InvoiceItem] = field(default_factory=list)
  items: list[InvoiceItem] = field(default_factory=list)
  price_list_ref: typing.Optional[PriceList] = None
  pricing_category_ref: typing.Optional[PricingCategory] = None
  scientist_ref: typing.Optional[Scientist] = None


# ---

def plainToInvoiceItem(json: dict) -> InvoiceItem:
  obj = InvoiceItem()
  obj.category = json.get('category')
  obj.code = json.get('code')
  obj.count = json.get('count')
  obj.description = json.get('description')
  obj.discount = json.get('discount')
  obj.heading = json.get('heading')
  obj.id = json.get('id')
  obj.invoice_id = json.get('invoice_id')
  obj.item_id = json.get('item_id')
  obj.manual = bool(json.get('manual'))
  obj.price = json.get('price')
  obj.reason = json.get('reason')
  obj.sent_date = datetime.fromisoformat(json.get('sent_date', '')) if json.get('sent_date') else None
  obj.sort_order = json.get('sort_order')
  obj.status = json.get('status')
  obj.total = json.get('total')
  obj.invoice = plainToInvoice(json['invoice']) if json.get('invoice') else None
  obj.item = plainToPriceListItem(json['item']) if json.get('item') else None

  return obj

def serializeInvoiceItem(obj: InvoiceItem) -> dict:
  json = {}
  json['category'] = obj.category
  json['code'] = obj.code
  json['count'] = obj.count
  json['description'] = obj.description
  json['discount'] = obj.discount
  json['heading'] = obj.heading
  json['id'] = obj.id
  json['invoice_id'] = obj.invoice_id
  json['item_id'] = obj.item_id
  json['manual'] = obj.manual
  json['price'] = obj.price
  json['reason'] = obj.reason
  json['sent_date'] = obj.sent_date.isoformat() if obj.sent_date else None
  json['sort_order'] = obj.sort_order
  json['status'] = obj.status
  json['total'] = obj.total
  json['invoice'] = serializeInvoice(obj.invoice) if obj.invoice is not None else None
  json['item'] = serializePriceListItem(obj.item) if obj.item is not None else None

  return json


@dataclass
class InvoiceItem:
  category: typing.Optional[str] = None
  code: typing.Optional[str] = None
  count: typing.Optional[typing.Union[int, float]] = None
  description: typing.Optional[str] = None
  discount: typing.Optional[typing.Union[int, float]] = None
  heading: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  invoice_id: typing.Optional[typing.Union[int, float]] = None
  item_id: typing.Optional[typing.Union[int, float]] = None
  manual: typing.Optional[bool] = None
  price: typing.Optional[typing.Union[int, float]] = None
  reason: typing.Optional[str] = None
  sent_date: typing.Optional[datetime] = None
  sort_order: typing.Optional[str] = None
  status: typing.Optional[str] = None
  total: typing.Optional[typing.Union[int, float]] = None

  
  invoice: typing.Optional[Invoice] = None
  item: typing.Optional[PriceListItem] = None


# ---

def plainToItemCategoryPrice(json: dict) -> ItemCategoryPrice:
  obj = ItemCategoryPrice()
  obj.category = json.get('category')
  obj.item_id = json.get('item_id')
  obj.price = json.get('price')
  obj.category_ref = plainToPricingCategory(json['category_ref']) if json.get('category_ref') else None
  obj.item = plainToPriceListItem(json['item']) if json.get('item') else None

  return obj

def serializeItemCategoryPrice(obj: ItemCategoryPrice) -> dict:
  json = {}
  json['category'] = obj.category
  json['item_id'] = obj.item_id
  json['price'] = obj.price
  json['category_ref'] = serializePricingCategory(obj.category_ref) if obj.category_ref is not None else None
  json['item'] = serializePriceListItem(obj.item) if obj.item is not None else None

  return json


@dataclass
class ItemCategoryPrice:
  category: typing.Optional[str] = None
  item_id: typing.Optional[typing.Union[int, float]] = None
  price: typing.Optional[typing.Union[int, float]] = None

  
  category_ref: typing.Optional[PricingCategory] = None
  item: typing.Optional[PriceListItem] = None


# ---

def plainToLane(json: dict) -> Lane:
  obj = Lane()
  obj.comments = json.get('comments')
  obj.conc = json.get('conc')
  obj.discount = json.get('discount')
  obj.group = json.get('group')
  obj.invoice_status = json.get('invoice_status')
  obj.is_saved = bool(json.get('is_saved'))
  obj.lane_checks = [ plainToResultCheck(o) for o in json['lane_checks'] ] if json.get('lane_checks') else []
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.needs_demultiplexing = bool(json.get('needs_demultiplexing'))
  obj.num = json.get('num')
  obj.phix = json.get('phix')
  obj.primer = json.get('primer')
  obj.run_id = json.get('run_id')
  obj.sample_fields = plainToSampleFields(json['sample_fields']) if json.get('sample_fields') else None
  obj.sampnum = json.get('sampnum')
  obj.scientist = json.get('scientist')
  obj.status = json.get('status')
  obj.unassigned_checks = [ plainToResultCheck(o) for o in json['unassigned_checks'] ] if json.get('unassigned_checks') else []
  obj.unit_id = json.get('unit_id')
  obj.username = json.get('username')
  obj.flowcell = plainToIlluminaRun(json['flowcell']) if json.get('flowcell') else None
  obj.primer_ref = plainToPrimer(json['primer_ref']) if json.get('primer_ref') else None
  obj.run_ref = plainToRun(json['run_ref']) if json.get('run_ref') else None
  obj.run_unit = plainToRunUnit(json['run_unit']) if json.get('run_unit') else None
  obj.sequenced_samples = [ plainToSequencedSample(o) for o in json['sequenced_samples'] ] if json.get('sequenced_samples') else []

  obj.objects = json.get('objects', {})
  return obj

def serializeLane(obj: Lane) -> dict:
  json = {}
  json['comments'] = obj.comments
  json['conc'] = obj.conc
  json['discount'] = obj.discount
  json['group'] = obj.group
  json['invoice_status'] = obj.invoice_status
  json['is_saved'] = obj.is_saved
  if obj.lane_checks is not None:
    json['lane_checks'] = [ serializeResultCheck(o) for o in obj.lane_checks ]
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['needs_demultiplexing'] = obj.needs_demultiplexing
  json['num'] = obj.num
  json['phix'] = obj.phix
  json['primer'] = obj.primer
  json['run_id'] = obj.run_id
  json['sample_fields'] = serializeSampleFields(obj.sample_fields) if obj.sample_fields is not None else None
  json['sampnum'] = obj.sampnum
  json['scientist'] = obj.scientist
  json['status'] = obj.status
  if obj.unassigned_checks is not None:
    json['unassigned_checks'] = [ serializeResultCheck(o) for o in obj.unassigned_checks ]
  json['unit_id'] = obj.unit_id
  json['username'] = obj.username
  json['flowcell'] = serializeIlluminaRun(obj.flowcell) if obj.flowcell is not None else None
  json['primer_ref'] = serializePrimer(obj.primer_ref) if obj.primer_ref is not None else None
  json['run_ref'] = serializeRun(obj.run_ref) if obj.run_ref is not None else None
  json['run_unit'] = serializeRunUnit(obj.run_unit) if obj.run_unit is not None else None
  if obj.sequenced_samples is not None:
    json['sequenced_samples'] = [ serializeSequencedSample(o) for o in obj.sequenced_samples ]

  return json


@dataclass
class Lane:
  comments: typing.Optional[str] = None
  conc: typing.Optional[typing.Any] = None
  discount: typing.Optional[typing.Union[int, float]] = None
  group: typing.Optional[typing.Any] = None
  invoice_status: typing.Optional[str] = None
  is_saved: typing.Optional[bool] = None
  lane_checks: list[ResultCheck]=field(default_factory=list)
  last_change: typing.Optional[datetime] = None
  needs_demultiplexing: typing.Optional[bool] = None
  num: typing.Optional[str] = None
  phix: typing.Optional[typing.Union[int, float]] = None
  primer: typing.Optional[str] = None
  run_id: typing.Optional[typing.Union[int, float]] = None
  sample_fields: typing.Optional[SampleFields] = None
  sampnum: typing.Optional[typing.Union[int, float]] = None
  scientist: typing.Optional[typing.Any] = None
  status: typing.Optional[str] = None
  unassigned_checks: list[ResultCheck]=field(default_factory=list)
  unit_id: typing.Optional[typing.Union[int, float]] = None
  username: typing.Optional[str] = None

  
  flowcell: typing.Optional[IlluminaRun] = None
  primer_ref: typing.Optional[Primer] = None
  run_ref: typing.Optional[Run] = None
  run_unit: typing.Optional[RunUnit] = None
  sequenced_samples: list[SequencedSample] = field(default_factory=list)

  objects: typing.Any = None

# ---

def plainToMachine(json: dict) -> Machine:
  obj = Machine()
  obj.active = bool(json.get('active'))
  obj.celltypes = [ plainToCelltype(o) for o in json['celltypes'] ] if json.get('celltypes') else []
  obj.description = json.get('description')
  obj.model = json.get('model')
  obj.name = json.get('name')
  obj.platform = json.get('platform')
  obj.readmodes = [ plainToReadmode(o) for o in json['readmodes'] ] if json.get('readmodes') else []
  obj.run_folder = json.get('run_folder')
  obj.vendor_id = json.get('vendor_id')
  obj.platform_ref = plainToPlatform(json['platform_ref']) if json.get('platform_ref') else None

  return obj

def serializeMachine(obj: Machine) -> dict:
  json = {}
  json['active'] = obj.active
  if obj.celltypes is not None:
    json['celltypes'] = [ serializeCelltype(o) for o in obj.celltypes ]
  json['description'] = obj.description
  json['model'] = obj.model
  json['name'] = obj.name
  json['platform'] = obj.platform
  if obj.readmodes is not None:
    json['readmodes'] = [ serializeReadmode(o) for o in obj.readmodes ]
  json['run_folder'] = obj.run_folder
  json['vendor_id'] = obj.vendor_id
  json['platform_ref'] = serializePlatform(obj.platform_ref) if obj.platform_ref is not None else None

  return json


@dataclass
class Machine:
  active: typing.Optional[bool] = None
  celltypes: list[Celltype]=field(default_factory=list)
  description: typing.Optional[str] = None
  model: typing.Optional[str] = None
  name: typing.Optional[str] = None
  platform: typing.Optional[str] = None
  readmodes: list[Readmode]=field(default_factory=list)
  run_folder: typing.Optional[str] = None
  vendor_id: typing.Optional[str] = None

  
  platform_ref: typing.Optional[Platform] = None


# ---

def plainToMultiplex(json: dict) -> Multiplex:
  obj = Multiplex()
  obj._imp_storage = bool(json.get('_imp_storage'))
  obj.adaptor_type = json.get('adaptor_type')
  obj.description = json.get('description')
  obj.group = json.get('group')
  obj.group_id = json.get('group_id')
  obj.id = json.get('id')
  obj.lab_count = json.get('lab_count')
  obj.lab_steps = [ plainToLabStep(o) for o in json['lab_steps'] ] if json.get('lab_steps') else []
  obj.measurement_count = json.get('measurement_count')
  obj.notes_count = json.get('notes_count')
  obj.obj_id = json.get('obj_id')
  obj.obj_type = json.get('obj_type')
  obj.platform = json.get('platform')
  obj.pooled = bool(json.get('pooled'))
  obj.received = datetime.fromisoformat(json.get('received', '')) if json.get('received') else None
  obj.request_count = json.get('request_count')
  obj.sampcount = json.get('sampcount')
  obj.sample_fields = plainToSampleFields(json['sample_fields']) if json.get('sample_fields') else None
  obj.scientist = json.get('scientist')
  obj.scientist_id = json.get('scientist_id')
  obj.sequencing_count = json.get('sequencing_count')
  obj.adaptor_type_ref = plainToAdaptorType(json['adaptor_type_ref']) if json.get('adaptor_type_ref') else None
  obj.data_entries = [ plainToDataEntry(o) for o in json['data_entries'] ] if json.get('data_entries') else []
  obj.group_ref = plainToGroup(json['group_ref']) if json.get('group_ref') else None
  obj.multi_data_entries = [ plainToDataEntry(o) for o in json['multi_data_entries'] ] if json.get('multi_data_entries') else []
  obj.multiplex_samples = [ plainToMultiplexSample(o) for o in json['multiplex_samples'] ] if json.get('multiplex_samples') else []
  obj.notes = [ plainToNote(o) for o in json['notes'] ] if json.get('notes') else []
  obj.platform_ref = plainToPlatform(json['platform_ref']) if json.get('platform_ref') else None
  obj.preparation_type_ref = plainToPreparationType(json['preparation_type_ref']) if json.get('preparation_type_ref') else None
  obj.request_lanes = [ plainToRequestLane(o) for o in json['request_lanes'] ] if json.get('request_lanes') else []
  obj.scientist_ref = plainToScientist(json['scientist_ref']) if json.get('scientist_ref') else None
  obj.versions = [ plainToObjectVersion(o) for o in json['versions'] ] if json.get('versions') else []

  return obj

def serializeMultiplex(obj: Multiplex) -> dict:
  json = {}
  json['_imp_storage'] = obj._imp_storage
  json['adaptor_type'] = obj.adaptor_type
  json['description'] = obj.description
  json['group'] = obj.group
  json['group_id'] = obj.group_id
  json['id'] = obj.id
  json['lab_count'] = obj.lab_count
  if obj.lab_steps is not None:
    json['lab_steps'] = [ serializeLabStep(o) for o in obj.lab_steps ]
  json['measurement_count'] = obj.measurement_count
  json['notes_count'] = obj.notes_count
  json['obj_id'] = obj.obj_id
  json['obj_type'] = obj.obj_type
  json['platform'] = obj.platform
  json['pooled'] = obj.pooled
  json['received'] = obj.received.isoformat() if obj.received else None
  json['request_count'] = obj.request_count
  json['sampcount'] = obj.sampcount
  json['sample_fields'] = serializeSampleFields(obj.sample_fields) if obj.sample_fields is not None else None
  json['scientist'] = obj.scientist
  json['scientist_id'] = obj.scientist_id
  json['sequencing_count'] = obj.sequencing_count
  json['adaptor_type_ref'] = serializeAdaptorType(obj.adaptor_type_ref) if obj.adaptor_type_ref is not None else None
  if obj.data_entries is not None:
    json['data_entries'] = [ serializeDataEntry(o) for o in obj.data_entries ]
  json['group_ref'] = serializeGroup(obj.group_ref) if obj.group_ref is not None else None
  if obj.multi_data_entries is not None:
    json['multi_data_entries'] = [ serializeDataEntry(o) for o in obj.multi_data_entries ]
  if obj.multiplex_samples is not None:
    json['multiplex_samples'] = [ serializeMultiplexSample(o) for o in obj.multiplex_samples ]
  if obj.notes is not None:
    json['notes'] = [ serializeNote(o) for o in obj.notes ]
  json['platform_ref'] = serializePlatform(obj.platform_ref) if obj.platform_ref is not None else None
  json['preparation_type_ref'] = serializePreparationType(obj.preparation_type_ref) if obj.preparation_type_ref is not None else None
  if obj.request_lanes is not None:
    json['request_lanes'] = [ serializeRequestLane(o) for o in obj.request_lanes ]
  json['scientist_ref'] = serializeScientist(obj.scientist_ref) if obj.scientist_ref is not None else None
  if obj.versions is not None:
    json['versions'] = [ serializeObjectVersion(o) for o in obj.versions ]

  return json


@dataclass
class Multiplex:
  _imp_storage: typing.Optional[bool] = None
  adaptor_type: typing.Optional[str] = None
  description: typing.Optional[str] = None
  group: typing.Optional[typing.Any] = None
  group_id: typing.Optional[typing.Union[int, float]] = None
  id: typing.Optional[typing.Union[int, float]] = None
  lab_count: typing.Optional[typing.Union[int, float]] = None
  lab_steps: list[LabStep]=field(default_factory=list)
  measurement_count: typing.Optional[typing.Union[int, float]] = None
  notes_count: typing.Optional[typing.Union[int, float]] = None
  obj_id: typing.Optional[typing.Union[int, float]] = None
  obj_type: typing.Optional[str] = None
  platform: typing.Optional[str] = None
  pooled: typing.Optional[bool] = None
  received: typing.Optional[datetime] = None
  request_count: typing.Optional[typing.Union[int, float]] = None
  sampcount: typing.Optional[typing.Union[int, float]] = None
  sample_fields: typing.Optional[SampleFields] = None
  scientist: typing.Optional[typing.Any] = None
  scientist_id: typing.Optional[typing.Union[int, float]] = None
  sequencing_count: typing.Optional[typing.Union[int, float]] = None

  
  adaptor_type_ref: typing.Optional[AdaptorType] = None
  data_entries: list[DataEntry] = field(default_factory=list)
  group_ref: typing.Optional[Group] = None
  multi_data_entries: list[DataEntry] = field(default_factory=list)
  multiplex_samples: list[MultiplexSample] = field(default_factory=list)
  notes: list[Note] = field(default_factory=list)
  platform_ref: typing.Optional[Platform] = None
  preparation_type_ref: typing.Optional[PreparationType] = None
  request_lanes: list[RequestLane] = field(default_factory=list)
  scientist_ref: typing.Optional[Scientist] = None
  versions: list[ObjectVersion] = field(default_factory=list)


# ---

def plainToMultiplexSample(json: dict) -> MultiplexSample:
  obj = MultiplexSample()
  obj.multi_id = json.get('multi_id')
  obj.ratio = json.get('ratio')
  obj.sample_id = json.get('sample_id')
  obj.multi = plainToMultiplex(json['multi']) if json.get('multi') else None
  obj.sample = plainToSample(json['sample']) if json.get('sample') else None
  obj.versions = [ plainToObjectVersion(o) for o in json['versions'] ] if json.get('versions') else []

  return obj

def serializeMultiplexSample(obj: MultiplexSample) -> dict:
  json = {}
  json['multi_id'] = obj.multi_id
  json['ratio'] = obj.ratio
  json['sample_id'] = obj.sample_id
  json['multi'] = serializeMultiplex(obj.multi) if obj.multi is not None else None
  json['sample'] = serializeSample(obj.sample) if obj.sample is not None else None
  if obj.versions is not None:
    json['versions'] = [ serializeObjectVersion(o) for o in obj.versions ]

  return json


@dataclass
class MultiplexSample:
  multi_id: typing.Optional[typing.Union[int, float]] = None
  ratio: typing.Optional[typing.Union[int, float]] = None
  sample_id: typing.Optional[typing.Union[int, float]] = None

  
  multi: typing.Optional[Multiplex] = None
  sample: typing.Optional[Sample] = None
  versions: list[ObjectVersion] = field(default_factory=list)


# ---

def plainToNanostat(json: dict) -> Nanostat:
  obj = Nanostat()
  obj.active_channels = json.get('active_channels')
  obj.barcode = json.get('barcode')
  obj.basecalls = json.get('basecalls')
  obj.basepairs = json.get('basepairs')
  obj.bc_best_filter = json.get('bc_best_filter')
  obj.bc_best_unique_rate = json.get('bc_best_unique_rate')
  obj.bc_hit_rate = json.get('bc_hit_rate')
  obj.created = datetime.fromisoformat(json.get('created', '')) if json.get('created') else None
  obj.flowcell_unique_id = json.get('flowcell_unique_id')
  obj.id = json.get('id')
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.mean_gc = json.get('mean_gc')
  obj.mean_length = json.get('mean_length')
  obj.mean_qual = json.get('mean_qual')
  obj.median_length = json.get('median_length')
  obj.median_qual = json.get('median_qual')
  obj.n50_length = json.get('n50_length')
  obj.path = json.get('path')
  obj.q10_basepairs = json.get('q10_basepairs')
  obj.q10_reads = json.get('q10_reads')
  obj.q12_basepairs = json.get('q12_basepairs')
  obj.q12_reads = json.get('q12_reads')
  obj.q15_basepairs = json.get('q15_basepairs')
  obj.q15_reads = json.get('q15_reads')
  obj.q5_basepairs = json.get('q5_basepairs')
  obj.q5_reads = json.get('q5_reads')
  obj.q7_basepairs = json.get('q7_basepairs')
  obj.q7_reads = json.get('q7_reads')
  obj.reads = json.get('reads')
  obj.result_check_id = json.get('result_check_id')
  obj.run_id = json.get('run_id')
  obj.run_unique_id = json.get('run_unique_id')
  obj.unit_id = json.get('unit_id')
  obj.ont_flowcell_run = plainToOntFlowcellRun(json['ont_flowcell_run']) if json.get('ont_flowcell_run') else None
  obj.ont_run = plainToOntRun(json['ont_run']) if json.get('ont_run') else None
  obj.result_check = plainToResultCheck(json['result_check']) if json.get('result_check') else None
  obj.run = plainToRun(json['run']) if json.get('run') else None
  obj.run_unit = plainToRunUnit(json['run_unit']) if json.get('run_unit') else None

  return obj

def serializeNanostat(obj: Nanostat) -> dict:
  json = {}
  json['active_channels'] = obj.active_channels
  json['barcode'] = obj.barcode
  json['basecalls'] = obj.basecalls
  json['basepairs'] = obj.basepairs
  json['bc_best_filter'] = obj.bc_best_filter
  json['bc_best_unique_rate'] = obj.bc_best_unique_rate
  json['bc_hit_rate'] = obj.bc_hit_rate
  json['created'] = obj.created.isoformat() if obj.created else None
  json['flowcell_unique_id'] = obj.flowcell_unique_id
  json['id'] = obj.id
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['mean_gc'] = obj.mean_gc
  json['mean_length'] = obj.mean_length
  json['mean_qual'] = obj.mean_qual
  json['median_length'] = obj.median_length
  json['median_qual'] = obj.median_qual
  json['n50_length'] = obj.n50_length
  json['path'] = obj.path
  json['q10_basepairs'] = obj.q10_basepairs
  json['q10_reads'] = obj.q10_reads
  json['q12_basepairs'] = obj.q12_basepairs
  json['q12_reads'] = obj.q12_reads
  json['q15_basepairs'] = obj.q15_basepairs
  json['q15_reads'] = obj.q15_reads
  json['q5_basepairs'] = obj.q5_basepairs
  json['q5_reads'] = obj.q5_reads
  json['q7_basepairs'] = obj.q7_basepairs
  json['q7_reads'] = obj.q7_reads
  json['reads'] = obj.reads
  json['result_check_id'] = obj.result_check_id
  json['run_id'] = obj.run_id
  json['run_unique_id'] = obj.run_unique_id
  json['unit_id'] = obj.unit_id
  json['ont_flowcell_run'] = serializeOntFlowcellRun(obj.ont_flowcell_run) if obj.ont_flowcell_run is not None else None
  json['ont_run'] = serializeOntRun(obj.ont_run) if obj.ont_run is not None else None
  json['result_check'] = serializeResultCheck(obj.result_check) if obj.result_check is not None else None
  json['run'] = serializeRun(obj.run) if obj.run is not None else None
  json['run_unit'] = serializeRunUnit(obj.run_unit) if obj.run_unit is not None else None

  return json


@dataclass
class Nanostat:
  active_channels: typing.Optional[typing.Union[int, float]] = None
  barcode: typing.Optional[str] = None
  basecalls: typing.Optional[str] = None
  basepairs: typing.Optional[typing.Any] = None
  bc_best_filter: typing.Optional[str] = None
  bc_best_unique_rate: typing.Optional[typing.Any] = None
  bc_hit_rate: typing.Optional[typing.Any] = None
  created: typing.Optional[datetime] = None
  flowcell_unique_id: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  last_change: typing.Optional[datetime] = None
  mean_gc: typing.Optional[typing.Any] = None
  mean_length: typing.Optional[typing.Any] = None
  mean_qual: typing.Optional[typing.Any] = None
  median_length: typing.Optional[typing.Any] = None
  median_qual: typing.Optional[typing.Any] = None
  n50_length: typing.Optional[typing.Any] = None
  path: typing.Optional[str] = None
  q10_basepairs: typing.Optional[typing.Any] = None
  q10_reads: typing.Optional[typing.Any] = None
  q12_basepairs: typing.Optional[typing.Any] = None
  q12_reads: typing.Optional[typing.Any] = None
  q15_basepairs: typing.Optional[typing.Any] = None
  q15_reads: typing.Optional[typing.Any] = None
  q5_basepairs: typing.Optional[typing.Any] = None
  q5_reads: typing.Optional[typing.Any] = None
  q7_basepairs: typing.Optional[typing.Any] = None
  q7_reads: typing.Optional[typing.Any] = None
  reads: typing.Optional[typing.Any] = None
  result_check_id: typing.Optional[typing.Union[int, float]] = None
  run_id: typing.Optional[typing.Union[int, float]] = None
  run_unique_id: typing.Optional[str] = None
  unit_id: typing.Optional[typing.Union[int, float]] = None

  
  ont_flowcell_run: typing.Optional[OntFlowcellRun] = None
  ont_run: typing.Optional[OntRun] = None
  result_check: typing.Optional[ResultCheck] = None
  run: typing.Optional[Run] = None
  run_unit: typing.Optional[RunUnit] = None


# ---

def plainToNote(json: dict) -> Note:
  obj = Note()
  obj.comment_date = datetime.fromisoformat(json.get('comment_date', '')) if json.get('comment_date') else None
  obj.comment_text = json.get('comment_text')
  obj.flag = json.get('flag')
  obj.id = json.get('id')
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.last_change_username = json.get('last_change_username')
  obj.note_type = json.get('note_type')
  obj.notified = bool(json.get('notified'))
  obj.obj_id = json.get('obj_id')
  obj.obj_type = json.get('obj_type')
  obj.resolved = bool(json.get('resolved'))
  obj.username = json.get('username')
  obj.last_change_user_ref = plainToScientist(json['last_change_user_ref']) if json.get('last_change_user_ref') else None
  obj.multiplex = plainToMultiplex(json['multiplex']) if json.get('multiplex') else None
  obj.request = plainToRequest(json['request']) if json.get('request') else None
  obj.run = plainToRun(json['run']) if json.get('run') else None
  obj.sample = plainToSample(json['sample']) if json.get('sample') else None
  obj.scientist = plainToScientist(json['scientist']) if json.get('scientist') else None
  obj.user_ref = plainToScientist(json['user_ref']) if json.get('user_ref') else None

  return obj

def serializeNote(obj: Note) -> dict:
  json = {}
  json['comment_date'] = obj.comment_date.isoformat() if obj.comment_date else None
  json['comment_text'] = obj.comment_text
  json['flag'] = obj.flag
  json['id'] = obj.id
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['last_change_username'] = obj.last_change_username
  json['note_type'] = obj.note_type
  json['notified'] = obj.notified
  json['obj_id'] = obj.obj_id
  json['obj_type'] = obj.obj_type
  json['resolved'] = obj.resolved
  json['username'] = obj.username
  json['last_change_user_ref'] = serializeScientist(obj.last_change_user_ref) if obj.last_change_user_ref is not None else None
  json['multiplex'] = serializeMultiplex(obj.multiplex) if obj.multiplex is not None else None
  json['request'] = serializeRequest(obj.request) if obj.request is not None else None
  json['run'] = serializeRun(obj.run) if obj.run is not None else None
  json['sample'] = serializeSample(obj.sample) if obj.sample is not None else None
  json['scientist'] = serializeScientist(obj.scientist) if obj.scientist is not None else None
  json['user_ref'] = serializeScientist(obj.user_ref) if obj.user_ref is not None else None

  return json


@dataclass
class Note:
  comment_date: typing.Optional[datetime] = None
  comment_text: typing.Optional[str] = None
  flag: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  last_change: typing.Optional[datetime] = None
  last_change_username: typing.Optional[str] = None
  note_type: typing.Optional[str] = None
  notified: typing.Optional[bool] = None
  obj_id: typing.Optional[typing.Union[int, float]] = None
  obj_type: typing.Optional[str] = None
  resolved: typing.Optional[bool] = None
  username: typing.Optional[str] = None

  
  last_change_user_ref: typing.Optional[Scientist] = None
  multiplex: typing.Optional[Multiplex] = None
  request: typing.Optional[Request] = None
  run: typing.Optional[Run] = None
  sample: typing.Optional[Sample] = None
  scientist: typing.Optional[Scientist] = None
  user_ref: typing.Optional[Scientist] = None


# ---

def plainToNotification(json: dict) -> Notification:
  obj = Notification()
  obj.additional = json.get('additional')
  obj.attach_reqsheet = bool(json.get('attach_reqsheet'))
  obj.body = json.get('body')
  obj.cc_recipients = json.get('cc_recipients')
  obj.date = datetime.fromisoformat(json.get('date', '')) if json.get('date') else None
  obj.done = bool(json.get('done'))
  obj.grouped_with = json.get('grouped_with')
  obj.id = json.get('id')
  obj.message_type = json.get('message_type')
  obj.message_type_id = json.get('message_type_id')
  obj.obj_id = json.get('obj_id')
  obj.obj_type = json.get('obj_type')
  obj.parameters = json.get('parameters')
  obj.state = json.get('state')
  obj.subject = json.get('subject')
  obj.grouped_notifications = [ plainToNotification(o) for o in json['grouped_notifications'] ] if json.get('grouped_notifications') else []
  obj.grouped_with_ref = plainToNotification(json['grouped_with_ref']) if json.get('grouped_with_ref') else None
  obj.multiplex = plainToMultiplex(json['multiplex']) if json.get('multiplex') else None
  obj.request = plainToRequest(json['request']) if json.get('request') else None
  obj.request_lane = plainToRequestLane(json['request_lane']) if json.get('request_lane') else None
  obj.run = plainToRun(json['run']) if json.get('run') else None
  obj.run_unit = plainToRunUnit(json['run_unit']) if json.get('run_unit') else None
  obj.sample = plainToSample(json['sample']) if json.get('sample') else None
  obj.user = plainToScientist(json['user']) if json.get('user') else None

  return obj

def serializeNotification(obj: Notification) -> dict:
  json = {}
  json['additional'] = obj.additional
  json['attach_reqsheet'] = obj.attach_reqsheet
  json['body'] = obj.body
  json['cc_recipients'] = obj.cc_recipients
  json['date'] = obj.date.isoformat() if obj.date else None
  json['done'] = obj.done
  json['grouped_with'] = obj.grouped_with
  json['id'] = obj.id
  json['message_type'] = obj.message_type
  json['message_type_id'] = obj.message_type_id
  json['obj_id'] = obj.obj_id
  json['obj_type'] = obj.obj_type
  json['parameters'] = obj.parameters
  json['state'] = obj.state
  json['subject'] = obj.subject
  if obj.grouped_notifications is not None:
    json['grouped_notifications'] = [ serializeNotification(o) for o in obj.grouped_notifications ]
  json['grouped_with_ref'] = serializeNotification(obj.grouped_with_ref) if obj.grouped_with_ref is not None else None
  json['multiplex'] = serializeMultiplex(obj.multiplex) if obj.multiplex is not None else None
  json['request'] = serializeRequest(obj.request) if obj.request is not None else None
  json['request_lane'] = serializeRequestLane(obj.request_lane) if obj.request_lane is not None else None
  json['run'] = serializeRun(obj.run) if obj.run is not None else None
  json['run_unit'] = serializeRunUnit(obj.run_unit) if obj.run_unit is not None else None
  json['sample'] = serializeSample(obj.sample) if obj.sample is not None else None
  json['user'] = serializeScientist(obj.user) if obj.user is not None else None

  return json


@dataclass
class Notification:
  additional: typing.Optional[str] = None
  attach_reqsheet: typing.Optional[bool] = None
  body: typing.Optional[str] = None
  cc_recipients: typing.Optional[str] = None
  date: typing.Optional[datetime] = None
  done: typing.Optional[bool] = None
  grouped_with: typing.Optional[typing.Union[int, float]] = None
  id: typing.Optional[typing.Union[int, float]] = None
  message_type: typing.Optional[str] = None
  message_type_id: typing.Optional[typing.Union[int, float]] = None
  obj_id: typing.Optional[str] = None
  obj_type: typing.Optional[str] = None
  parameters: typing.Optional[dict] = None
  state: typing.Optional[str] = None
  subject: typing.Optional[str] = None

  
  grouped_notifications: list[Notification] = field(default_factory=list)
  grouped_with_ref: typing.Optional[Notification] = None
  multiplex: typing.Optional[Multiplex] = None
  request: typing.Optional[Request] = None
  request_lane: typing.Optional[RequestLane] = None
  run: typing.Optional[Run] = None
  run_unit: typing.Optional[RunUnit] = None
  sample: typing.Optional[Sample] = None
  user: typing.Optional[Scientist] = None


# ---

def plainToObjectVersion(json: dict) -> ObjectVersion:
  obj = ObjectVersion()
  obj.date = datetime.fromisoformat(json.get('date', '')) if json.get('date') else None
  obj.id = json.get('id')
  obj.obj_data = json.get('obj_data')
  obj.obj_id = json.get('obj_id')
  obj.obj_type = json.get('obj_type')
  obj.op = json.get('op')
  obj.username = json.get('username')
  obj.version = json.get('version')
  obj.scientist_ref = plainToScientist(json['scientist_ref']) if json.get('scientist_ref') else None

  return obj

def serializeObjectVersion(obj: ObjectVersion) -> dict:
  json = {}
  json['date'] = obj.date.isoformat() if obj.date else None
  json['id'] = obj.id
  json['obj_data'] = obj.obj_data
  json['obj_id'] = obj.obj_id
  json['obj_type'] = obj.obj_type
  json['op'] = obj.op
  json['username'] = obj.username
  json['version'] = obj.version
  json['scientist_ref'] = serializeScientist(obj.scientist_ref) if obj.scientist_ref is not None else None

  return json


@dataclass
class ObjectVersion:
  date: typing.Optional[datetime] = None
  id: typing.Optional[typing.Union[int, float]] = None
  obj_data: typing.Optional[dict] = None
  obj_id: typing.Optional[typing.Union[int, float]] = None
  obj_type: typing.Optional[str] = None
  op: typing.Optional[str] = None
  username: typing.Optional[str] = None
  version: typing.Optional[typing.Union[int, float]] = None

  
  scientist_ref: typing.Optional[Scientist] = None


# ---

def plainToOntFlowcellRun(json: dict) -> OntFlowcellRun:
  obj = OntFlowcellRun()
  obj.basecalled = datetime.fromisoformat(json.get('basecalled', '')) if json.get('basecalled') else None
  obj.basecaller = json.get('basecaller')
  obj.basecalls = json.get('basecalls')
  obj.comments = json.get('comments')
  obj.conc = json.get('conc')
  obj.copied = datetime.fromisoformat(json.get('copied', '')) if json.get('copied') else None
  obj.datafiles_created = datetime.fromisoformat(json.get('datafiles_created', '')) if json.get('datafiles_created') else None
  obj.datafiles_hash = json.get('datafiles_hash')
  obj.datafiles_id = json.get('datafiles_id')
  obj.datafiles_link = json.get('datafiles_link')
  obj.datafiles_path = json.get('datafiles_path')
  obj.datafiles_size = json.get('datafiles_size')
  obj.datafiles_url = json.get('datafiles_url')
  obj.demultiplexed = datetime.fromisoformat(json.get('demultiplexed', '')) if json.get('demultiplexed') else None
  obj.discount = json.get('discount')
  obj.experiment_name = json.get('experiment_name')
  obj.fastq_path = json.get('fastq_path')
  obj.group = json.get('group')
  obj.invoice_status = json.get('invoice_status')
  obj.is_saved = bool(json.get('is_saved'))
  obj.kit = json.get('kit')
  obj.lane_checks = [ plainToResultCheck(o) for o in json['lane_checks'] ] if json.get('lane_checks') else []
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.loading = json.get('loading')
  obj.multiplexing = bool(json.get('multiplexing'))
  obj.needs_demultiplexing = bool(json.get('needs_demultiplexing'))
  obj.output_path = json.get('output_path')
  obj.processed = datetime.fromisoformat(json.get('processed', '')) if json.get('processed') else None
  obj.report_url = json.get('report_url')
  obj.run_id = json.get('run_id')
  obj.run_length = json.get('run_length')
  obj.sample_fields = plainToSampleFields(json['sample_fields']) if json.get('sample_fields') else None
  obj.sample_type = json.get('sample_type')
  obj.sampnum = json.get('sampnum')
  obj.scientist = json.get('scientist')
  obj.software_version = json.get('software_version')
  obj.start_time = datetime.fromisoformat(json.get('start_time', '')) if json.get('start_time') else None
  obj.status = json.get('status')
  obj.unassigned_checks = [ plainToResultCheck(o) for o in json['unassigned_checks'] ] if json.get('unassigned_checks') else []
  obj.unique_id = json.get('unique_id')
  obj.unit_id = json.get('unit_id')
  obj.username = json.get('username')
  obj.flowcell = plainToOntRun(json['flowcell']) if json.get('flowcell') else None
  obj.run_ref = plainToRun(json['run_ref']) if json.get('run_ref') else None
  obj.run_unit = plainToRunUnit(json['run_unit']) if json.get('run_unit') else None
  obj.sequenced_samples = [ plainToSequencedSample(o) for o in json['sequenced_samples'] ] if json.get('sequenced_samples') else []

  obj.objects = json.get('objects', {})
  return obj

def serializeOntFlowcellRun(obj: OntFlowcellRun) -> dict:
  json = {}
  json['basecalled'] = obj.basecalled.isoformat() if obj.basecalled else None
  json['basecaller'] = obj.basecaller
  json['basecalls'] = obj.basecalls
  json['comments'] = obj.comments
  json['conc'] = obj.conc
  json['copied'] = obj.copied.isoformat() if obj.copied else None
  json['datafiles_created'] = obj.datafiles_created.isoformat() if obj.datafiles_created else None
  json['datafiles_hash'] = obj.datafiles_hash
  json['datafiles_id'] = obj.datafiles_id
  json['datafiles_link'] = obj.datafiles_link
  json['datafiles_path'] = obj.datafiles_path
  json['datafiles_size'] = obj.datafiles_size
  json['datafiles_url'] = obj.datafiles_url
  json['demultiplexed'] = obj.demultiplexed.isoformat() if obj.demultiplexed else None
  json['discount'] = obj.discount
  json['experiment_name'] = obj.experiment_name
  json['fastq_path'] = obj.fastq_path
  json['group'] = obj.group
  json['invoice_status'] = obj.invoice_status
  json['is_saved'] = obj.is_saved
  json['kit'] = obj.kit
  if obj.lane_checks is not None:
    json['lane_checks'] = [ serializeResultCheck(o) for o in obj.lane_checks ]
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['loading'] = obj.loading
  json['multiplexing'] = obj.multiplexing
  json['needs_demultiplexing'] = obj.needs_demultiplexing
  json['output_path'] = obj.output_path
  json['processed'] = obj.processed.isoformat() if obj.processed else None
  json['report_url'] = obj.report_url
  json['run_id'] = obj.run_id
  json['run_length'] = obj.run_length
  json['sample_fields'] = serializeSampleFields(obj.sample_fields) if obj.sample_fields is not None else None
  json['sample_type'] = obj.sample_type
  json['sampnum'] = obj.sampnum
  json['scientist'] = obj.scientist
  json['software_version'] = obj.software_version
  json['start_time'] = obj.start_time.isoformat() if obj.start_time else None
  json['status'] = obj.status
  if obj.unassigned_checks is not None:
    json['unassigned_checks'] = [ serializeResultCheck(o) for o in obj.unassigned_checks ]
  json['unique_id'] = obj.unique_id
  json['unit_id'] = obj.unit_id
  json['username'] = obj.username
  json['flowcell'] = serializeOntRun(obj.flowcell) if obj.flowcell is not None else None
  json['run_ref'] = serializeRun(obj.run_ref) if obj.run_ref is not None else None
  json['run_unit'] = serializeRunUnit(obj.run_unit) if obj.run_unit is not None else None
  if obj.sequenced_samples is not None:
    json['sequenced_samples'] = [ serializeSequencedSample(o) for o in obj.sequenced_samples ]

  return json


@dataclass
class OntFlowcellRun:
  basecalled: typing.Optional[datetime] = None
  basecaller: typing.Optional[str] = None
  basecalls: typing.Optional[str] = None
  comments: typing.Optional[str] = None
  conc: typing.Optional[typing.Any] = None
  copied: typing.Optional[datetime] = None
  datafiles_created: typing.Optional[datetime] = None
  datafiles_hash: typing.Optional[str] = None
  datafiles_id: typing.Optional[typing.Union[int, float]] = None
  datafiles_link: typing.Optional[str] = None
  datafiles_path: typing.Optional[str] = None
  datafiles_size: typing.Optional[typing.Any] = None
  datafiles_url: typing.Optional[str] = None
  demultiplexed: typing.Optional[datetime] = None
  discount: typing.Optional[typing.Union[int, float]] = None
  experiment_name: typing.Optional[str] = None
  fastq_path: typing.Optional[str] = None
  group: typing.Optional[typing.Any] = None
  invoice_status: typing.Optional[str] = None
  is_saved: typing.Optional[bool] = None
  kit: typing.Optional[str] = None
  lane_checks: list[ResultCheck]=field(default_factory=list)
  last_change: typing.Optional[datetime] = None
  loading: typing.Optional[typing.Union[int, float]] = None
  multiplexing: typing.Optional[bool] = None
  needs_demultiplexing: typing.Optional[bool] = None
  output_path: typing.Optional[str] = None
  processed: typing.Optional[datetime] = None
  report_url: typing.Optional[str] = None
  run_id: typing.Optional[typing.Union[int, float]] = None
  run_length: typing.Optional[typing.Union[int, float]] = None
  sample_fields: typing.Optional[SampleFields] = None
  sample_type: typing.Optional[str] = None
  sampnum: typing.Optional[typing.Union[int, float]] = None
  scientist: typing.Optional[typing.Any] = None
  software_version: typing.Optional[str] = None
  start_time: typing.Optional[datetime] = None
  status: typing.Optional[str] = None
  unassigned_checks: list[ResultCheck]=field(default_factory=list)
  unique_id: typing.Optional[str] = None
  unit_id: typing.Optional[typing.Union[int, float]] = None
  username: typing.Optional[str] = None

  
  flowcell: typing.Optional[OntRun] = None
  run_ref: typing.Optional[Run] = None
  run_unit: typing.Optional[RunUnit] = None
  sequenced_samples: list[SequencedSample] = field(default_factory=list)

  objects: typing.Any = None

# ---

def plainToOntRun(json: dict) -> OntRun:
  obj = OntRun()
  obj.comments = json.get('comments')
  obj.description = json.get('description')
  obj.device_id = json.get('device_id')
  obj.draft = bool(json.get('draft'))
  obj.flowcell_type = json.get('flowcell_type')
  obj.group = json.get('group')
  obj.group_id = json.get('group_id')
  obj.id = json.get('id')
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.machine = json.get('machine')
  obj.mux_scan_pores = json.get('mux_scan_pores')
  obj.name = json.get('name')
  obj.obj_type = json.get('obj_type')
  obj.platform = json.get('platform')
  obj.preparation_date = datetime.fromisoformat(json.get('preparation_date', '')) if json.get('preparation_date') else None
  obj.qc_pores = json.get('qc_pores')
  obj.readmode = plainToReadmode(json['readmode']) if json.get('readmode') else None
  obj.readmode_id = json.get('readmode_id')
  obj.report_url = json.get('report_url')
  obj.run_folder = json.get('run_folder')
  obj.run_id = json.get('run_id')
  obj.scientist = json.get('scientist')
  obj.scientist_id = json.get('scientist_id')
  obj.selfservice = bool(json.get('selfservice'))
  obj.sequencing_date = datetime.fromisoformat(json.get('sequencing_date', '')) if json.get('sequencing_date') else None
  obj.status = json.get('status')
  obj.unique_id = json.get('unique_id')
  obj.username = json.get('username')
  obj.vendor_id = json.get('vendor_id')
  obj.inventory_changes = [ plainToInventoryChange(o) for o in json['inventory_changes'] ] if json.get('inventory_changes') else []
  obj.ont_flowcell_runs = [ plainToOntFlowcellRun(o) for o in json['ont_flowcell_runs'] ] if json.get('ont_flowcell_runs') else []
  obj.run = plainToRun(json['run']) if json.get('run') else None

  return obj

def serializeOntRun(obj: OntRun) -> dict:
  json = {}
  json['comments'] = obj.comments
  json['description'] = obj.description
  json['device_id'] = obj.device_id
  json['draft'] = obj.draft
  json['flowcell_type'] = obj.flowcell_type
  json['group'] = obj.group
  json['group_id'] = obj.group_id
  json['id'] = obj.id
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['machine'] = obj.machine
  json['mux_scan_pores'] = obj.mux_scan_pores
  json['name'] = obj.name
  json['obj_type'] = obj.obj_type
  json['platform'] = obj.platform
  json['preparation_date'] = obj.preparation_date.isoformat() if obj.preparation_date else None
  json['qc_pores'] = obj.qc_pores
  json['readmode'] = serializeReadmode(obj.readmode) if obj.readmode is not None else None
  json['readmode_id'] = obj.readmode_id
  json['report_url'] = obj.report_url
  json['run_folder'] = obj.run_folder
  json['run_id'] = obj.run_id
  json['scientist'] = obj.scientist
  json['scientist_id'] = obj.scientist_id
  json['selfservice'] = obj.selfservice
  json['sequencing_date'] = obj.sequencing_date.isoformat() if obj.sequencing_date else None
  json['status'] = obj.status
  json['unique_id'] = obj.unique_id
  json['username'] = obj.username
  json['vendor_id'] = obj.vendor_id
  if obj.inventory_changes is not None:
    json['inventory_changes'] = [ serializeInventoryChange(o) for o in obj.inventory_changes ]
  if obj.ont_flowcell_runs is not None:
    json['ont_flowcell_runs'] = [ serializeOntFlowcellRun(o) for o in obj.ont_flowcell_runs ]
  json['run'] = serializeRun(obj.run) if obj.run is not None else None

  return json


@dataclass
class OntRun:
  comments: typing.Optional[str] = None
  description: typing.Optional[str] = None
  device_id: typing.Optional[str] = None
  draft: typing.Optional[bool] = None
  flowcell_type: typing.Optional[str] = None
  group: typing.Optional[typing.Any] = None
  group_id: typing.Optional[typing.Union[int, float]] = None
  id: typing.Optional[typing.Union[int, float]] = None
  last_change: typing.Optional[datetime] = None
  machine: typing.Optional[str] = None
  mux_scan_pores: typing.Optional[typing.Union[int, float]] = None
  name: typing.Optional[str] = None
  obj_type: typing.Optional[str] = None
  platform: typing.Optional[str] = None
  preparation_date: typing.Optional[datetime] = None
  qc_pores: typing.Optional[typing.Union[int, float]] = None
  readmode: typing.Optional[Readmode] = None
  readmode_id: typing.Optional[typing.Union[int, float]] = None
  report_url: typing.Optional[str] = None
  run_folder: typing.Optional[str] = None
  run_id: typing.Optional[typing.Union[int, float]] = None
  scientist: typing.Optional[typing.Any] = None
  scientist_id: typing.Optional[typing.Union[int, float]] = None
  selfservice: typing.Optional[bool] = None
  sequencing_date: typing.Optional[datetime] = None
  status: typing.Optional[str] = None
  unique_id: typing.Optional[str] = None
  username: typing.Optional[str] = None
  vendor_id: typing.Optional[str] = None

  
  inventory_changes: list[InventoryChange] = field(default_factory=list)
  ont_flowcell_runs: list[OntFlowcellRun] = field(default_factory=list)
  run: typing.Optional[Run] = None


# ---

def plainToPacbioRun(json: dict) -> PacbioRun:
  obj = PacbioRun()
  obj.comments = json.get('comments')
  obj.description = json.get('description')
  obj.draft = bool(json.get('draft'))
  obj.group = json.get('group')
  obj.group_id = json.get('group_id')
  obj.id = json.get('id')
  obj.instrument_sw_version = json.get('instrument_sw_version')
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.machine = json.get('machine')
  obj.name = json.get('name')
  obj.obj_type = json.get('obj_type')
  obj.platform = json.get('platform')
  obj.preparation_date = datetime.fromisoformat(json.get('preparation_date', '')) if json.get('preparation_date') else None
  obj.primary_analysis_version = json.get('primary_analysis_version')
  obj.readmode = plainToReadmode(json['readmode']) if json.get('readmode') else None
  obj.readmode_id = json.get('readmode_id')
  obj.report_url = json.get('report_url')
  obj.run_folder = json.get('run_folder')
  obj.run_id = json.get('run_id')
  obj.scientist = json.get('scientist')
  obj.scientist_id = json.get('scientist_id')
  obj.selfservice = bool(json.get('selfservice'))
  obj.sequencing_date = datetime.fromisoformat(json.get('sequencing_date', '')) if json.get('sequencing_date') else None
  obj.status = json.get('status')
  obj.unique_id = json.get('unique_id')
  obj.username = json.get('username')
  obj.vendor_id = json.get('vendor_id')
  obj.inventory_changes = [ plainToInventoryChange(o) for o in json['inventory_changes'] ] if json.get('inventory_changes') else []
  obj.run = plainToRun(json['run']) if json.get('run') else None
  obj.smrtcells = [ plainToSmrtCell(o) for o in json['smrtcells'] ] if json.get('smrtcells') else []
  obj.subreadstats = [ plainToSubreadstat(o) for o in json['subreadstats'] ] if json.get('subreadstats') else []

  return obj

def serializePacbioRun(obj: PacbioRun) -> dict:
  json = {}
  json['comments'] = obj.comments
  json['description'] = obj.description
  json['draft'] = obj.draft
  json['group'] = obj.group
  json['group_id'] = obj.group_id
  json['id'] = obj.id
  json['instrument_sw_version'] = obj.instrument_sw_version
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['machine'] = obj.machine
  json['name'] = obj.name
  json['obj_type'] = obj.obj_type
  json['platform'] = obj.platform
  json['preparation_date'] = obj.preparation_date.isoformat() if obj.preparation_date else None
  json['primary_analysis_version'] = obj.primary_analysis_version
  json['readmode'] = serializeReadmode(obj.readmode) if obj.readmode is not None else None
  json['readmode_id'] = obj.readmode_id
  json['report_url'] = obj.report_url
  json['run_folder'] = obj.run_folder
  json['run_id'] = obj.run_id
  json['scientist'] = obj.scientist
  json['scientist_id'] = obj.scientist_id
  json['selfservice'] = obj.selfservice
  json['sequencing_date'] = obj.sequencing_date.isoformat() if obj.sequencing_date else None
  json['status'] = obj.status
  json['unique_id'] = obj.unique_id
  json['username'] = obj.username
  json['vendor_id'] = obj.vendor_id
  if obj.inventory_changes is not None:
    json['inventory_changes'] = [ serializeInventoryChange(o) for o in obj.inventory_changes ]
  json['run'] = serializeRun(obj.run) if obj.run is not None else None
  if obj.smrtcells is not None:
    json['smrtcells'] = [ serializeSmrtCell(o) for o in obj.smrtcells ]
  if obj.subreadstats is not None:
    json['subreadstats'] = [ serializeSubreadstat(o) for o in obj.subreadstats ]

  return json


@dataclass
class PacbioRun:
  comments: typing.Optional[str] = None
  description: typing.Optional[str] = None
  draft: typing.Optional[bool] = None
  group: typing.Optional[typing.Any] = None
  group_id: typing.Optional[typing.Union[int, float]] = None
  id: typing.Optional[typing.Union[int, float]] = None
  instrument_sw_version: typing.Optional[str] = None
  last_change: typing.Optional[datetime] = None
  machine: typing.Optional[str] = None
  name: typing.Optional[str] = None
  obj_type: typing.Optional[str] = None
  platform: typing.Optional[str] = None
  preparation_date: typing.Optional[datetime] = None
  primary_analysis_version: typing.Optional[str] = None
  readmode: typing.Optional[Readmode] = None
  readmode_id: typing.Optional[typing.Union[int, float]] = None
  report_url: typing.Optional[str] = None
  run_folder: typing.Optional[str] = None
  run_id: typing.Optional[typing.Union[int, float]] = None
  scientist: typing.Optional[typing.Any] = None
  scientist_id: typing.Optional[typing.Union[int, float]] = None
  selfservice: typing.Optional[bool] = None
  sequencing_date: typing.Optional[datetime] = None
  status: typing.Optional[str] = None
  unique_id: typing.Optional[str] = None
  username: typing.Optional[str] = None
  vendor_id: typing.Optional[str] = None

  
  inventory_changes: list[InventoryChange] = field(default_factory=list)
  run: typing.Optional[Run] = None
  smrtcells: list[SmrtCell] = field(default_factory=list)
  subreadstats: list[Subreadstat] = field(default_factory=list)


# ---

def plainToPlatform(json: dict) -> Platform:
  obj = Platform()
  obj.description = json.get('description')
  obj.name = json.get('name')
  obj.readmodes = [ plainToReadmode(o) for o in json['readmodes'] ] if json.get('readmodes') else []
  obj.vendor = json.get('vendor')
  obj.adaptor_types = [ plainToAdaptorType(o) for o in json['adaptor_types'] ] if json.get('adaptor_types') else []
  obj.forms = [ plainToForm(o) for o in json['forms'] ] if json.get('forms') else []
  obj.machines = [ plainToMachine(o) for o in json['machines'] ] if json.get('machines') else []
  obj.preparation_types = [ plainToPreparationType(o) for o in json['preparation_types'] ] if json.get('preparation_types') else []
  obj.primers = [ plainToPrimer(o) for o in json['primers'] ] if json.get('primers') else []
  obj.requests = [ plainToRequest(o) for o in json['requests'] ] if json.get('requests') else []
  obj.samples = [ plainToSample(o) for o in json['samples'] ] if json.get('samples') else []

  return obj

def serializePlatform(obj: Platform) -> dict:
  json = {}
  json['description'] = obj.description
  json['name'] = obj.name
  if obj.readmodes is not None:
    json['readmodes'] = [ serializeReadmode(o) for o in obj.readmodes ]
  json['vendor'] = obj.vendor
  if obj.adaptor_types is not None:
    json['adaptor_types'] = [ serializeAdaptorType(o) for o in obj.adaptor_types ]
  if obj.forms is not None:
    json['forms'] = [ serializeForm(o) for o in obj.forms ]
  if obj.machines is not None:
    json['machines'] = [ serializeMachine(o) for o in obj.machines ]
  if obj.preparation_types is not None:
    json['preparation_types'] = [ serializePreparationType(o) for o in obj.preparation_types ]
  if obj.primers is not None:
    json['primers'] = [ serializePrimer(o) for o in obj.primers ]
  if obj.requests is not None:
    json['requests'] = [ serializeRequest(o) for o in obj.requests ]
  if obj.samples is not None:
    json['samples'] = [ serializeSample(o) for o in obj.samples ]

  return json


@dataclass
class Platform:
  description: typing.Optional[str] = None
  name: typing.Optional[str] = None
  readmodes: list[Readmode]=field(default_factory=list)
  vendor: typing.Optional[str] = None

  
  adaptor_types: list[AdaptorType] = field(default_factory=list)
  forms: list[Form] = field(default_factory=list)
  machines: list[Machine] = field(default_factory=list)
  preparation_types: list[PreparationType] = field(default_factory=list)
  primers: list[Primer] = field(default_factory=list)
  requests: list[Request] = field(default_factory=list)
  samples: list[Sample] = field(default_factory=list)


# ---

def plainToPreparationKit(json: dict) -> PreparationKit:
  obj = PreparationKit()
  obj.adaptor_type = json.get('adaptor_type')
  obj.additional_qc_item_name = json.get('additional_qc_item_name')
  obj.available = bool(json.get('available'))
  obj.description = json.get('description')
  obj.kit = json.get('kit')
  obj.min_samples = json.get('min_samples')
  obj.multiplexing = bool(json.get('multiplexing'))
  obj.needs_review = bool(json.get('needs_review'))
  obj.own_risk = bool(json.get('own_risk'))
  obj.plate_submission = json.get('plate_submission')
  obj.platform = json.get('platform')
  obj.prep_per_sample = bool(json.get('prep_per_sample'))
  obj.prep_volume = json.get('prep_volume')
  obj.preparation_type = json.get('preparation_type')
  obj.pricing_item_name = json.get('pricing_item_name')
  obj.qc_per_sample = bool(json.get('qc_per_sample'))
  obj.samples_per_plate = json.get('samples_per_plate')
  obj.strand_specific = bool(json.get('strand_specific'))
  obj.adaptor_type_ref = plainToAdaptorType(json['adaptor_type_ref']) if json.get('adaptor_type_ref') else None
  obj.additional_qc_item = plainToPricingItem(json['additional_qc_item']) if json.get('additional_qc_item') else None
  obj.cutout_sizes = [ plainToCutoutSize(o) for o in json['cutout_sizes'] ] if json.get('cutout_sizes') else []
  obj.platform_ref = plainToPlatform(json['platform_ref']) if json.get('platform_ref') else None
  obj.preparation_type_ref = plainToPreparationType(json['preparation_type_ref']) if json.get('preparation_type_ref') else None
  obj.pricing_item = plainToPricingItem(json['pricing_item']) if json.get('pricing_item') else None
  obj.samples = [ plainToSample(o) for o in json['samples'] ] if json.get('samples') else []

  return obj

def serializePreparationKit(obj: PreparationKit) -> dict:
  json = {}
  json['adaptor_type'] = obj.adaptor_type
  json['additional_qc_item_name'] = obj.additional_qc_item_name
  json['available'] = obj.available
  json['description'] = obj.description
  json['kit'] = obj.kit
  json['min_samples'] = obj.min_samples
  json['multiplexing'] = obj.multiplexing
  json['needs_review'] = obj.needs_review
  json['own_risk'] = obj.own_risk
  json['plate_submission'] = obj.plate_submission
  json['platform'] = obj.platform
  json['prep_per_sample'] = obj.prep_per_sample
  json['prep_volume'] = obj.prep_volume
  json['preparation_type'] = obj.preparation_type
  json['pricing_item_name'] = obj.pricing_item_name
  json['qc_per_sample'] = obj.qc_per_sample
  json['samples_per_plate'] = obj.samples_per_plate
  json['strand_specific'] = obj.strand_specific
  json['adaptor_type_ref'] = serializeAdaptorType(obj.adaptor_type_ref) if obj.adaptor_type_ref is not None else None
  json['additional_qc_item'] = serializePricingItem(obj.additional_qc_item) if obj.additional_qc_item is not None else None
  if obj.cutout_sizes is not None:
    json['cutout_sizes'] = [ serializeCutoutSize(o) for o in obj.cutout_sizes ]
  json['platform_ref'] = serializePlatform(obj.platform_ref) if obj.platform_ref is not None else None
  json['preparation_type_ref'] = serializePreparationType(obj.preparation_type_ref) if obj.preparation_type_ref is not None else None
  json['pricing_item'] = serializePricingItem(obj.pricing_item) if obj.pricing_item is not None else None
  if obj.samples is not None:
    json['samples'] = [ serializeSample(o) for o in obj.samples ]

  return json


@dataclass
class PreparationKit:
  adaptor_type: typing.Optional[str] = None
  additional_qc_item_name: typing.Optional[str] = None
  available: typing.Optional[bool] = None
  description: typing.Optional[str] = None
  kit: typing.Optional[str] = None
  min_samples: typing.Optional[typing.Union[int, float]] = None
  multiplexing: typing.Optional[bool] = None
  needs_review: typing.Optional[bool] = None
  own_risk: typing.Optional[bool] = None
  plate_submission: typing.Optional[typing.Union[int, float]] = None
  platform: typing.Optional[str] = None
  prep_per_sample: typing.Optional[bool] = None
  prep_volume: typing.Optional[typing.Any] = None
  preparation_type: typing.Optional[str] = None
  pricing_item_name: typing.Optional[str] = None
  qc_per_sample: typing.Optional[bool] = None
  samples_per_plate: typing.Optional[typing.Union[int, float]] = None
  strand_specific: typing.Optional[bool] = None

  
  adaptor_type_ref: typing.Optional[AdaptorType] = None
  additional_qc_item: typing.Optional[PricingItem] = None
  cutout_sizes: list[CutoutSize] = field(default_factory=list)
  platform_ref: typing.Optional[Platform] = None
  preparation_type_ref: typing.Optional[PreparationType] = None
  pricing_item: typing.Optional[PricingItem] = None
  samples: list[Sample] = field(default_factory=list)


# ---

def plainToPreparationStep(json: dict) -> PreparationStep:
  obj = PreparationStep()
  obj.form = json.get('form')
  obj.ordering = json.get('ordering')
  obj.platform = json.get('platform')
  obj.preparation_type = json.get('preparation_type')
  obj.form_ref = plainToForm(json['form_ref']) if json.get('form_ref') else None
  obj.preparation_type_ref = plainToPreparationType(json['preparation_type_ref']) if json.get('preparation_type_ref') else None

  return obj

def serializePreparationStep(obj: PreparationStep) -> dict:
  json = {}
  json['form'] = obj.form
  json['ordering'] = obj.ordering
  json['platform'] = obj.platform
  json['preparation_type'] = obj.preparation_type
  json['form_ref'] = serializeForm(obj.form_ref) if obj.form_ref is not None else None
  json['preparation_type_ref'] = serializePreparationType(obj.preparation_type_ref) if obj.preparation_type_ref is not None else None

  return json


@dataclass
class PreparationStep:
  form: typing.Optional[str] = None
  ordering: typing.Optional[typing.Union[int, float]] = None
  platform: typing.Optional[str] = None
  preparation_type: typing.Optional[str] = None

  
  form_ref: typing.Optional[Form] = None
  preparation_type_ref: typing.Optional[PreparationType] = None


# ---

def plainToPreparationType(json: dict) -> PreparationType:
  obj = PreparationType()
  obj.description = json.get('description')
  obj.name = json.get('name')
  obj.platform = json.get('platform')
  obj.watchdog_time = json.get('watchdog_time')
  obj.platform_ref = plainToPlatform(json['platform_ref']) if json.get('platform_ref') else None
  obj.preparation_kits = [ plainToPreparationKit(o) for o in json['preparation_kits'] ] if json.get('preparation_kits') else []
  obj.preparation_steps = [ plainToPreparationStep(o) for o in json['preparation_steps'] ] if json.get('preparation_steps') else []
  obj.samples = [ plainToSample(o) for o in json['samples'] ] if json.get('samples') else []

  return obj

def serializePreparationType(obj: PreparationType) -> dict:
  json = {}
  json['description'] = obj.description
  json['name'] = obj.name
  json['platform'] = obj.platform
  json['watchdog_time'] = obj.watchdog_time
  json['platform_ref'] = serializePlatform(obj.platform_ref) if obj.platform_ref is not None else None
  if obj.preparation_kits is not None:
    json['preparation_kits'] = [ serializePreparationKit(o) for o in obj.preparation_kits ]
  if obj.preparation_steps is not None:
    json['preparation_steps'] = [ serializePreparationStep(o) for o in obj.preparation_steps ]
  if obj.samples is not None:
    json['samples'] = [ serializeSample(o) for o in obj.samples ]

  return json


@dataclass
class PreparationType:
  description: typing.Optional[str] = None
  name: typing.Optional[str] = None
  platform: typing.Optional[str] = None
  watchdog_time: typing.Optional[typing.Union[int, float]] = None

  
  platform_ref: typing.Optional[Platform] = None
  preparation_kits: list[PreparationKit] = field(default_factory=list)
  preparation_steps: list[PreparationStep] = field(default_factory=list)
  samples: list[Sample] = field(default_factory=list)


# ---

def plainToPriceList(json: dict) -> PriceList:
  obj = PriceList()
  obj.description = json.get('description')
  obj.id = json.get('id')
  obj.valid_from = datetime.fromisoformat(json.get('valid_from', '')) if json.get('valid_from') else None
  obj.items = [ plainToPriceListItem(o) for o in json['items'] ] if json.get('items') else []

  return obj

def serializePriceList(obj: PriceList) -> dict:
  json = {}
  json['description'] = obj.description
  json['id'] = obj.id
  json['valid_from'] = obj.valid_from.isoformat() if obj.valid_from else None
  if obj.items is not None:
    json['items'] = [ serializePriceListItem(o) for o in obj.items ]

  return json


@dataclass
class PriceList:
  description: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  valid_from: typing.Optional[datetime] = None

  
  items: list[PriceListItem] = field(default_factory=list)


# ---

def plainToPriceListItem(json: dict) -> PriceListItem:
  obj = PriceListItem()
  obj.category = json.get('category')
  obj.code = json.get('code')
  obj.comment = json.get('comment')
  obj.count = json.get('count')
  obj.description = json.get('description')
  obj.id = json.get('id')
  obj.item = json.get('item')
  obj.ordering = json.get('ordering')
  obj.price = json.get('price')
  obj.price_list_id = json.get('price_list_id')
  obj.show = bool(json.get('show'))
  obj.sort_order = json.get('sort_order')
  obj.total = json.get('total')
  obj.category_prices = [ plainToItemCategoryPrice(o) for o in json['category_prices'] ] if json.get('category_prices') else []
  obj.price_list = plainToPriceList(json['price_list']) if json.get('price_list') else None
  obj.pricing_item = plainToPricingItem(json['pricing_item']) if json.get('pricing_item') else None

  return obj

def serializePriceListItem(obj: PriceListItem) -> dict:
  json = {}
  json['category'] = obj.category
  json['code'] = obj.code
  json['comment'] = obj.comment
  json['count'] = obj.count
  json['description'] = obj.description
  json['id'] = obj.id
  json['item'] = obj.item
  json['ordering'] = obj.ordering
  json['price'] = obj.price
  json['price_list_id'] = obj.price_list_id
  json['show'] = obj.show
  json['sort_order'] = obj.sort_order
  json['total'] = obj.total
  if obj.category_prices is not None:
    json['category_prices'] = [ serializeItemCategoryPrice(o) for o in obj.category_prices ]
  json['price_list'] = serializePriceList(obj.price_list) if obj.price_list is not None else None
  json['pricing_item'] = serializePricingItem(obj.pricing_item) if obj.pricing_item is not None else None

  return json


@dataclass
class PriceListItem:
  category: typing.Optional[str] = None
  code: typing.Optional[str] = None
  comment: typing.Optional[str] = None
  count: typing.Optional[typing.Union[int, float]] = None
  description: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  item: typing.Optional[str] = None
  ordering: typing.Optional[typing.Union[int, float]] = None
  price: typing.Optional[typing.Union[int, float]] = None
  price_list_id: typing.Optional[typing.Union[int, float]] = None
  show: typing.Optional[bool] = None
  sort_order: typing.Optional[typing.Any] = None
  total: typing.Optional[typing.Union[int, float]] = None

  
  category_prices: list[ItemCategoryPrice] = field(default_factory=list)
  price_list: typing.Optional[PriceList] = None
  pricing_item: typing.Optional[PricingItem] = None


# ---

def plainToPricingCategory(json: dict) -> PricingCategory:
  obj = PricingCategory()
  obj.code = json.get('code')
  obj.description = json.get('description')
  obj.name = json.get('name')
  obj.category_prices = [ plainToItemCategoryPrice(o) for o in json['category_prices'] ] if json.get('category_prices') else []
  obj.groups = [ plainToGroup(o) for o in json['groups'] ] if json.get('groups') else []

  return obj

def serializePricingCategory(obj: PricingCategory) -> dict:
  json = {}
  json['code'] = obj.code
  json['description'] = obj.description
  json['name'] = obj.name
  if obj.category_prices is not None:
    json['category_prices'] = [ serializeItemCategoryPrice(o) for o in obj.category_prices ]
  if obj.groups is not None:
    json['groups'] = [ serializeGroup(o) for o in obj.groups ]

  return json


@dataclass
class PricingCategory:
  code: typing.Optional[str] = None
  description: typing.Optional[str] = None
  name: typing.Optional[str] = None

  
  category_prices: list[ItemCategoryPrice] = field(default_factory=list)
  groups: list[Group] = field(default_factory=list)


# ---

def plainToPricingItem(json: dict) -> PricingItem:
  obj = PricingItem()
  obj.base_item = json.get('base_item')
  obj.category = json.get('category')
  obj.comment = json.get('comment')
  obj.count_bracket_max = json.get('count_bracket_max')
  obj.count_bracket_min = json.get('count_bracket_min')
  obj.description = json.get('description')
  obj.foreign_billing = bool(json.get('foreign_billing'))
  obj.heading = json.get('heading')
  obj.item = json.get('item')
  obj.unit = json.get('unit')
  obj.base_item_ref = plainToPricingItem(json['base_item_ref']) if json.get('base_item_ref') else None
  obj.inventory_items = [ plainToInventoryItem(o) for o in json['inventory_items'] ] if json.get('inventory_items') else []
  obj.preparation_kits = [ plainToPreparationKit(o) for o in json['preparation_kits'] ] if json.get('preparation_kits') else []
  obj.price_list_items = [ plainToPriceListItem(o) for o in json['price_list_items'] ] if json.get('price_list_items') else []
  obj.staggered_items = [ plainToPricingItem(o) for o in json['staggered_items'] ] if json.get('staggered_items') else []

  return obj

def serializePricingItem(obj: PricingItem) -> dict:
  json = {}
  json['base_item'] = obj.base_item
  json['category'] = obj.category
  json['comment'] = obj.comment
  json['count_bracket_max'] = obj.count_bracket_max
  json['count_bracket_min'] = obj.count_bracket_min
  json['description'] = obj.description
  json['foreign_billing'] = obj.foreign_billing
  json['heading'] = obj.heading
  json['item'] = obj.item
  json['unit'] = obj.unit
  json['base_item_ref'] = serializePricingItem(obj.base_item_ref) if obj.base_item_ref is not None else None
  if obj.inventory_items is not None:
    json['inventory_items'] = [ serializeInventoryItem(o) for o in obj.inventory_items ]
  if obj.preparation_kits is not None:
    json['preparation_kits'] = [ serializePreparationKit(o) for o in obj.preparation_kits ]
  if obj.price_list_items is not None:
    json['price_list_items'] = [ serializePriceListItem(o) for o in obj.price_list_items ]
  if obj.staggered_items is not None:
    json['staggered_items'] = [ serializePricingItem(o) for o in obj.staggered_items ]

  return json


@dataclass
class PricingItem:
  base_item: typing.Optional[str] = None
  category: typing.Optional[str] = None
  comment: typing.Optional[str] = None
  count_bracket_max: typing.Optional[typing.Union[int, float]] = None
  count_bracket_min: typing.Optional[typing.Union[int, float]] = None
  description: typing.Optional[str] = None
  foreign_billing: typing.Optional[bool] = None
  heading: typing.Optional[str] = None
  item: typing.Optional[str] = None
  unit: typing.Optional[str] = None

  
  base_item_ref: typing.Optional[PricingItem] = None
  inventory_items: list[InventoryItem] = field(default_factory=list)
  preparation_kits: list[PreparationKit] = field(default_factory=list)
  price_list_items: list[PriceListItem] = field(default_factory=list)
  staggered_items: list[PricingItem] = field(default_factory=list)


# ---

def plainToPrimer(json: dict) -> Primer:
  obj = Primer()
  obj.available = bool(json.get('available'))
  obj.conc = json.get('conc')
  obj.create_date = datetime.fromisoformat(json.get('create_date', '')) if json.get('create_date') else None
  obj.description = json.get('description')
  obj.group = json.get('group')
  obj.group_id = json.get('group_id')
  obj.id = json.get('id')
  obj.name = json.get('name')
  obj.number = json.get('number')
  obj.platform = json.get('platform')
  obj.read = json.get('read')
  obj.sequence = json.get('sequence')
  obj.volume = json.get('volume')
  obj.group_ref = plainToGroup(json['group_ref']) if json.get('group_ref') else None
  obj.platform_ref = plainToPlatform(json['platform_ref']) if json.get('platform_ref') else None
  obj.samples = [ plainToSample(o) for o in json['samples'] ] if json.get('samples') else []

  return obj

def serializePrimer(obj: Primer) -> dict:
  json = {}
  json['available'] = obj.available
  json['conc'] = obj.conc
  json['create_date'] = obj.create_date.isoformat() if obj.create_date else None
  json['description'] = obj.description
  json['group'] = obj.group
  json['group_id'] = obj.group_id
  json['id'] = obj.id
  json['name'] = obj.name
  json['number'] = obj.number
  json['platform'] = obj.platform
  json['read'] = obj.read
  json['sequence'] = obj.sequence
  json['volume'] = obj.volume
  json['group_ref'] = serializeGroup(obj.group_ref) if obj.group_ref is not None else None
  json['platform_ref'] = serializePlatform(obj.platform_ref) if obj.platform_ref is not None else None
  if obj.samples is not None:
    json['samples'] = [ serializeSample(o) for o in obj.samples ]

  return json


@dataclass
class Primer:
  available: typing.Optional[bool] = None
  conc: typing.Optional[typing.Union[int, float]] = None
  create_date: typing.Optional[datetime] = None
  description: typing.Optional[str] = None
  group: typing.Optional[typing.Any] = None
  group_id: typing.Optional[typing.Union[int, float]] = None
  id: typing.Optional[typing.Union[int, float]] = None
  name: typing.Optional[str] = None
  number: typing.Optional[typing.Union[int, float]] = None
  platform: typing.Optional[str] = None
  read: typing.Optional[str] = None
  sequence: typing.Optional[str] = None
  volume: typing.Optional[typing.Union[int, float]] = None

  
  group_ref: typing.Optional[Group] = None
  platform_ref: typing.Optional[Platform] = None
  samples: list[Sample] = field(default_factory=list)


# ---

def plainToProject(json: dict) -> Project:
  obj = Project()
  obj.completed = datetime.fromisoformat(json.get('completed', '')) if json.get('completed') else None
  obj.cost_assignment = json.get('cost_assignment')
  obj.created = datetime.fromisoformat(json.get('created', '')) if json.get('created') else None
  obj.description = json.get('description')
  obj.group = json.get('group')
  obj.group_id = json.get('group_id')
  obj.history = [ plainToTimelineEvent(o) for o in json['history'] ] if json.get('history') else []
  obj.id = json.get('id')
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.last_request = datetime.fromisoformat(json.get('last_request', '')) if json.get('last_request') else None
  obj.name = json.get('name')
  obj.obj_id = json.get('obj_id')
  obj.obj_type = json.get('obj_type')
  obj.request_count = json.get('request_count')
  obj.sample_count = json.get('sample_count')
  obj.scientist = json.get('scientist')
  obj.scientist_id = json.get('scientist_id')
  obj.sequencing_count = json.get('sequencing_count')
  obj.status = json.get('status')
  obj.data_entries = [ plainToDataEntry(o) for o in json['data_entries'] ] if json.get('data_entries') else []
  obj.group_ref = plainToGroup(json['group_ref']) if json.get('group_ref') else None
  obj.notes = [ plainToNote(o) for o in json['notes'] ] if json.get('notes') else []
  obj.requests = [ plainToRequest(o) for o in json['requests'] ] if json.get('requests') else []
  obj.scientist_ref = plainToScientist(json['scientist_ref']) if json.get('scientist_ref') else None

  return obj

def serializeProject(obj: Project) -> dict:
  json = {}
  json['completed'] = obj.completed.isoformat() if obj.completed else None
  json['cost_assignment'] = obj.cost_assignment
  json['created'] = obj.created.isoformat() if obj.created else None
  json['description'] = obj.description
  json['group'] = obj.group
  json['group_id'] = obj.group_id
  if obj.history is not None:
    json['history'] = [ serializeTimelineEvent(o) for o in obj.history ]
  json['id'] = obj.id
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['last_request'] = obj.last_request.isoformat() if obj.last_request else None
  json['name'] = obj.name
  json['obj_id'] = obj.obj_id
  json['obj_type'] = obj.obj_type
  json['request_count'] = obj.request_count
  json['sample_count'] = obj.sample_count
  json['scientist'] = obj.scientist
  json['scientist_id'] = obj.scientist_id
  json['sequencing_count'] = obj.sequencing_count
  json['status'] = obj.status
  if obj.data_entries is not None:
    json['data_entries'] = [ serializeDataEntry(o) for o in obj.data_entries ]
  json['group_ref'] = serializeGroup(obj.group_ref) if obj.group_ref is not None else None
  if obj.notes is not None:
    json['notes'] = [ serializeNote(o) for o in obj.notes ]
  if obj.requests is not None:
    json['requests'] = [ serializeRequest(o) for o in obj.requests ]
  json['scientist_ref'] = serializeScientist(obj.scientist_ref) if obj.scientist_ref is not None else None

  return json


@dataclass
class Project:
  completed: typing.Optional[datetime] = None
  cost_assignment: typing.Optional[str] = None
  created: typing.Optional[datetime] = None
  description: typing.Optional[str] = None
  group: typing.Optional[typing.Any] = None
  group_id: typing.Optional[typing.Union[int, float]] = None
  history: list[TimelineEvent]=field(default_factory=list)
  id: typing.Optional[typing.Union[int, float]] = None
  last_change: typing.Optional[datetime] = None
  last_request: typing.Optional[datetime] = None
  name: typing.Optional[str] = None
  obj_id: typing.Optional[typing.Union[int, float]] = None
  obj_type: typing.Optional[str] = None
  request_count: typing.Optional[typing.Union[int, float]] = None
  sample_count: typing.Optional[typing.Union[int, float]] = None
  scientist: typing.Optional[typing.Any] = None
  scientist_id: typing.Optional[typing.Union[int, float]] = None
  sequencing_count: typing.Optional[typing.Union[int, float]] = None
  status: typing.Optional[str] = None

  
  data_entries: list[DataEntry] = field(default_factory=list)
  group_ref: typing.Optional[Group] = None
  notes: list[Note] = field(default_factory=list)
  requests: list[Request] = field(default_factory=list)
  scientist_ref: typing.Optional[Scientist] = None


# ---

def plainToReport(json: dict) -> Report:
  obj = Report()
  obj.created = datetime.fromisoformat(json.get('created', '')) if json.get('created') else None
  obj.id = json.get('id')
  obj.json_data = json.get('json_data')
  obj.raw_data = json.get('raw_data')
  obj.report_html = json.get('report_html')
  obj.report_path = json.get('report_path')
  obj.title = json.get('title')
  obj.type = json.get('type')

  return obj

def serializeReport(obj: Report) -> dict:
  json = {}
  json['created'] = obj.created.isoformat() if obj.created else None
  json['id'] = obj.id
  json['json_data'] = obj.json_data
  json['raw_data'] = obj.raw_data
  json['report_html'] = obj.report_html
  json['report_path'] = obj.report_path
  json['title'] = obj.title
  json['type'] = obj.type

  return json


@dataclass
class Report:
  created: typing.Optional[datetime] = None
  id: typing.Optional[typing.Union[int, float]] = None
  json_data: typing.Optional[dict] = None
  raw_data: typing.Optional[dict] = None
  report_html: typing.Optional[str] = None
  report_path: typing.Optional[str] = None
  title: typing.Optional[str] = None
  type: typing.Optional[str] = None

  
  

# ---

def plainToRequest(json: dict) -> Request:
  obj = Request()
  obj._imp_storage = bool(json.get('_imp_storage'))
  obj.accepted = datetime.fromisoformat(json.get('accepted', '')) if json.get('accepted') else None
  obj.attachment_count = json.get('attachment_count')
  obj.comments = json.get('comments')
  obj.completed = datetime.fromisoformat(json.get('completed', '')) if json.get('completed') else None
  obj.cost_assignment = json.get('cost_assignment')
  obj.custom_readlength = json.get('custom_readlength')
  obj.demultiplexing = bool(json.get('demultiplexing'))
  obj.duration = json.get('duration')
  obj.external_analysis = json.get('external_analysis')
  obj.group = json.get('group')
  obj.group_id = json.get('group_id')
  obj.history = [ plainToTimelineEvent(o) for o in json['history'] ] if json.get('history') else []
  obj.id = json.get('id')
  obj.is_control = bool(json.get('is_control'))
  obj.lab_count = json.get('lab_count')
  obj.lab_steps = [ plainToLabStep(o) for o in json['lab_steps'] ] if json.get('lab_steps') else []
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.long_seqtype = json.get('long_seqtype')
  obj.measurement_count = json.get('measurement_count')
  obj.needs_review = bool(json.get('needs_review'))
  obj.notes_count = json.get('notes_count')
  obj.obj_id = json.get('obj_id')
  obj.obj_type = json.get('obj_type')
  obj.parent_request_id = json.get('parent_request_id')
  obj.plate_submission_required = bool(json.get('plate_submission_required'))
  obj.platform = json.get('platform')
  obj.priority = json.get('priority')
  obj.project_id = json.get('project_id')
  obj.readmode = plainToReadmode(json['readmode']) if json.get('readmode') else None
  obj.readmode_id = json.get('readmode_id')
  obj.reviewed = bool(json.get('reviewed'))
  obj.sample_fields = plainToSampleFields(json['sample_fields']) if json.get('sample_fields') else None
  obj.sampnum = json.get('sampnum')
  obj.scientist = json.get('scientist')
  obj.scientist_id = json.get('scientist_id')
  obj.selfservice = bool(json.get('selfservice'))
  obj.sequencing_count = json.get('sequencing_count')
  obj.short_seqtype = json.get('short_seqtype')
  obj.status = json.get('status')
  obj.submitted = datetime.fromisoformat(json.get('submitted', '')) if json.get('submitted') else None
  obj.xp_workflow_enabled = bool(json.get('xp_workflow_enabled'))
  obj.attachments = [ plainToAttachment(o) for o in json['attachments'] ] if json.get('attachments') else []
  obj.cost_estimate_ref = plainToCostEstimate(json['cost_estimate_ref']) if json.get('cost_estimate_ref') else None
  obj.data_entries = [ plainToDataEntry(o) for o in json['data_entries'] ] if json.get('data_entries') else []
  obj.group_ref = plainToGroup(json['group_ref']) if json.get('group_ref') else None
  obj.invoice_ref = plainToInvoice(json['invoice_ref']) if json.get('invoice_ref') else None
  obj.notes = [ plainToNote(o) for o in json['notes'] ] if json.get('notes') else []
  obj.parent_request_ref = plainToRequest(json['parent_request_ref']) if json.get('parent_request_ref') else None
  obj.platform_ref = plainToPlatform(json['platform_ref']) if json.get('platform_ref') else None
  obj.project = plainToProject(json['project']) if json.get('project') else None
  obj.request_lanes = [ plainToRequestLane(o) for o in json['request_lanes'] ] if json.get('request_lanes') else []
  obj.scientist_ref = plainToScientist(json['scientist_ref']) if json.get('scientist_ref') else None
  obj.shadow_requests = [ plainToRequest(o) for o in json['shadow_requests'] ] if json.get('shadow_requests') else []
  obj.versions = [ plainToObjectVersion(o) for o in json['versions'] ] if json.get('versions') else []

  return obj

def serializeRequest(obj: Request) -> dict:
  json = {}
  json['_imp_storage'] = obj._imp_storage
  json['accepted'] = obj.accepted.isoformat() if obj.accepted else None
  json['attachment_count'] = obj.attachment_count
  json['comments'] = obj.comments
  json['completed'] = obj.completed.isoformat() if obj.completed else None
  json['cost_assignment'] = obj.cost_assignment
  json['custom_readlength'] = obj.custom_readlength
  json['demultiplexing'] = obj.demultiplexing
  json['duration'] = obj.duration
  json['external_analysis'] = obj.external_analysis
  json['group'] = obj.group
  json['group_id'] = obj.group_id
  if obj.history is not None:
    json['history'] = [ serializeTimelineEvent(o) for o in obj.history ]
  json['id'] = obj.id
  json['is_control'] = obj.is_control
  json['lab_count'] = obj.lab_count
  if obj.lab_steps is not None:
    json['lab_steps'] = [ serializeLabStep(o) for o in obj.lab_steps ]
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['long_seqtype'] = obj.long_seqtype
  json['measurement_count'] = obj.measurement_count
  json['needs_review'] = obj.needs_review
  json['notes_count'] = obj.notes_count
  json['obj_id'] = obj.obj_id
  json['obj_type'] = obj.obj_type
  json['parent_request_id'] = obj.parent_request_id
  json['plate_submission_required'] = obj.plate_submission_required
  json['platform'] = obj.platform
  json['priority'] = obj.priority
  json['project_id'] = obj.project_id
  json['readmode'] = serializeReadmode(obj.readmode) if obj.readmode is not None else None
  json['readmode_id'] = obj.readmode_id
  json['reviewed'] = obj.reviewed
  json['sample_fields'] = serializeSampleFields(obj.sample_fields) if obj.sample_fields is not None else None
  json['sampnum'] = obj.sampnum
  json['scientist'] = obj.scientist
  json['scientist_id'] = obj.scientist_id
  json['selfservice'] = obj.selfservice
  json['sequencing_count'] = obj.sequencing_count
  json['short_seqtype'] = obj.short_seqtype
  json['status'] = obj.status
  json['submitted'] = obj.submitted.isoformat() if obj.submitted else None
  json['xp_workflow_enabled'] = obj.xp_workflow_enabled
  if obj.attachments is not None:
    json['attachments'] = [ serializeAttachment(o) for o in obj.attachments ]
  json['cost_estimate_ref'] = serializeCostEstimate(obj.cost_estimate_ref) if obj.cost_estimate_ref is not None else None
  if obj.data_entries is not None:
    json['data_entries'] = [ serializeDataEntry(o) for o in obj.data_entries ]
  json['group_ref'] = serializeGroup(obj.group_ref) if obj.group_ref is not None else None
  json['invoice_ref'] = serializeInvoice(obj.invoice_ref) if obj.invoice_ref is not None else None
  if obj.notes is not None:
    json['notes'] = [ serializeNote(o) for o in obj.notes ]
  json['parent_request_ref'] = serializeRequest(obj.parent_request_ref) if obj.parent_request_ref is not None else None
  json['platform_ref'] = serializePlatform(obj.platform_ref) if obj.platform_ref is not None else None
  json['project'] = serializeProject(obj.project) if obj.project is not None else None
  if obj.request_lanes is not None:
    json['request_lanes'] = [ serializeRequestLane(o) for o in obj.request_lanes ]
  json['scientist_ref'] = serializeScientist(obj.scientist_ref) if obj.scientist_ref is not None else None
  if obj.shadow_requests is not None:
    json['shadow_requests'] = [ serializeRequest(o) for o in obj.shadow_requests ]
  if obj.versions is not None:
    json['versions'] = [ serializeObjectVersion(o) for o in obj.versions ]

  return json


@dataclass
class Request:
  _imp_storage: typing.Optional[bool] = None
  accepted: typing.Optional[datetime] = None
  attachment_count: typing.Optional[typing.Union[int, float]] = None
  comments: typing.Optional[str] = None
  completed: typing.Optional[datetime] = None
  cost_assignment: typing.Optional[str] = None
  custom_readlength: typing.Optional[typing.Union[int, float]] = None
  demultiplexing: typing.Optional[bool] = None
  duration: typing.Optional[typing.Union[int, float]] = None
  external_analysis: typing.Optional[str] = None
  group: typing.Optional[typing.Any] = None
  group_id: typing.Optional[typing.Union[int, float]] = None
  history: list[TimelineEvent]=field(default_factory=list)
  id: typing.Optional[typing.Union[int, float]] = None
  is_control: typing.Optional[bool] = None
  lab_count: typing.Optional[typing.Union[int, float]] = None
  lab_steps: list[LabStep]=field(default_factory=list)
  last_change: typing.Optional[datetime] = None
  long_seqtype: typing.Optional[typing.Any] = None
  measurement_count: typing.Optional[typing.Union[int, float]] = None
  needs_review: typing.Optional[bool] = None
  notes_count: typing.Optional[typing.Union[int, float]] = None
  obj_id: typing.Optional[typing.Union[int, float]] = None
  obj_type: typing.Optional[str] = None
  parent_request_id: typing.Optional[typing.Union[int, float]] = None
  plate_submission_required: typing.Optional[bool] = None
  platform: typing.Optional[str] = None
  priority: typing.Optional[typing.Union[int, float]] = None
  project_id: typing.Optional[typing.Union[int, float]] = None
  readmode: typing.Optional[Readmode] = None
  readmode_id: typing.Optional[typing.Union[int, float]] = None
  reviewed: typing.Optional[bool] = None
  sample_fields: typing.Optional[SampleFields] = None
  sampnum: typing.Optional[typing.Union[int, float]] = None
  scientist: typing.Optional[typing.Any] = None
  scientist_id: typing.Optional[typing.Union[int, float]] = None
  selfservice: typing.Optional[bool] = None
  sequencing_count: typing.Optional[typing.Union[int, float]] = None
  short_seqtype: typing.Optional[typing.Any] = None
  status: typing.Optional[str] = None
  submitted: typing.Optional[datetime] = None
  xp_workflow_enabled: typing.Optional[bool] = None

  
  attachments: list[Attachment] = field(default_factory=list)
  cost_estimate_ref: typing.Optional[CostEstimate] = None
  data_entries: list[DataEntry] = field(default_factory=list)
  group_ref: typing.Optional[Group] = None
  invoice_ref: typing.Optional[Invoice] = None
  notes: list[Note] = field(default_factory=list)
  parent_request_ref: typing.Optional[Request] = None
  platform_ref: typing.Optional[Platform] = None
  project: typing.Optional[Project] = None
  request_lanes: list[RequestLane] = field(default_factory=list)
  scientist_ref: typing.Optional[Scientist] = None
  shadow_requests: list[Request] = field(default_factory=list)
  versions: list[ObjectVersion] = field(default_factory=list)


# ---

def plainToRequestDraft(json: dict) -> RequestDraft:
  obj = RequestDraft()
  obj.create_date = datetime.fromisoformat(json.get('create_date', '')) if json.get('create_date') else None
  obj.group = json.get('group')
  obj.group_id = json.get('group_id')
  obj.id = json.get('id')
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.name = json.get('name')
  obj.request_data = plainToRequest(json['request_data']) if json.get('request_data') else None
  obj.scientist = json.get('scientist')
  obj.scientist_id = json.get('scientist_id')
  obj.valid = bool(json.get('valid'))
  obj.group_ref = plainToGroup(json['group_ref']) if json.get('group_ref') else None
  obj.scientist_ref = plainToScientist(json['scientist_ref']) if json.get('scientist_ref') else None

  return obj

def serializeRequestDraft(obj: RequestDraft) -> dict:
  json = {}
  json['create_date'] = obj.create_date.isoformat() if obj.create_date else None
  json['group'] = obj.group
  json['group_id'] = obj.group_id
  json['id'] = obj.id
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['name'] = obj.name
  json['request_data'] = serializeRequest(obj.request_data) if obj.request_data is not None else None
  json['scientist'] = obj.scientist
  json['scientist_id'] = obj.scientist_id
  json['valid'] = obj.valid
  json['group_ref'] = serializeGroup(obj.group_ref) if obj.group_ref is not None else None
  json['scientist_ref'] = serializeScientist(obj.scientist_ref) if obj.scientist_ref is not None else None

  return json


@dataclass
class RequestDraft:
  create_date: typing.Optional[datetime] = None
  group: typing.Optional[typing.Any] = None
  group_id: typing.Optional[typing.Union[int, float]] = None
  id: typing.Optional[typing.Union[int, float]] = None
  last_change: typing.Optional[datetime] = None
  name: typing.Optional[str] = None
  request_data: typing.Optional[Request] = None
  scientist: typing.Optional[typing.Any] = None
  scientist_id: typing.Optional[typing.Union[int, float]] = None
  valid: typing.Optional[bool] = None

  
  group_ref: typing.Optional[Group] = None
  scientist_ref: typing.Optional[Scientist] = None


# ---

def plainToRequestLane(json: dict) -> RequestLane:
  obj = RequestLane()
  obj.control_for = [ plainToControlSample(o) for o in json['control_for'] ] if json.get('control_for') else []
  obj.custom_primer = json.get('custom_primer')
  obj.days_to_dismiss = json.get('days_to_dismiss')
  obj.days_to_warn = json.get('days_to_warn')
  obj.duration = json.get('duration')
  obj.extra_phix = json.get('extra_phix')
  obj.id = json.get('id')
  obj.is_control = bool(json.get('is_control'))
  obj.lab_steps = [ plainToLabStep(o) for o in json['lab_steps'] ] if json.get('lab_steps') else []
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.low_complexity = bool(json.get('low_complexity'))
  obj.multi_id = json.get('multi_id')
  obj.num = json.get('num')
  obj.onhold_notified = datetime.fromisoformat(json.get('onhold_notified', '')) if json.get('onhold_notified') else None
  obj.onhold_started = datetime.fromisoformat(json.get('onhold_started', '')) if json.get('onhold_started') else None
  obj.parent_lane = plainToRequestLane(json['parent_lane']) if json.get('parent_lane') else None
  obj.pooled = bool(json.get('pooled'))
  obj.pooling_strategy = json.get('pooling_strategy')
  obj.request_id = json.get('request_id')
  obj.required_reads = json.get('required_reads')
  obj.sample_fields = plainToSampleFields(json['sample_fields']) if json.get('sample_fields') else None
  obj.sampnum = json.get('sampnum')
  obj.sequencing_runs = [ plainToRunUnit(o) for o in json['sequencing_runs'] ] if json.get('sequencing_runs') else []
  obj.shadow_lanes = [ plainToRequestLane(o) for o in json['shadow_lanes'] ] if json.get('shadow_lanes') else []
  obj.share_required_ratio = json.get('share_required_ratio')
  obj.share_status = json.get('share_status')
  obj.show_id = json.get('show_id')
  obj.show_obj_id = json.get('show_obj_id')
  obj.status = json.get('status')
  obj.super_multi_id = json.get('super_multi_id')
  obj.time_to_watchdog = json.get('time_to_watchdog')
  obj.watchdog_notified = datetime.fromisoformat(json.get('watchdog_notified', '')) if json.get('watchdog_notified') else None
  obj.multi = plainToMultiplex(json['multi']) if json.get('multi') else None
  obj.request = plainToRequest(json['request']) if json.get('request') else None
  obj.requests_samples = [ plainToRequestsSample(o) for o in json['requests_samples'] ] if json.get('requests_samples') else []
  obj.super_multi = plainToSuperMulti(json['super_multi']) if json.get('super_multi') else None
  obj.versions = [ plainToObjectVersion(o) for o in json['versions'] ] if json.get('versions') else []

  return obj

def serializeRequestLane(obj: RequestLane) -> dict:
  json = {}
  if obj.control_for is not None:
    json['control_for'] = [ serializeControlSample(o) for o in obj.control_for ]
  json['custom_primer'] = obj.custom_primer
  json['days_to_dismiss'] = obj.days_to_dismiss
  json['days_to_warn'] = obj.days_to_warn
  json['duration'] = obj.duration
  json['extra_phix'] = obj.extra_phix
  json['id'] = obj.id
  json['is_control'] = obj.is_control
  if obj.lab_steps is not None:
    json['lab_steps'] = [ serializeLabStep(o) for o in obj.lab_steps ]
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['low_complexity'] = obj.low_complexity
  json['multi_id'] = obj.multi_id
  json['num'] = obj.num
  json['onhold_notified'] = obj.onhold_notified.isoformat() if obj.onhold_notified else None
  json['onhold_started'] = obj.onhold_started.isoformat() if obj.onhold_started else None
  json['parent_lane'] = serializeRequestLane(obj.parent_lane) if obj.parent_lane is not None else None
  json['pooled'] = obj.pooled
  json['pooling_strategy'] = obj.pooling_strategy
  json['request_id'] = obj.request_id
  json['required_reads'] = obj.required_reads
  json['sample_fields'] = serializeSampleFields(obj.sample_fields) if obj.sample_fields is not None else None
  json['sampnum'] = obj.sampnum
  if obj.sequencing_runs is not None:
    json['sequencing_runs'] = [ serializeRunUnit(o) for o in obj.sequencing_runs ]
  if obj.shadow_lanes is not None:
    json['shadow_lanes'] = [ serializeRequestLane(o) for o in obj.shadow_lanes ]
  json['share_required_ratio'] = obj.share_required_ratio
  json['share_status'] = obj.share_status
  json['show_id'] = obj.show_id
  json['show_obj_id'] = obj.show_obj_id
  json['status'] = obj.status
  json['super_multi_id'] = obj.super_multi_id
  json['time_to_watchdog'] = obj.time_to_watchdog
  json['watchdog_notified'] = obj.watchdog_notified.isoformat() if obj.watchdog_notified else None
  json['multi'] = serializeMultiplex(obj.multi) if obj.multi is not None else None
  json['request'] = serializeRequest(obj.request) if obj.request is not None else None
  if obj.requests_samples is not None:
    json['requests_samples'] = [ serializeRequestsSample(o) for o in obj.requests_samples ]
  json['super_multi'] = serializeSuperMulti(obj.super_multi) if obj.super_multi is not None else None
  if obj.versions is not None:
    json['versions'] = [ serializeObjectVersion(o) for o in obj.versions ]

  return json


@dataclass
class RequestLane:
  control_for: list[ControlSample]=field(default_factory=list)
  custom_primer: typing.Optional[typing.Any] = None
  days_to_dismiss: typing.Optional[typing.Union[int, float]] = None
  days_to_warn: typing.Optional[typing.Union[int, float]] = None
  duration: typing.Optional[typing.Union[int, float]] = None
  extra_phix: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  is_control: typing.Optional[bool] = None
  lab_steps: list[LabStep]=field(default_factory=list)
  last_change: typing.Optional[datetime] = None
  low_complexity: typing.Optional[bool] = None
  multi_id: typing.Optional[typing.Union[int, float]] = None
  num: typing.Optional[typing.Union[int, float]] = None
  onhold_notified: typing.Optional[datetime] = None
  onhold_started: typing.Optional[datetime] = None
  parent_lane: typing.Optional[RequestLane] = None
  pooled: typing.Optional[bool] = None
  pooling_strategy: typing.Optional[typing.Any] = None
  request_id: typing.Optional[typing.Union[int, float]] = None
  required_reads: typing.Optional[typing.Union[int, float]] = None
  sample_fields: typing.Optional[SampleFields] = None
  sampnum: typing.Optional[typing.Union[int, float]] = None
  sequencing_runs: list[RunUnit]=field(default_factory=list)
  shadow_lanes: list[RequestLane]=field(default_factory=list)
  share_required_ratio: typing.Optional[typing.Any] = None
  share_status: typing.Optional[typing.Any] = None
  show_id: typing.Optional[typing.Any] = None
  show_obj_id: typing.Optional[str] = None
  status: typing.Optional[str] = None
  super_multi_id: typing.Optional[typing.Union[int, float]] = None
  time_to_watchdog: typing.Optional[typing.Union[int, float]] = None
  watchdog_notified: typing.Optional[datetime] = None

  
  multi: typing.Optional[Multiplex] = None
  request: typing.Optional[Request] = None
  requests_samples: list[RequestsSample] = field(default_factory=list)
  super_multi: typing.Optional[SuperMulti] = None
  versions: list[ObjectVersion] = field(default_factory=list)


# ---

def plainToRequestsSample(json: dict) -> RequestsSample:
  obj = RequestsSample()
  obj.analysis_pipeline = json.get('analysis_pipeline')
  obj.duration = json.get('duration')
  obj.id = json.get('id')
  obj.lane = json.get('lane')
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.obj_id = json.get('obj_id')
  obj.obj_type = json.get('obj_type')
  obj.onhold_started = datetime.fromisoformat(json.get('onhold_started', '')) if json.get('onhold_started') else None
  obj.ratio = json.get('ratio')
  obj.request_id = json.get('request_id')
  obj.required_ratio = json.get('required_ratio')
  obj.required_reads = json.get('required_reads')
  obj.resubmission = bool(json.get('resubmission'))
  obj.sample_id = json.get('sample_id')
  obj.status = json.get('status')
  obj.time_to_watchdog = json.get('time_to_watchdog')
  obj._request = plainToRequest(json['_request']) if json.get('_request') else None
  obj.request_lane = plainToRequestLane(json['request_lane']) if json.get('request_lane') else None
  obj.sample = plainToSample(json['sample']) if json.get('sample') else None
  obj.sequenced_samples = [ plainToSequencedSample(o) for o in json['sequenced_samples'] ] if json.get('sequenced_samples') else []
  obj.versions = [ plainToObjectVersion(o) for o in json['versions'] ] if json.get('versions') else []

  return obj

def serializeRequestsSample(obj: RequestsSample) -> dict:
  json = {}
  json['analysis_pipeline'] = obj.analysis_pipeline
  json['duration'] = obj.duration
  json['id'] = obj.id
  json['lane'] = obj.lane
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['obj_id'] = obj.obj_id
  json['obj_type'] = obj.obj_type
  json['onhold_started'] = obj.onhold_started.isoformat() if obj.onhold_started else None
  json['ratio'] = obj.ratio
  json['request_id'] = obj.request_id
  json['required_ratio'] = obj.required_ratio
  json['required_reads'] = obj.required_reads
  json['resubmission'] = obj.resubmission
  json['sample_id'] = obj.sample_id
  json['status'] = obj.status
  json['time_to_watchdog'] = obj.time_to_watchdog
  json['_request'] = serializeRequest(obj._request) if obj._request is not None else None
  json['request_lane'] = serializeRequestLane(obj.request_lane) if obj.request_lane is not None else None
  json['sample'] = serializeSample(obj.sample) if obj.sample is not None else None
  if obj.sequenced_samples is not None:
    json['sequenced_samples'] = [ serializeSequencedSample(o) for o in obj.sequenced_samples ]
  if obj.versions is not None:
    json['versions'] = [ serializeObjectVersion(o) for o in obj.versions ]

  return json


@dataclass
class RequestsSample:
  analysis_pipeline: typing.Optional[str] = None
  duration: typing.Optional[typing.Union[int, float]] = None
  id: typing.Optional[typing.Union[int, float]] = None
  lane: typing.Optional[typing.Union[int, float]] = None
  last_change: typing.Optional[datetime] = None
  obj_id: typing.Optional[typing.Union[int, float]] = None
  obj_type: typing.Optional[str] = None
  onhold_started: typing.Optional[datetime] = None
  ratio: typing.Optional[typing.Union[int, float]] = None
  request_id: typing.Optional[typing.Union[int, float]] = None
  required_ratio: typing.Optional[typing.Any] = None
  required_reads: typing.Optional[typing.Union[int, float]] = None
  resubmission: typing.Optional[bool] = None
  sample_id: typing.Optional[typing.Union[int, float]] = None
  status: typing.Optional[str] = None
  time_to_watchdog: typing.Optional[typing.Union[int, float]] = None

  
  _request: typing.Optional[Request] = None
  request_lane: typing.Optional[RequestLane] = None
  sample: typing.Optional[Sample] = None
  sequenced_samples: list[SequencedSample] = field(default_factory=list)
  versions: list[ObjectVersion] = field(default_factory=list)


# ---

def plainToResultCheck(json: dict) -> ResultCheck:
  obj = ResultCheck()
  obj.actual_ratio = json.get('actual_ratio')
  obj.actual_reads = json.get('actual_reads')
  obj.barcode = json.get('barcode')
  obj.basecalls = json.get('basecalls')
  obj.checked_by_user = json.get('checked_by_user')
  obj.checked_on = datetime.fromisoformat(json.get('checked_on', '')) if json.get('checked_on') else None
  obj.checking_by_date = datetime.fromisoformat(json.get('checking_by_date', '')) if json.get('checking_by_date') else None
  obj.checking_by_user = json.get('checking_by_user')
  obj.comment = json.get('comment')
  obj.deleted_on = datetime.fromisoformat(json.get('deleted_on', '')) if json.get('deleted_on') else None
  obj.downloaded = bool(json.get('downloaded'))
  obj.file_status = json.get('file_status')
  obj.id = json.get('id')
  obj.md5 = json.get('md5')
  obj.nanostat = plainToNanostat(json['nanostat']) if json.get('nanostat') else None
  obj.notified_on = datetime.fromisoformat(json.get('notified_on', '')) if json.get('notified_on') else None
  obj.reqsamp_id = json.get('reqsamp_id')
  obj.required_bloom_filter = json.get('required_bloom_filter')
  obj.required_ratio = json.get('required_ratio')
  obj.required_reads = json.get('required_reads')
  obj.result = json.get('result')
  obj.run_id = json.get('run_id')
  obj.samplestat = plainToSamplestat(json['samplestat']) if json.get('samplestat') else None
  obj.subreadstat = plainToSubreadstat(json['subreadstat']) if json.get('subreadstat') else None
  obj.sync_time = datetime.fromisoformat(json.get('sync_time', '')) if json.get('sync_time') else None
  obj.unit_id = json.get('unit_id')
  obj.vendor_id = json.get('vendor_id')
  obj.fastqcs = [ plainToFastqc(o) for o in json['fastqcs'] ] if json.get('fastqcs') else []
  obj.nanostats = [ plainToNanostat(o) for o in json['nanostats'] ] if json.get('nanostats') else []
  obj.run_unit = plainToRunUnit(json['run_unit']) if json.get('run_unit') else None
  obj.samplestats = [ plainToSamplestat(o) for o in json['samplestats'] ] if json.get('samplestats') else []
  obj.sequenced_sample = plainToSequencedSample(json['sequenced_sample']) if json.get('sequenced_sample') else None
  obj.subreadstats = [ plainToSubreadstat(o) for o in json['subreadstats'] ] if json.get('subreadstats') else []

  return obj

def serializeResultCheck(obj: ResultCheck) -> dict:
  json = {}
  json['actual_ratio'] = obj.actual_ratio
  json['actual_reads'] = obj.actual_reads
  json['barcode'] = obj.barcode
  json['basecalls'] = obj.basecalls
  json['checked_by_user'] = obj.checked_by_user
  json['checked_on'] = obj.checked_on.isoformat() if obj.checked_on else None
  json['checking_by_date'] = obj.checking_by_date.isoformat() if obj.checking_by_date else None
  json['checking_by_user'] = obj.checking_by_user
  json['comment'] = obj.comment
  json['deleted_on'] = obj.deleted_on.isoformat() if obj.deleted_on else None
  json['downloaded'] = obj.downloaded
  json['file_status'] = obj.file_status
  json['id'] = obj.id
  json['md5'] = obj.md5
  json['nanostat'] = serializeNanostat(obj.nanostat) if obj.nanostat is not None else None
  json['notified_on'] = obj.notified_on.isoformat() if obj.notified_on else None
  json['reqsamp_id'] = obj.reqsamp_id
  json['required_bloom_filter'] = obj.required_bloom_filter
  json['required_ratio'] = obj.required_ratio
  json['required_reads'] = obj.required_reads
  json['result'] = obj.result
  json['run_id'] = obj.run_id
  json['samplestat'] = serializeSamplestat(obj.samplestat) if obj.samplestat is not None else None
  json['subreadstat'] = serializeSubreadstat(obj.subreadstat) if obj.subreadstat is not None else None
  json['sync_time'] = obj.sync_time.isoformat() if obj.sync_time else None
  json['unit_id'] = obj.unit_id
  json['vendor_id'] = obj.vendor_id
  if obj.fastqcs is not None:
    json['fastqcs'] = [ serializeFastqc(o) for o in obj.fastqcs ]
  if obj.nanostats is not None:
    json['nanostats'] = [ serializeNanostat(o) for o in obj.nanostats ]
  json['run_unit'] = serializeRunUnit(obj.run_unit) if obj.run_unit is not None else None
  if obj.samplestats is not None:
    json['samplestats'] = [ serializeSamplestat(o) for o in obj.samplestats ]
  json['sequenced_sample'] = serializeSequencedSample(obj.sequenced_sample) if obj.sequenced_sample is not None else None
  if obj.subreadstats is not None:
    json['subreadstats'] = [ serializeSubreadstat(o) for o in obj.subreadstats ]

  return json


@dataclass
class ResultCheck:
  actual_ratio: typing.Optional[typing.Any] = None
  actual_reads: typing.Optional[typing.Any] = None
  barcode: typing.Optional[str] = None
  basecalls: typing.Optional[str] = None
  checked_by_user: typing.Optional[typing.Union[int, float]] = None
  checked_on: typing.Optional[datetime] = None
  checking_by_date: typing.Optional[datetime] = None
  checking_by_user: typing.Optional[typing.Union[int, float]] = None
  comment: typing.Optional[str] = None
  deleted_on: typing.Optional[datetime] = None
  downloaded: typing.Optional[bool] = None
  file_status: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  md5: typing.Optional[str] = None
  nanostat: typing.Optional[Nanostat] = None
  notified_on: typing.Optional[datetime] = None
  reqsamp_id: typing.Optional[typing.Union[int, float]] = None
  required_bloom_filter: typing.Optional[typing.Any] = None
  required_ratio: typing.Optional[typing.Any] = None
  required_reads: typing.Optional[typing.Any] = None
  result: typing.Optional[str] = None
  run_id: typing.Optional[typing.Union[int, float]] = None
  samplestat: typing.Optional[Samplestat] = None
  subreadstat: typing.Optional[Subreadstat] = None
  sync_time: typing.Optional[datetime] = None
  unit_id: typing.Optional[typing.Union[int, float]] = None
  vendor_id: typing.Optional[str] = None

  
  fastqcs: list[Fastqc] = field(default_factory=list)
  nanostats: list[Nanostat] = field(default_factory=list)
  run_unit: typing.Optional[RunUnit] = None
  samplestats: list[Samplestat] = field(default_factory=list)
  sequenced_sample: typing.Optional[SequencedSample] = None
  subreadstats: list[Subreadstat] = field(default_factory=list)


# ---

def plainToRun(json: dict) -> Run:
  obj = Run()
  obj.comments = json.get('comments')
  obj.description = json.get('description')
  obj.draft = bool(json.get('draft'))
  obj.group = json.get('group')
  obj.group_id = json.get('group_id')
  obj.id = json.get('id')
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.machine = json.get('machine')
  obj.name = json.get('name')
  obj.obj_type = json.get('obj_type')
  obj.platform = json.get('platform')
  obj.preparation_date = datetime.fromisoformat(json.get('preparation_date', '')) if json.get('preparation_date') else None
  obj.readmode = plainToReadmode(json['readmode']) if json.get('readmode') else None
  obj.readmode_id = json.get('readmode_id')
  obj.report_url = json.get('report_url')
  obj.run_folder = json.get('run_folder')
  obj.scientist = json.get('scientist')
  obj.scientist_id = json.get('scientist_id')
  obj.selfservice = bool(json.get('selfservice'))
  obj.sequencing_date = datetime.fromisoformat(json.get('sequencing_date', '')) if json.get('sequencing_date') else None
  obj.status = json.get('status')
  obj.username = json.get('username')
  obj.vendor_id = json.get('vendor_id')
  obj.group_ref = plainToGroup(json['group_ref']) if json.get('group_ref') else None
  obj.illumina_run_ref = plainToIlluminaRun(json['illumina_run_ref']) if json.get('illumina_run_ref') else None
  obj.inventory_changes = [ plainToInventoryChange(o) for o in json['inventory_changes'] ] if json.get('inventory_changes') else []
  obj.machine_ref = plainToMachine(json['machine_ref']) if json.get('machine_ref') else None
  obj.ont_run_ref = plainToOntRun(json['ont_run_ref']) if json.get('ont_run_ref') else None
  obj.pacbio_run_ref = plainToPacbioRun(json['pacbio_run_ref']) if json.get('pacbio_run_ref') else None
  obj.platform_ref = plainToPlatform(json['platform_ref']) if json.get('platform_ref') else None
  obj.run_units = [ plainToRunUnit(o) for o in json['run_units'] ] if json.get('run_units') else []
  obj.scientist_ref = plainToScientist(json['scientist_ref']) if json.get('scientist_ref') else None
  obj.user_ref = plainToScientist(json['user_ref']) if json.get('user_ref') else None

  return obj

def serializeRun(obj: Run) -> dict:
  json = {}
  json['comments'] = obj.comments
  json['description'] = obj.description
  json['draft'] = obj.draft
  json['group'] = obj.group
  json['group_id'] = obj.group_id
  json['id'] = obj.id
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['machine'] = obj.machine
  json['name'] = obj.name
  json['obj_type'] = obj.obj_type
  json['platform'] = obj.platform
  json['preparation_date'] = obj.preparation_date.isoformat() if obj.preparation_date else None
  json['readmode'] = serializeReadmode(obj.readmode) if obj.readmode is not None else None
  json['readmode_id'] = obj.readmode_id
  json['report_url'] = obj.report_url
  json['run_folder'] = obj.run_folder
  json['scientist'] = obj.scientist
  json['scientist_id'] = obj.scientist_id
  json['selfservice'] = obj.selfservice
  json['sequencing_date'] = obj.sequencing_date.isoformat() if obj.sequencing_date else None
  json['status'] = obj.status
  json['username'] = obj.username
  json['vendor_id'] = obj.vendor_id
  json['group_ref'] = serializeGroup(obj.group_ref) if obj.group_ref is not None else None
  json['illumina_run_ref'] = serializeIlluminaRun(obj.illumina_run_ref) if obj.illumina_run_ref is not None else None
  if obj.inventory_changes is not None:
    json['inventory_changes'] = [ serializeInventoryChange(o) for o in obj.inventory_changes ]
  json['machine_ref'] = serializeMachine(obj.machine_ref) if obj.machine_ref is not None else None
  json['ont_run_ref'] = serializeOntRun(obj.ont_run_ref) if obj.ont_run_ref is not None else None
  json['pacbio_run_ref'] = serializePacbioRun(obj.pacbio_run_ref) if obj.pacbio_run_ref is not None else None
  json['platform_ref'] = serializePlatform(obj.platform_ref) if obj.platform_ref is not None else None
  if obj.run_units is not None:
    json['run_units'] = [ serializeRunUnit(o) for o in obj.run_units ]
  json['scientist_ref'] = serializeScientist(obj.scientist_ref) if obj.scientist_ref is not None else None
  json['user_ref'] = serializeScientist(obj.user_ref) if obj.user_ref is not None else None

  return json


@dataclass
class Run:
  comments: typing.Optional[str] = None
  description: typing.Optional[str] = None
  draft: typing.Optional[bool] = None
  group: typing.Optional[typing.Any] = None
  group_id: typing.Optional[typing.Union[int, float]] = None
  id: typing.Optional[typing.Union[int, float]] = None
  last_change: typing.Optional[datetime] = None
  machine: typing.Optional[str] = None
  name: typing.Optional[str] = None
  obj_type: typing.Optional[str] = None
  platform: typing.Optional[str] = None
  preparation_date: typing.Optional[datetime] = None
  readmode: typing.Optional[Readmode] = None
  readmode_id: typing.Optional[typing.Union[int, float]] = None
  report_url: typing.Optional[str] = None
  run_folder: typing.Optional[str] = None
  scientist: typing.Optional[typing.Any] = None
  scientist_id: typing.Optional[typing.Union[int, float]] = None
  selfservice: typing.Optional[bool] = None
  sequencing_date: typing.Optional[datetime] = None
  status: typing.Optional[str] = None
  username: typing.Optional[str] = None
  vendor_id: typing.Optional[str] = None

  
  group_ref: typing.Optional[Group] = None
  illumina_run_ref: typing.Optional[IlluminaRun] = None
  inventory_changes: list[InventoryChange] = field(default_factory=list)
  machine_ref: typing.Optional[Machine] = None
  ont_run_ref: typing.Optional[OntRun] = None
  pacbio_run_ref: typing.Optional[PacbioRun] = None
  platform_ref: typing.Optional[Platform] = None
  run_units: list[RunUnit] = field(default_factory=list)
  scientist_ref: typing.Optional[Scientist] = None
  user_ref: typing.Optional[Scientist] = None


# ---

def plainToRunUnit(json: dict) -> RunUnit:
  obj = RunUnit()
  obj.comments = json.get('comments')
  obj.conc = json.get('conc')
  obj.discount = json.get('discount')
  obj.group = json.get('group')
  obj.invoice_status = json.get('invoice_status')
  obj.is_saved = bool(json.get('is_saved'))
  obj.lane_checks = [ plainToResultCheck(o) for o in json['lane_checks'] ] if json.get('lane_checks') else []
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.needs_demultiplexing = bool(json.get('needs_demultiplexing'))
  obj.run_id = json.get('run_id')
  obj.sample_fields = plainToSampleFields(json['sample_fields']) if json.get('sample_fields') else None
  obj.sampnum = json.get('sampnum')
  obj.scientist = json.get('scientist')
  obj.status = json.get('status')
  obj.unassigned_checks = [ plainToResultCheck(o) for o in json['unassigned_checks'] ] if json.get('unassigned_checks') else []
  obj.unit_id = json.get('unit_id')
  obj.username = json.get('username')
  obj.data_entries = [ plainToDataEntry(o) for o in json['data_entries'] ] if json.get('data_entries') else []
  obj.lane = plainToLane(json['lane']) if json.get('lane') else None
  obj.ont_flowcell_run = plainToOntFlowcellRun(json['ont_flowcell_run']) if json.get('ont_flowcell_run') else None
  obj.result_checks = [ plainToResultCheck(o) for o in json['result_checks'] ] if json.get('result_checks') else []
  obj.run = plainToRun(json['run']) if json.get('run') else None
  obj.sequenced_samples = [ plainToSequencedSample(o) for o in json['sequenced_samples'] ] if json.get('sequenced_samples') else []
  obj.smrtcell = plainToSmrtCell(json['smrtcell']) if json.get('smrtcell') else None
  obj.user_ref = plainToScientist(json['user_ref']) if json.get('user_ref') else None

  return obj

def serializeRunUnit(obj: RunUnit) -> dict:
  json = {}
  json['comments'] = obj.comments
  json['conc'] = obj.conc
  json['discount'] = obj.discount
  json['group'] = obj.group
  json['invoice_status'] = obj.invoice_status
  json['is_saved'] = obj.is_saved
  if obj.lane_checks is not None:
    json['lane_checks'] = [ serializeResultCheck(o) for o in obj.lane_checks ]
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['needs_demultiplexing'] = obj.needs_demultiplexing
  json['run_id'] = obj.run_id
  json['sample_fields'] = serializeSampleFields(obj.sample_fields) if obj.sample_fields is not None else None
  json['sampnum'] = obj.sampnum
  json['scientist'] = obj.scientist
  json['status'] = obj.status
  if obj.unassigned_checks is not None:
    json['unassigned_checks'] = [ serializeResultCheck(o) for o in obj.unassigned_checks ]
  json['unit_id'] = obj.unit_id
  json['username'] = obj.username
  if obj.data_entries is not None:
    json['data_entries'] = [ serializeDataEntry(o) for o in obj.data_entries ]
  json['lane'] = serializeLane(obj.lane) if obj.lane is not None else None
  json['ont_flowcell_run'] = serializeOntFlowcellRun(obj.ont_flowcell_run) if obj.ont_flowcell_run is not None else None
  if obj.result_checks is not None:
    json['result_checks'] = [ serializeResultCheck(o) for o in obj.result_checks ]
  json['run'] = serializeRun(obj.run) if obj.run is not None else None
  if obj.sequenced_samples is not None:
    json['sequenced_samples'] = [ serializeSequencedSample(o) for o in obj.sequenced_samples ]
  json['smrtcell'] = serializeSmrtCell(obj.smrtcell) if obj.smrtcell is not None else None
  json['user_ref'] = serializeScientist(obj.user_ref) if obj.user_ref is not None else None

  return json


@dataclass
class RunUnit:
  comments: typing.Optional[str] = None
  conc: typing.Optional[typing.Any] = None
  discount: typing.Optional[typing.Union[int, float]] = None
  group: typing.Optional[typing.Any] = None
  invoice_status: typing.Optional[str] = None
  is_saved: typing.Optional[bool] = None
  lane_checks: list[ResultCheck]=field(default_factory=list)
  last_change: typing.Optional[datetime] = None
  needs_demultiplexing: typing.Optional[bool] = None
  run_id: typing.Optional[typing.Union[int, float]] = None
  sample_fields: typing.Optional[SampleFields] = None
  sampnum: typing.Optional[typing.Union[int, float]] = None
  scientist: typing.Optional[typing.Any] = None
  status: typing.Optional[str] = None
  unassigned_checks: list[ResultCheck]=field(default_factory=list)
  unit_id: typing.Optional[typing.Union[int, float]] = None
  username: typing.Optional[str] = None

  
  data_entries: list[DataEntry] = field(default_factory=list)
  lane: typing.Optional[Lane] = None
  ont_flowcell_run: typing.Optional[OntFlowcellRun] = None
  result_checks: list[ResultCheck] = field(default_factory=list)
  run: typing.Optional[Run] = None
  sequenced_samples: list[SequencedSample] = field(default_factory=list)
  smrtcell: typing.Optional[SmrtCell] = None
  user_ref: typing.Optional[Scientist] = None


# ---

def plainToSample(json: dict) -> Sample:
  obj = Sample()
  obj._imp_storage = bool(json.get('_imp_storage'))
  obj.adaptor_inline_number = json.get('adaptor_inline_number')
  obj.adaptor_inline_tag = json.get('adaptor_inline_tag')
  obj.adaptor_number = json.get('adaptor_number')
  obj.adaptor_secondary_number = json.get('adaptor_secondary_number')
  obj.adaptor_secondary_tag = json.get('adaptor_secondary_tag')
  obj.adaptor_tag = json.get('adaptor_tag')
  obj.adaptor_type = json.get('adaptor_type')
  obj.antibody = json.get('antibody')
  obj.celltype = json.get('celltype')
  obj.comments = json.get('comments')
  obj.conc = json.get('conc')
  obj.control_for_count = json.get('control_for_count')
  obj.control_type = json.get('control_type')
  obj.cutout_size = json.get('cutout_size')
  obj.cutout_size_max = json.get('cutout_size_max')
  obj.cutout_size_min = json.get('cutout_size_min')
  obj.description = json.get('description')
  obj.exptype = json.get('exptype')
  obj.external_link = json.get('external_link')
  obj.fragment_size = json.get('fragment_size')
  obj.fragmented = bool(json.get('fragmented'))
  obj.genotype = json.get('genotype')
  obj.group = json.get('group')
  obj.group_id = json.get('group_id')
  obj.history = [ plainToTimelineEvent(o) for o in json['history'] ] if json.get('history') else []
  obj.id = json.get('id')
  obj.is_control = json.get('is_control')
  obj.lab_count = json.get('lab_count')
  obj.lab_steps = [ plainToLabStep(o) for o in json['lab_steps'] ] if json.get('lab_steps') else []
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.measurement_count = json.get('measurement_count')
  obj.notes_count = json.get('notes_count')
  obj.obj_id = json.get('obj_id')
  obj.obj_type = json.get('obj_type')
  obj.organism = json.get('organism')
  obj.own_risk = bool(json.get('own_risk'))
  obj.platform = json.get('platform')
  obj.preparation_kit = json.get('preparation_kit')
  obj.preparation_type = json.get('preparation_type')
  obj.primer = json.get('primer')
  obj.ready = datetime.fromisoformat(json.get('ready', '')) if json.get('ready') else None
  obj.received = datetime.fromisoformat(json.get('received', '')) if json.get('received') else None
  obj.request_count = json.get('request_count')
  obj.scientist = json.get('scientist')
  obj.scientist_id = json.get('scientist_id')
  obj.sequencing_count = json.get('sequencing_count')
  obj.status = json.get('status')
  obj.stranded = bool(json.get('stranded'))
  obj.tissue_type = json.get('tissue_type')
  obj.treatment = json.get('treatment')
  obj.user_preparation_kit = json.get('user_preparation_kit')
  obj.volume = json.get('volume')
  obj.adaptor_type_ref = plainToAdaptorType(json['adaptor_type_ref']) if json.get('adaptor_type_ref') else None
  obj.control_for = [ plainToControlSample(o) for o in json['control_for'] ] if json.get('control_for') else []
  obj.control_samples = [ plainToControlSample(o) for o in json['control_samples'] ] if json.get('control_samples') else []
  obj.controls = [ plainToSample(o) for o in json['controls'] ] if json.get('controls') else []
  obj.cutout_size_ref = plainToCutoutSize(json['cutout_size_ref']) if json.get('cutout_size_ref') else None
  obj.data_entries = [ plainToDataEntry(o) for o in json['data_entries'] ] if json.get('data_entries') else []
  obj.group_ref = plainToGroup(json['group_ref']) if json.get('group_ref') else None
  obj.inline_adaptor = plainToTag(json['inline_adaptor']) if json.get('inline_adaptor') else None
  obj.multiplex_samples = [ plainToMultiplexSample(o) for o in json['multiplex_samples'] ] if json.get('multiplex_samples') else []
  obj.notes = [ plainToNote(o) for o in json['notes'] ] if json.get('notes') else []
  obj.platform_ref = plainToPlatform(json['platform_ref']) if json.get('platform_ref') else None
  obj.pool_tags = [ plainToSampleTag(o) for o in json['pool_tags'] ] if json.get('pool_tags') else []
  obj.preparation_kit_ref = plainToPreparationKit(json['preparation_kit_ref']) if json.get('preparation_kit_ref') else None
  obj.preparation_type_ref = plainToPreparationType(json['preparation_type_ref']) if json.get('preparation_type_ref') else None
  obj.primary_adaptor = plainToTag(json['primary_adaptor']) if json.get('primary_adaptor') else None
  obj.primer_ref = plainToPrimer(json['primer_ref']) if json.get('primer_ref') else None
  obj.requests_samples = [ plainToRequestsSample(o) for o in json['requests_samples'] ] if json.get('requests_samples') else []
  obj.scientist_ref = plainToScientist(json['scientist_ref']) if json.get('scientist_ref') else None
  obj.secondary_adaptor = plainToTag(json['secondary_adaptor']) if json.get('secondary_adaptor') else None
  obj.trash_notes = [ plainToNote(o) for o in json['trash_notes'] ] if json.get('trash_notes') else []
  obj.versions = [ plainToObjectVersion(o) for o in json['versions'] ] if json.get('versions') else []

  return obj

def serializeSample(obj: Sample) -> dict:
  json = {}
  json['_imp_storage'] = obj._imp_storage
  json['adaptor_inline_number'] = obj.adaptor_inline_number
  json['adaptor_inline_tag'] = obj.adaptor_inline_tag
  json['adaptor_number'] = obj.adaptor_number
  json['adaptor_secondary_number'] = obj.adaptor_secondary_number
  json['adaptor_secondary_tag'] = obj.adaptor_secondary_tag
  json['adaptor_tag'] = obj.adaptor_tag
  json['adaptor_type'] = obj.adaptor_type
  json['antibody'] = obj.antibody
  json['celltype'] = obj.celltype
  json['comments'] = obj.comments
  json['conc'] = obj.conc
  json['control_for_count'] = obj.control_for_count
  json['control_type'] = obj.control_type
  json['cutout_size'] = obj.cutout_size
  json['cutout_size_max'] = obj.cutout_size_max
  json['cutout_size_min'] = obj.cutout_size_min
  json['description'] = obj.description
  json['exptype'] = obj.exptype
  json['external_link'] = obj.external_link
  json['fragment_size'] = obj.fragment_size
  json['fragmented'] = obj.fragmented
  json['genotype'] = obj.genotype
  json['group'] = obj.group
  json['group_id'] = obj.group_id
  if obj.history is not None:
    json['history'] = [ serializeTimelineEvent(o) for o in obj.history ]
  json['id'] = obj.id
  json['is_control'] = obj.is_control
  json['lab_count'] = obj.lab_count
  if obj.lab_steps is not None:
    json['lab_steps'] = [ serializeLabStep(o) for o in obj.lab_steps ]
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['measurement_count'] = obj.measurement_count
  json['notes_count'] = obj.notes_count
  json['obj_id'] = obj.obj_id
  json['obj_type'] = obj.obj_type
  json['organism'] = obj.organism
  json['own_risk'] = obj.own_risk
  json['platform'] = obj.platform
  json['preparation_kit'] = obj.preparation_kit
  json['preparation_type'] = obj.preparation_type
  json['primer'] = obj.primer
  json['ready'] = obj.ready.isoformat() if obj.ready else None
  json['received'] = obj.received.isoformat() if obj.received else None
  json['request_count'] = obj.request_count
  json['scientist'] = obj.scientist
  json['scientist_id'] = obj.scientist_id
  json['sequencing_count'] = obj.sequencing_count
  json['status'] = obj.status
  json['stranded'] = obj.stranded
  json['tissue_type'] = obj.tissue_type
  json['treatment'] = obj.treatment
  json['user_preparation_kit'] = obj.user_preparation_kit
  json['volume'] = obj.volume
  json['adaptor_type_ref'] = serializeAdaptorType(obj.adaptor_type_ref) if obj.adaptor_type_ref is not None else None
  if obj.control_for is not None:
    json['control_for'] = [ serializeControlSample(o) for o in obj.control_for ]
  if obj.control_samples is not None:
    json['control_samples'] = [ serializeControlSample(o) for o in obj.control_samples ]
  if obj.controls is not None:
    json['controls'] = [ serializeSample(o) for o in obj.controls ]
  json['cutout_size_ref'] = serializeCutoutSize(obj.cutout_size_ref) if obj.cutout_size_ref is not None else None
  if obj.data_entries is not None:
    json['data_entries'] = [ serializeDataEntry(o) for o in obj.data_entries ]
  json['group_ref'] = serializeGroup(obj.group_ref) if obj.group_ref is not None else None
  json['inline_adaptor'] = serializeTag(obj.inline_adaptor) if obj.inline_adaptor is not None else None
  if obj.multiplex_samples is not None:
    json['multiplex_samples'] = [ serializeMultiplexSample(o) for o in obj.multiplex_samples ]
  if obj.notes is not None:
    json['notes'] = [ serializeNote(o) for o in obj.notes ]
  json['platform_ref'] = serializePlatform(obj.platform_ref) if obj.platform_ref is not None else None
  if obj.pool_tags is not None:
    json['pool_tags'] = [ serializeSampleTag(o) for o in obj.pool_tags ]
  json['preparation_kit_ref'] = serializePreparationKit(obj.preparation_kit_ref) if obj.preparation_kit_ref is not None else None
  json['preparation_type_ref'] = serializePreparationType(obj.preparation_type_ref) if obj.preparation_type_ref is not None else None
  json['primary_adaptor'] = serializeTag(obj.primary_adaptor) if obj.primary_adaptor is not None else None
  json['primer_ref'] = serializePrimer(obj.primer_ref) if obj.primer_ref is not None else None
  if obj.requests_samples is not None:
    json['requests_samples'] = [ serializeRequestsSample(o) for o in obj.requests_samples ]
  json['scientist_ref'] = serializeScientist(obj.scientist_ref) if obj.scientist_ref is not None else None
  json['secondary_adaptor'] = serializeTag(obj.secondary_adaptor) if obj.secondary_adaptor is not None else None
  if obj.trash_notes is not None:
    json['trash_notes'] = [ serializeNote(o) for o in obj.trash_notes ]
  if obj.versions is not None:
    json['versions'] = [ serializeObjectVersion(o) for o in obj.versions ]

  return json


@dataclass
class Sample:
  _imp_storage: typing.Optional[bool] = None
  adaptor_inline_number: typing.Optional[typing.Union[int, float]] = None
  adaptor_inline_tag: typing.Optional[str] = None
  adaptor_number: typing.Optional[typing.Union[int, float]] = None
  adaptor_secondary_number: typing.Optional[typing.Union[int, float]] = None
  adaptor_secondary_tag: typing.Optional[str] = None
  adaptor_tag: typing.Optional[str] = None
  adaptor_type: typing.Optional[str] = None
  antibody: typing.Optional[str] = None
  celltype: typing.Optional[str] = None
  comments: typing.Optional[str] = None
  conc: typing.Optional[typing.Any] = None
  control_for_count: typing.Optional[typing.Union[int, float]] = None
  control_type: typing.Optional[str] = None
  cutout_size: typing.Optional[str] = None
  cutout_size_max: typing.Optional[typing.Any] = None
  cutout_size_min: typing.Optional[typing.Any] = None
  description: typing.Optional[str] = None
  exptype: typing.Optional[str] = None
  external_link: typing.Optional[str] = None
  fragment_size: typing.Optional[str] = None
  fragmented: typing.Optional[bool] = None
  genotype: typing.Optional[str] = None
  group: typing.Optional[typing.Any] = None
  group_id: typing.Optional[typing.Union[int, float]] = None
  history: list[TimelineEvent]=field(default_factory=list)
  id: typing.Optional[typing.Union[int, float]] = None
  is_control: typing.Optional[typing.Any] = None
  lab_count: typing.Optional[typing.Union[int, float]] = None
  lab_steps: list[LabStep]=field(default_factory=list)
  last_change: typing.Optional[datetime] = None
  measurement_count: typing.Optional[typing.Union[int, float]] = None
  notes_count: typing.Optional[typing.Union[int, float]] = None
  obj_id: typing.Optional[typing.Union[int, float]] = None
  obj_type: typing.Optional[str] = None
  organism: typing.Optional[str] = None
  own_risk: typing.Optional[bool] = None
  platform: typing.Optional[str] = None
  preparation_kit: typing.Optional[str] = None
  preparation_type: typing.Optional[str] = None
  primer: typing.Optional[str] = None
  ready: typing.Optional[datetime] = None
  received: typing.Optional[datetime] = None
  request_count: typing.Optional[typing.Union[int, float]] = None
  scientist: typing.Optional[typing.Any] = None
  scientist_id: typing.Optional[typing.Union[int, float]] = None
  sequencing_count: typing.Optional[typing.Union[int, float]] = None
  status: typing.Optional[str] = None
  stranded: typing.Optional[bool] = None
  tissue_type: typing.Optional[str] = None
  treatment: typing.Optional[str] = None
  user_preparation_kit: typing.Optional[str] = None
  volume: typing.Optional[typing.Any] = None

  
  adaptor_type_ref: typing.Optional[AdaptorType] = None
  control_for: list[ControlSample] = field(default_factory=list)
  control_samples: list[ControlSample] = field(default_factory=list)
  controls: list[Sample] = field(default_factory=list)
  cutout_size_ref: typing.Optional[CutoutSize] = None
  data_entries: list[DataEntry] = field(default_factory=list)
  group_ref: typing.Optional[Group] = None
  inline_adaptor: typing.Optional[Tag] = None
  multiplex_samples: list[MultiplexSample] = field(default_factory=list)
  notes: list[Note] = field(default_factory=list)
  platform_ref: typing.Optional[Platform] = None
  pool_tags: list[SampleTag] = field(default_factory=list)
  preparation_kit_ref: typing.Optional[PreparationKit] = None
  preparation_type_ref: typing.Optional[PreparationType] = None
  primary_adaptor: typing.Optional[Tag] = None
  primer_ref: typing.Optional[Primer] = None
  requests_samples: list[RequestsSample] = field(default_factory=list)
  scientist_ref: typing.Optional[Scientist] = None
  secondary_adaptor: typing.Optional[Tag] = None
  trash_notes: list[Note] = field(default_factory=list)
  versions: list[ObjectVersion] = field(default_factory=list)


# ---

def plainToSampleList(json: dict) -> SampleList:
  obj = SampleList()
  obj.created = datetime.fromisoformat(json.get('created', '')) if json.get('created') else None
  obj.id = json.get('id')
  obj.ids = json.get('ids')
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.last_change_username = json.get('last_change_username')
  obj.title = json.get('title')
  obj.username = json.get('username')
  obj.last_change_user_ref = plainToScientist(json['last_change_user_ref']) if json.get('last_change_user_ref') else None
  obj.user_ref = plainToScientist(json['user_ref']) if json.get('user_ref') else None

  return obj

def serializeSampleList(obj: SampleList) -> dict:
  json = {}
  json['created'] = obj.created.isoformat() if obj.created else None
  json['id'] = obj.id
  json['ids'] = obj.ids
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['last_change_username'] = obj.last_change_username
  json['title'] = obj.title
  json['username'] = obj.username
  json['last_change_user_ref'] = serializeScientist(obj.last_change_user_ref) if obj.last_change_user_ref is not None else None
  json['user_ref'] = serializeScientist(obj.user_ref) if obj.user_ref is not None else None

  return json


@dataclass
class SampleList:
  created: typing.Optional[datetime] = None
  id: typing.Optional[typing.Union[int, float]] = None
  ids: typing.Optional[dict] = None
  last_change: typing.Optional[datetime] = None
  last_change_username: typing.Optional[str] = None
  title: typing.Optional[str] = None
  username: typing.Optional[str] = None

  
  last_change_user_ref: typing.Optional[Scientist] = None
  user_ref: typing.Optional[Scientist] = None


# ---

def plainToSampleTag(json: dict) -> SampleTag:
  obj = SampleTag()
  obj.adaptor_inline_number = json.get('adaptor_inline_number')
  obj.adaptor_number = json.get('adaptor_number')
  obj.adaptor_secondary_number = json.get('adaptor_secondary_number')
  obj.adaptor_secondary_tag = json.get('adaptor_secondary_tag')
  obj.adaptor_tag = json.get('adaptor_tag')
  obj.adaptor_type = json.get('adaptor_type')
  obj.description = json.get('description')
  obj.id = json.get('id')
  obj.ratio = json.get('ratio')
  obj.sample_id = json.get('sample_id')
  obj.inline_adaptor = plainToTag(json['inline_adaptor']) if json.get('inline_adaptor') else None
  obj.primary_adaptor = plainToTag(json['primary_adaptor']) if json.get('primary_adaptor') else None
  obj.sample = plainToSample(json['sample']) if json.get('sample') else None
  obj.secondary_adaptor = plainToTag(json['secondary_adaptor']) if json.get('secondary_adaptor') else None

  return obj

def serializeSampleTag(obj: SampleTag) -> dict:
  json = {}
  json['adaptor_inline_number'] = obj.adaptor_inline_number
  json['adaptor_number'] = obj.adaptor_number
  json['adaptor_secondary_number'] = obj.adaptor_secondary_number
  json['adaptor_secondary_tag'] = obj.adaptor_secondary_tag
  json['adaptor_tag'] = obj.adaptor_tag
  json['adaptor_type'] = obj.adaptor_type
  json['description'] = obj.description
  json['id'] = obj.id
  json['ratio'] = obj.ratio
  json['sample_id'] = obj.sample_id
  json['inline_adaptor'] = serializeTag(obj.inline_adaptor) if obj.inline_adaptor is not None else None
  json['primary_adaptor'] = serializeTag(obj.primary_adaptor) if obj.primary_adaptor is not None else None
  json['sample'] = serializeSample(obj.sample) if obj.sample is not None else None
  json['secondary_adaptor'] = serializeTag(obj.secondary_adaptor) if obj.secondary_adaptor is not None else None

  return json


@dataclass
class SampleTag:
  adaptor_inline_number: typing.Optional[typing.Union[int, float]] = None
  adaptor_number: typing.Optional[typing.Union[int, float]] = None
  adaptor_secondary_number: typing.Optional[typing.Union[int, float]] = None
  adaptor_secondary_tag: typing.Optional[str] = None
  adaptor_tag: typing.Optional[str] = None
  adaptor_type: typing.Optional[str] = None
  description: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  ratio: typing.Optional[typing.Union[int, float]] = None
  sample_id: typing.Optional[typing.Union[int, float]] = None

  
  inline_adaptor: typing.Optional[Tag] = None
  primary_adaptor: typing.Optional[Tag] = None
  sample: typing.Optional[Sample] = None
  secondary_adaptor: typing.Optional[Tag] = None


# ---

def plainToSamplestat(json: dict) -> Samplestat:
  obj = Samplestat()
  obj.alignment_rate = json.get('alignment_rate')
  obj.barcode = json.get('barcode')
  obj.basecalls = json.get('basecalls')
  obj.bc_best_filter = json.get('bc_best_filter')
  obj.bc_best_unique_rate = json.get('bc_best_unique_rate')
  obj.bc_hit_rate = json.get('bc_hit_rate')
  obj.date = datetime.fromisoformat(json.get('date', '')) if json.get('date') else None
  obj.file = json.get('file')
  obj.flowcell = json.get('flowcell')
  obj.id = json.get('id')
  obj.lane = json.get('lane')
  obj.library_diversity = json.get('library_diversity')
  obj.library_saturation = json.get('library_saturation')
  obj.path = json.get('path')
  obj.result_check_id = json.get('result_check_id')
  obj.run_id = json.get('run_id')
  obj.taxo_guess = json.get('taxo_guess')
  obj.result_check = plainToResultCheck(json['result_check']) if json.get('result_check') else None

  return obj

def serializeSamplestat(obj: Samplestat) -> dict:
  json = {}
  json['alignment_rate'] = obj.alignment_rate
  json['barcode'] = obj.barcode
  json['basecalls'] = obj.basecalls
  json['bc_best_filter'] = obj.bc_best_filter
  json['bc_best_unique_rate'] = obj.bc_best_unique_rate
  json['bc_hit_rate'] = obj.bc_hit_rate
  json['date'] = obj.date.isoformat() if obj.date else None
  json['file'] = obj.file
  json['flowcell'] = obj.flowcell
  json['id'] = obj.id
  json['lane'] = obj.lane
  json['library_diversity'] = obj.library_diversity
  json['library_saturation'] = obj.library_saturation
  json['path'] = obj.path
  json['result_check_id'] = obj.result_check_id
  json['run_id'] = obj.run_id
  json['taxo_guess'] = obj.taxo_guess
  json['result_check'] = serializeResultCheck(obj.result_check) if obj.result_check is not None else None

  return json


@dataclass
class Samplestat:
  alignment_rate: typing.Optional[typing.Any] = None
  barcode: typing.Optional[str] = None
  basecalls: typing.Optional[str] = None
  bc_best_filter: typing.Optional[str] = None
  bc_best_unique_rate: typing.Optional[typing.Any] = None
  bc_hit_rate: typing.Optional[typing.Any] = None
  date: typing.Optional[datetime] = None
  file: typing.Optional[str] = None
  flowcell: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  lane: typing.Optional[typing.Union[int, float]] = None
  library_diversity: typing.Optional[typing.Any] = None
  library_saturation: typing.Optional[typing.Any] = None
  path: typing.Optional[str] = None
  result_check_id: typing.Optional[typing.Union[int, float]] = None
  run_id: typing.Optional[typing.Union[int, float]] = None
  taxo_guess: typing.Optional[str] = None

  
  result_check: typing.Optional[ResultCheck] = None


# ---

def plainToScientist(json: dict) -> Scientist:
  obj = Scientist()
  obj.active = bool(json.get('active'))
  obj.announce_subscribed = bool(json.get('announce_subscribed'))
  obj.created = datetime.fromisoformat(json.get('created', '')) if json.get('created') else None
  obj.delivery = json.get('delivery')
  obj.email = json.get('email')
  obj.firstname = json.get('firstname')
  obj.id = json.get('id')
  obj.imp_galaxy_username = json.get('imp_galaxy_username')
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.last_login = datetime.fromisoformat(json.get('last_login', '')) if json.get('last_login') else None
  obj.lastname = json.get('lastname')
  obj.login_failed = json.get('login_failed')
  obj.login_ok = json.get('login_ok')
  obj.obj_id = json.get('obj_id')
  obj.obj_type = json.get('obj_type')
  obj.previous_login = datetime.fromisoformat(json.get('previous_login', '')) if json.get('previous_login') else None
  obj.primary_group_id = json.get('primary_group_id')
  obj.reviewed = bool(json.get('reviewed'))
  obj.username = json.get('username')
  obj.api_keys = [ plainToApiKey(o) for o in json['api_keys'] ] if json.get('api_keys') else []
  obj.multiplexes = [ plainToMultiplex(o) for o in json['multiplexes'] ] if json.get('multiplexes') else []
  obj.notes = [ plainToNote(o) for o in json['notes'] ] if json.get('notes') else []
  obj.primary_group = plainToGroup(json['primary_group']) if json.get('primary_group') else None
  obj.projects = [ plainToProject(o) for o in json['projects'] ] if json.get('projects') else []
  obj.request_drafts = [ plainToRequestDraft(o) for o in json['request_drafts'] ] if json.get('request_drafts') else []
  obj.requests = [ plainToRequest(o) for o in json['requests'] ] if json.get('requests') else []
  obj.samples = [ plainToSample(o) for o in json['samples'] ] if json.get('samples') else []

  obj.is_admin = bool(json.get('is_admin'))
  obj.groups = [ plainToGroup(o) for o in json['groups'] ] if json.get('groups') else []

  return obj

def serializeScientist(obj: Scientist) -> dict:
  json = {}
  json['active'] = obj.active
  json['announce_subscribed'] = obj.announce_subscribed
  json['created'] = obj.created.isoformat() if obj.created else None
  json['delivery'] = obj.delivery
  json['email'] = obj.email
  json['firstname'] = obj.firstname
  json['id'] = obj.id
  json['imp_galaxy_username'] = obj.imp_galaxy_username
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['last_login'] = obj.last_login.isoformat() if obj.last_login else None
  json['lastname'] = obj.lastname
  json['login_failed'] = obj.login_failed
  json['login_ok'] = obj.login_ok
  json['obj_id'] = obj.obj_id
  json['obj_type'] = obj.obj_type
  json['previous_login'] = obj.previous_login.isoformat() if obj.previous_login else None
  json['primary_group_id'] = obj.primary_group_id
  json['reviewed'] = obj.reviewed
  json['username'] = obj.username
  if obj.api_keys is not None:
    json['api_keys'] = [ serializeApiKey(o) for o in obj.api_keys ]
  if obj.multiplexes is not None:
    json['multiplexes'] = [ serializeMultiplex(o) for o in obj.multiplexes ]
  if obj.notes is not None:
    json['notes'] = [ serializeNote(o) for o in obj.notes ]
  json['primary_group'] = serializeGroup(obj.primary_group) if obj.primary_group is not None else None
  if obj.projects is not None:
    json['projects'] = [ serializeProject(o) for o in obj.projects ]
  if obj.request_drafts is not None:
    json['request_drafts'] = [ serializeRequestDraft(o) for o in obj.request_drafts ]
  if obj.requests is not None:
    json['requests'] = [ serializeRequest(o) for o in obj.requests ]
  if obj.samples is not None:
    json['samples'] = [ serializeSample(o) for o in obj.samples ]

  json['groups'] = [ serializeGroup(g) for g in obj.groups ]
  json['is_admin'] = obj.is_admin
  return json


@dataclass
class Scientist:
  active: typing.Optional[bool] = None
  announce_subscribed: typing.Optional[bool] = None
  created: typing.Optional[datetime] = None
  delivery: typing.Optional[str] = None
  email: typing.Optional[str] = None
  firstname: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  imp_galaxy_username: typing.Optional[str] = None
  last_change: typing.Optional[datetime] = None
  last_login: typing.Optional[datetime] = None
  lastname: typing.Optional[str] = None
  login_failed: typing.Optional[typing.Union[int, float]] = None
  login_ok: typing.Optional[typing.Union[int, float]] = None
  obj_id: typing.Optional[typing.Union[int, float]] = None
  obj_type: typing.Optional[str] = None
  previous_login: typing.Optional[datetime] = None
  primary_group_id: typing.Optional[typing.Union[int, float]] = None
  reviewed: typing.Optional[bool] = None
  username: typing.Optional[str] = None

  
  api_keys: list[ApiKey] = field(default_factory=list)
  multiplexes: list[Multiplex] = field(default_factory=list)
  notes: list[Note] = field(default_factory=list)
  primary_group: typing.Optional[Group] = None
  projects: list[Project] = field(default_factory=list)
  request_drafts: list[RequestDraft] = field(default_factory=list)
  requests: list[Request] = field(default_factory=list)
  samples: list[Sample] = field(default_factory=list)


  is_admin: bool = False
  groups: list[Group] = field(default_factory=list)

  @property
  def fullname(self) -> str:
    return f"{self.firstname} {self.lastname}"

# ---

def plainToSequencedSample(json: dict) -> SequencedSample:
  obj = SequencedSample()
  obj.comments = json.get('comments')
  obj.conc = json.get('conc')
  obj.id = json.get('id')
  obj.is_repetition = bool(json.get('is_repetition'))
  obj.is_spikein = bool(json.get('is_spikein'))
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.multi_id = json.get('multi_id')
  obj.reqsamp_id = json.get('reqsamp_id')
  obj.run_id = json.get('run_id')
  obj.status = json.get('status')
  obj.unit_id = json.get('unit_id')
  obj.multi = plainToMultiplex(json['multi']) if json.get('multi') else None
  obj.request_sample = plainToRequestsSample(json['request_sample']) if json.get('request_sample') else None
  obj.result_checks = [ plainToResultCheck(o) for o in json['result_checks'] ] if json.get('result_checks') else []
  obj.run = plainToRun(json['run']) if json.get('run') else None
  obj.run_unit = plainToRunUnit(json['run_unit']) if json.get('run_unit') else None

  return obj

def serializeSequencedSample(obj: SequencedSample) -> dict:
  json = {}
  json['comments'] = obj.comments
  json['conc'] = obj.conc
  json['id'] = obj.id
  json['is_repetition'] = obj.is_repetition
  json['is_spikein'] = obj.is_spikein
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['multi_id'] = obj.multi_id
  json['reqsamp_id'] = obj.reqsamp_id
  json['run_id'] = obj.run_id
  json['status'] = obj.status
  json['unit_id'] = obj.unit_id
  json['multi'] = serializeMultiplex(obj.multi) if obj.multi is not None else None
  json['request_sample'] = serializeRequestsSample(obj.request_sample) if obj.request_sample is not None else None
  if obj.result_checks is not None:
    json['result_checks'] = [ serializeResultCheck(o) for o in obj.result_checks ]
  json['run'] = serializeRun(obj.run) if obj.run is not None else None
  json['run_unit'] = serializeRunUnit(obj.run_unit) if obj.run_unit is not None else None

  return json


@dataclass
class SequencedSample:
  comments: typing.Optional[str] = None
  conc: typing.Optional[typing.Union[int, float]] = None
  id: typing.Optional[typing.Union[int, float]] = None
  is_repetition: typing.Optional[bool] = None
  is_spikein: typing.Optional[bool] = None
  last_change: typing.Optional[datetime] = None
  multi_id: typing.Optional[typing.Union[int, float]] = None
  reqsamp_id: typing.Optional[typing.Union[int, float]] = None
  run_id: typing.Optional[typing.Union[int, float]] = None
  status: typing.Optional[str] = None
  unit_id: typing.Optional[typing.Union[int, float]] = None

  
  multi: typing.Optional[Multiplex] = None
  request_sample: typing.Optional[RequestsSample] = None
  result_checks: list[ResultCheck] = field(default_factory=list)
  run: typing.Optional[Run] = None
  run_unit: typing.Optional[RunUnit] = None


# ---

def plainToSmrtCell(json: dict) -> SmrtCell:
  obj = SmrtCell()
  obj.binding_kit = json.get('binding_kit')
  obj.cell_pac = json.get('cell_pac')
  obj.comments = json.get('comments')
  obj.conc = json.get('conc')
  obj.concentration = json.get('concentration')
  obj.context = json.get('context')
  obj.control_kit = json.get('control_kit')
  obj.datafiles_created = datetime.fromisoformat(json.get('datafiles_created', '')) if json.get('datafiles_created') else None
  obj.datafiles_hash = json.get('datafiles_hash')
  obj.datafiles_id = json.get('datafiles_id')
  obj.datafiles_link = json.get('datafiles_link')
  obj.datafiles_path = json.get('datafiles_path')
  obj.datafiles_size = json.get('datafiles_size')
  obj.datafiles_url = json.get('datafiles_url')
  obj.demultiplexed = datetime.fromisoformat(json.get('demultiplexed', '')) if json.get('demultiplexed') else None
  obj.discount = json.get('discount')
  obj.extend_first = bool(json.get('extend_first'))
  obj.extension_time = json.get('extension_time')
  obj.group = json.get('group')
  obj.immobilization_time = json.get('immobilization_time')
  obj.insert_size = json.get('insert_size')
  obj.invoice_status = json.get('invoice_status')
  obj.is_saved = bool(json.get('is_saved'))
  obj.lane_checks = [ plainToResultCheck(o) for o in json['lane_checks'] ] if json.get('lane_checks') else []
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.magbead_loading = bool(json.get('magbead_loading'))
  obj.movie_time = json.get('movie_time')
  obj.name = json.get('name')
  obj.needs_demultiplexing = bool(json.get('needs_demultiplexing'))
  obj.output_folder = json.get('output_folder')
  obj.processed = datetime.fromisoformat(json.get('processed', '')) if json.get('processed') else None
  obj.report_url = json.get('report_url')
  obj.run_id = json.get('run_id')
  obj.sample_fields = plainToSampleFields(json['sample_fields']) if json.get('sample_fields') else None
  obj.sampnum = json.get('sampnum')
  obj.scientist = json.get('scientist')
  obj.sequencing_kit = json.get('sequencing_kit')
  obj.status = json.get('status')
  obj.subreads = json.get('subreads')
  obj.template_prep_kit = json.get('template_prep_kit')
  obj.unassigned_checks = [ plainToResultCheck(o) for o in json['unassigned_checks'] ] if json.get('unassigned_checks') else []
  obj.unique_id = json.get('unique_id')
  obj.unit_id = json.get('unit_id')
  obj.username = json.get('username')
  obj.well = json.get('well')
  obj.pacbio_run = plainToPacbioRun(json['pacbio_run']) if json.get('pacbio_run') else None
  obj.run_ref = plainToRun(json['run_ref']) if json.get('run_ref') else None
  obj.run_unit = plainToRunUnit(json['run_unit']) if json.get('run_unit') else None
  obj.sequenced_samples = [ plainToSequencedSample(o) for o in json['sequenced_samples'] ] if json.get('sequenced_samples') else []

  obj.objects = json.get('objects', {})
  return obj

def serializeSmrtCell(obj: SmrtCell) -> dict:
  json = {}
  json['binding_kit'] = obj.binding_kit
  json['cell_pac'] = obj.cell_pac
  json['comments'] = obj.comments
  json['conc'] = obj.conc
  json['concentration'] = obj.concentration
  json['context'] = obj.context
  json['control_kit'] = obj.control_kit
  json['datafiles_created'] = obj.datafiles_created.isoformat() if obj.datafiles_created else None
  json['datafiles_hash'] = obj.datafiles_hash
  json['datafiles_id'] = obj.datafiles_id
  json['datafiles_link'] = obj.datafiles_link
  json['datafiles_path'] = obj.datafiles_path
  json['datafiles_size'] = obj.datafiles_size
  json['datafiles_url'] = obj.datafiles_url
  json['demultiplexed'] = obj.demultiplexed.isoformat() if obj.demultiplexed else None
  json['discount'] = obj.discount
  json['extend_first'] = obj.extend_first
  json['extension_time'] = obj.extension_time
  json['group'] = obj.group
  json['immobilization_time'] = obj.immobilization_time
  json['insert_size'] = obj.insert_size
  json['invoice_status'] = obj.invoice_status
  json['is_saved'] = obj.is_saved
  if obj.lane_checks is not None:
    json['lane_checks'] = [ serializeResultCheck(o) for o in obj.lane_checks ]
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['magbead_loading'] = obj.magbead_loading
  json['movie_time'] = obj.movie_time
  json['name'] = obj.name
  json['needs_demultiplexing'] = obj.needs_demultiplexing
  json['output_folder'] = obj.output_folder
  json['processed'] = obj.processed.isoformat() if obj.processed else None
  json['report_url'] = obj.report_url
  json['run_id'] = obj.run_id
  json['sample_fields'] = serializeSampleFields(obj.sample_fields) if obj.sample_fields is not None else None
  json['sampnum'] = obj.sampnum
  json['scientist'] = obj.scientist
  json['sequencing_kit'] = obj.sequencing_kit
  json['status'] = obj.status
  json['subreads'] = obj.subreads
  json['template_prep_kit'] = obj.template_prep_kit
  if obj.unassigned_checks is not None:
    json['unassigned_checks'] = [ serializeResultCheck(o) for o in obj.unassigned_checks ]
  json['unique_id'] = obj.unique_id
  json['unit_id'] = obj.unit_id
  json['username'] = obj.username
  json['well'] = obj.well
  json['pacbio_run'] = serializePacbioRun(obj.pacbio_run) if obj.pacbio_run is not None else None
  json['run_ref'] = serializeRun(obj.run_ref) if obj.run_ref is not None else None
  json['run_unit'] = serializeRunUnit(obj.run_unit) if obj.run_unit is not None else None
  if obj.sequenced_samples is not None:
    json['sequenced_samples'] = [ serializeSequencedSample(o) for o in obj.sequenced_samples ]

  return json


@dataclass
class SmrtCell:
  binding_kit: typing.Optional[str] = None
  cell_pac: typing.Optional[str] = None
  comments: typing.Optional[str] = None
  conc: typing.Optional[typing.Any] = None
  concentration: typing.Optional[typing.Union[int, float]] = None
  context: typing.Optional[str] = None
  control_kit: typing.Optional[str] = None
  datafiles_created: typing.Optional[datetime] = None
  datafiles_hash: typing.Optional[str] = None
  datafiles_id: typing.Optional[typing.Union[int, float]] = None
  datafiles_link: typing.Optional[str] = None
  datafiles_path: typing.Optional[str] = None
  datafiles_size: typing.Optional[typing.Any] = None
  datafiles_url: typing.Optional[str] = None
  demultiplexed: typing.Optional[datetime] = None
  discount: typing.Optional[typing.Union[int, float]] = None
  extend_first: typing.Optional[bool] = None
  extension_time: typing.Optional[typing.Union[int, float]] = None
  group: typing.Optional[typing.Any] = None
  immobilization_time: typing.Optional[typing.Union[int, float]] = None
  insert_size: typing.Optional[typing.Union[int, float]] = None
  invoice_status: typing.Optional[str] = None
  is_saved: typing.Optional[bool] = None
  lane_checks: list[ResultCheck]=field(default_factory=list)
  last_change: typing.Optional[datetime] = None
  magbead_loading: typing.Optional[bool] = None
  movie_time: typing.Optional[typing.Union[int, float]] = None
  name: typing.Optional[str] = None
  needs_demultiplexing: typing.Optional[bool] = None
  output_folder: typing.Optional[str] = None
  processed: typing.Optional[datetime] = None
  report_url: typing.Optional[str] = None
  run_id: typing.Optional[typing.Union[int, float]] = None
  sample_fields: typing.Optional[SampleFields] = None
  sampnum: typing.Optional[typing.Union[int, float]] = None
  scientist: typing.Optional[typing.Any] = None
  sequencing_kit: typing.Optional[str] = None
  status: typing.Optional[str] = None
  subreads: typing.Optional[str] = None
  template_prep_kit: typing.Optional[str] = None
  unassigned_checks: list[ResultCheck]=field(default_factory=list)
  unique_id: typing.Optional[str] = None
  unit_id: typing.Optional[typing.Union[int, float]] = None
  username: typing.Optional[str] = None
  well: typing.Optional[str] = None

  
  pacbio_run: typing.Optional[PacbioRun] = None
  run_ref: typing.Optional[Run] = None
  run_unit: typing.Optional[RunUnit] = None
  sequenced_samples: list[SequencedSample] = field(default_factory=list)

  objects: typing.Any = None

# ---

def plainToSubreadstat(json: dict) -> Subreadstat:
  obj = Subreadstat()
  obj.barcode = json.get('barcode')
  obj.basepairs = json.get('basepairs')
  obj.bc1 = json.get('bc1')
  obj.bc2 = json.get('bc2')
  obj.bc_best_filter = json.get('bc_best_filter')
  obj.bc_best_unique_rate = json.get('bc_best_unique_rate')
  obj.bc_hit_rate = json.get('bc_hit_rate')
  obj.bq_hqreads = json.get('bq_hqreads')
  obj.bq_mode = json.get('bq_mode')
  obj.created = datetime.fromisoformat(json.get('created', '')) if json.get('created') else None
  obj.id = json.get('id')
  obj.last_change = datetime.fromisoformat(json.get('last_change', '')) if json.get('last_change') else None
  obj.loading_p0 = json.get('loading_p0')
  obj.loading_p1 = json.get('loading_p1')
  obj.loading_p2 = json.get('loading_p2')
  obj.mean_gc = json.get('mean_gc')
  obj.mean_length = json.get('mean_length')
  obj.median_length = json.get('median_length')
  obj.n50_length = json.get('n50_length')
  obj.path = json.get('path')
  obj.reads = json.get('reads')
  obj.result_check_id = json.get('result_check_id')
  obj.run_id = json.get('run_id')
  obj.run_unique_id = json.get('run_unique_id')
  obj.smrtcell_unique_id = json.get('smrtcell_unique_id')
  obj.unit_id = json.get('unit_id')
  obj.pacbio_run = plainToPacbioRun(json['pacbio_run']) if json.get('pacbio_run') else None
  obj.result_check = plainToResultCheck(json['result_check']) if json.get('result_check') else None
  obj.run = plainToRun(json['run']) if json.get('run') else None
  obj.run_unit = plainToRunUnit(json['run_unit']) if json.get('run_unit') else None
  obj.smrtcell = plainToSmrtCell(json['smrtcell']) if json.get('smrtcell') else None

  return obj

def serializeSubreadstat(obj: Subreadstat) -> dict:
  json = {}
  json['barcode'] = obj.barcode
  json['basepairs'] = obj.basepairs
  json['bc1'] = obj.bc1
  json['bc2'] = obj.bc2
  json['bc_best_filter'] = obj.bc_best_filter
  json['bc_best_unique_rate'] = obj.bc_best_unique_rate
  json['bc_hit_rate'] = obj.bc_hit_rate
  json['bq_hqreads'] = obj.bq_hqreads
  json['bq_mode'] = obj.bq_mode
  json['created'] = obj.created.isoformat() if obj.created else None
  json['id'] = obj.id
  json['last_change'] = obj.last_change.isoformat() if obj.last_change else None
  json['loading_p0'] = obj.loading_p0
  json['loading_p1'] = obj.loading_p1
  json['loading_p2'] = obj.loading_p2
  json['mean_gc'] = obj.mean_gc
  json['mean_length'] = obj.mean_length
  json['median_length'] = obj.median_length
  json['n50_length'] = obj.n50_length
  json['path'] = obj.path
  json['reads'] = obj.reads
  json['result_check_id'] = obj.result_check_id
  json['run_id'] = obj.run_id
  json['run_unique_id'] = obj.run_unique_id
  json['smrtcell_unique_id'] = obj.smrtcell_unique_id
  json['unit_id'] = obj.unit_id
  json['pacbio_run'] = serializePacbioRun(obj.pacbio_run) if obj.pacbio_run is not None else None
  json['result_check'] = serializeResultCheck(obj.result_check) if obj.result_check is not None else None
  json['run'] = serializeRun(obj.run) if obj.run is not None else None
  json['run_unit'] = serializeRunUnit(obj.run_unit) if obj.run_unit is not None else None
  json['smrtcell'] = serializeSmrtCell(obj.smrtcell) if obj.smrtcell is not None else None

  return json


@dataclass
class Subreadstat:
  barcode: typing.Optional[str] = None
  basepairs: typing.Optional[typing.Any] = None
  bc1: typing.Optional[str] = None
  bc2: typing.Optional[str] = None
  bc_best_filter: typing.Optional[str] = None
  bc_best_unique_rate: typing.Optional[typing.Any] = None
  bc_hit_rate: typing.Optional[typing.Any] = None
  bq_hqreads: typing.Optional[typing.Any] = None
  bq_mode: typing.Optional[typing.Any] = None
  created: typing.Optional[datetime] = None
  id: typing.Optional[typing.Union[int, float]] = None
  last_change: typing.Optional[datetime] = None
  loading_p0: typing.Optional[typing.Any] = None
  loading_p1: typing.Optional[typing.Any] = None
  loading_p2: typing.Optional[typing.Any] = None
  mean_gc: typing.Optional[typing.Any] = None
  mean_length: typing.Optional[typing.Any] = None
  median_length: typing.Optional[typing.Any] = None
  n50_length: typing.Optional[typing.Any] = None
  path: typing.Optional[str] = None
  reads: typing.Optional[typing.Any] = None
  result_check_id: typing.Optional[typing.Union[int, float]] = None
  run_id: typing.Optional[typing.Union[int, float]] = None
  run_unique_id: typing.Optional[str] = None
  smrtcell_unique_id: typing.Optional[str] = None
  unit_id: typing.Optional[typing.Union[int, float]] = None

  
  pacbio_run: typing.Optional[PacbioRun] = None
  result_check: typing.Optional[ResultCheck] = None
  run: typing.Optional[Run] = None
  run_unit: typing.Optional[RunUnit] = None
  smrtcell: typing.Optional[SmrtCell] = None


# ---

def plainToSuperMulti(json: dict) -> SuperMulti:
  obj = SuperMulti()
  obj.description = json.get('description')
  obj.id = json.get('id')
  obj.unique_dual_required = bool(json.get('unique_dual_required'))
  obj.request_lanes = [ plainToRequestLane(o) for o in json['request_lanes'] ] if json.get('request_lanes') else []

  return obj

def serializeSuperMulti(obj: SuperMulti) -> dict:
  json = {}
  json['description'] = obj.description
  json['id'] = obj.id
  json['unique_dual_required'] = obj.unique_dual_required
  if obj.request_lanes is not None:
    json['request_lanes'] = [ serializeRequestLane(o) for o in obj.request_lanes ]

  return json


@dataclass
class SuperMulti:
  description: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  unique_dual_required: typing.Optional[bool] = None

  
  request_lanes: list[RequestLane] = field(default_factory=list)


# ---

def plainToTag(json: dict) -> Tag:
  obj = Tag()
  obj.adaptor_type = json.get('adaptor_type')
  obj.available = bool(json.get('available'))
  obj.name = json.get('name')
  obj.num = json.get('num')
  obj.pos = json.get('pos')
  obj.seq = json.get('seq')
  obj.unique_combination = json.get('unique_combination')
  obj.adaptor_type_ref = plainToAdaptorType(json['adaptor_type_ref']) if json.get('adaptor_type_ref') else None
  obj.samples_adaptor_type_adaptor_numbers = [ plainToSample(o) for o in json['samples_adaptor_type_adaptor_numbers'] ] if json.get('samples_adaptor_type_adaptor_numbers') else []
  obj.samples_adaptor_type_adaptor_secondary_numbers = [ plainToSample(o) for o in json['samples_adaptor_type_adaptor_secondary_numbers'] ] if json.get('samples_adaptor_type_adaptor_secondary_numbers') else []

  return obj

def serializeTag(obj: Tag) -> dict:
  json = {}
  json['adaptor_type'] = obj.adaptor_type
  json['available'] = obj.available
  json['name'] = obj.name
  json['num'] = obj.num
  json['pos'] = obj.pos
  json['seq'] = obj.seq
  json['unique_combination'] = obj.unique_combination
  json['adaptor_type_ref'] = serializeAdaptorType(obj.adaptor_type_ref) if obj.adaptor_type_ref is not None else None
  if obj.samples_adaptor_type_adaptor_numbers is not None:
    json['samples_adaptor_type_adaptor_numbers'] = [ serializeSample(o) for o in obj.samples_adaptor_type_adaptor_numbers ]
  if obj.samples_adaptor_type_adaptor_secondary_numbers is not None:
    json['samples_adaptor_type_adaptor_secondary_numbers'] = [ serializeSample(o) for o in obj.samples_adaptor_type_adaptor_secondary_numbers ]

  return json


@dataclass
class Tag:
  adaptor_type: typing.Optional[str] = None
  available: typing.Optional[bool] = None
  name: typing.Optional[str] = None
  num: typing.Optional[typing.Union[int, float]] = None
  pos: typing.Optional[str] = None
  seq: typing.Optional[str] = None
  unique_combination: typing.Optional[typing.Union[int, float]] = None

  
  adaptor_type_ref: typing.Optional[AdaptorType] = None
  samples_adaptor_type_adaptor_numbers: list[Sample] = field(default_factory=list)
  samples_adaptor_type_adaptor_secondary_numbers: list[Sample] = field(default_factory=list)


# ---

def plainToLabStep(json: dict) -> LabStep:
  obj = LabStep()
  obj.fails = [ plainToLabStep(o) for o in json['fails'] ] if json.get('fails') else []
  obj.flag = json.get('flag')
  obj.form = json.get('form')
  obj.have = json.get('have')
  obj.obj_id = json.get('obj_id')
  obj.obj_type = json.get('obj_type')
  obj.ordering = json.get('ordering')
  obj.should = json.get('should')
  obj.warnings = [ plainToLabStep(o) for o in json['warnings'] ] if json.get('warnings') else []

  return obj

def serializeLabStep(obj: LabStep) -> dict:
  json = {}
  if obj.fails is not None:
    json['fails'] = [ serializeLabStep(o) for o in obj.fails ]
  json['flag'] = obj.flag
  json['form'] = obj.form
  json['have'] = obj.have
  json['obj_id'] = obj.obj_id
  json['obj_type'] = obj.obj_type
  json['ordering'] = obj.ordering
  json['should'] = obj.should
  if obj.warnings is not None:
    json['warnings'] = [ serializeLabStep(o) for o in obj.warnings ]

  return json


@dataclass
class LabStep:
  fails: list[LabStep]=field(default_factory=list)
  flag: typing.Optional[str] = None
  form: typing.Optional[str] = None
  have: typing.Optional[typing.Union[int, float]] = None
  obj_id: typing.Optional[typing.Union[int, float]] = None
  obj_type: typing.Optional[str] = None
  ordering: typing.Optional[typing.Union[int, float]] = None
  should: typing.Optional[typing.Union[int, float]] = None
  warnings: list[LabStep]=field(default_factory=list)

  
  

# ---

def plainToSampleFields(json: dict) -> SampleFields:
  obj = SampleFields()
  obj.adaptor_type = json.get('adaptor_type')
  obj.antibody = json.get('antibody')
  obj.celltype = json.get('celltype')
  obj.cutout_size = json.get('cutout_size')
  obj.exptype = json.get('exptype')
  obj.fragment_size = json.get('fragment_size')
  obj.genotype = json.get('genotype')
  obj.organism = json.get('organism')
  obj.own_risk = json.get('own_risk')
  obj.preparation_kit = json.get('preparation_kit')
  obj.preparation_type = json.get('preparation_type')
  obj.primer = json.get('primer')
  obj.ready = json.get('ready')
  obj.received = json.get('received')
  obj.status = json.get('status')
  obj.stranded = json.get('stranded')
  obj.tissue_type = json.get('tissue_type')
  obj.treatment = json.get('treatment')

  return obj

def serializeSampleFields(obj: SampleFields) -> dict:
  json = {}
  json['adaptor_type'] = obj.adaptor_type
  json['antibody'] = obj.antibody
  json['celltype'] = obj.celltype
  json['cutout_size'] = obj.cutout_size
  json['exptype'] = obj.exptype
  json['fragment_size'] = obj.fragment_size
  json['genotype'] = obj.genotype
  json['organism'] = obj.organism
  json['own_risk'] = obj.own_risk
  json['preparation_kit'] = obj.preparation_kit
  json['preparation_type'] = obj.preparation_type
  json['primer'] = obj.primer
  json['ready'] = obj.ready
  json['received'] = obj.received
  json['status'] = obj.status
  json['stranded'] = obj.stranded
  json['tissue_type'] = obj.tissue_type
  json['treatment'] = obj.treatment

  return json


@dataclass
class SampleFields:
  adaptor_type: typing.Optional[dict] = None
  antibody: typing.Optional[dict] = None
  celltype: typing.Optional[dict] = None
  cutout_size: typing.Optional[dict] = None
  exptype: typing.Optional[dict] = None
  fragment_size: typing.Optional[dict] = None
  genotype: typing.Optional[dict] = None
  organism: typing.Optional[dict] = None
  own_risk: typing.Optional[dict] = None
  preparation_kit: typing.Optional[dict] = None
  preparation_type: typing.Optional[dict] = None
  primer: typing.Optional[dict] = None
  ready: typing.Optional[dict] = None
  received: typing.Optional[dict] = None
  status: typing.Optional[dict] = None
  stranded: typing.Optional[dict] = None
  tissue_type: typing.Optional[dict] = None
  treatment: typing.Optional[dict] = None

  
  

# ---

def plainToCelltype(json: dict) -> Celltype:
  obj = Celltype()
  obj.available = bool(json.get('available'))
  obj.custom_readlengths = bool(json.get('custom_readlengths'))
  obj.description = json.get('description')
  obj.flowcell_count = json.get('flowcell_count')
  obj.lane_count = json.get('lane_count')
  obj.name = json.get('name')
  obj.read_minimum = json.get('read_minimum')
  obj.read_typical = json.get('read_typical')
  obj.selfservice = bool(json.get('selfservice'))

  return obj

def serializeCelltype(obj: Celltype) -> dict:
  json = {}
  json['available'] = obj.available
  json['custom_readlengths'] = obj.custom_readlengths
  json['description'] = obj.description
  json['flowcell_count'] = obj.flowcell_count
  json['lane_count'] = obj.lane_count
  json['name'] = obj.name
  json['read_minimum'] = obj.read_minimum
  json['read_typical'] = obj.read_typical
  json['selfservice'] = obj.selfservice

  return json


@dataclass
class Celltype:
  available: typing.Optional[bool] = None
  custom_readlengths: typing.Optional[bool] = None
  description: typing.Optional[str] = None
  flowcell_count: typing.Optional[typing.Union[int, float]] = None
  lane_count: typing.Optional[typing.Union[int, float]] = None
  name: typing.Optional[str] = None
  read_minimum: typing.Optional[typing.Union[int, float]] = None
  read_typical: typing.Optional[str] = None
  selfservice: typing.Optional[bool] = None

  
  

# ---

def plainToEstimateRequest(json: dict) -> EstimateRequest:
  obj = EstimateRequest()
  obj.accepted = datetime.fromisoformat(json.get('accepted', '')) if json.get('accepted') else None
  obj.completed = datetime.fromisoformat(json.get('completed', '')) if json.get('completed') else None
  obj.cost_assignment = json.get('cost_assignment')
  obj.group = json.get('group')
  obj.id = json.get('id')
  obj.long_seqtype = json.get('long_seqtype')
  obj.pricing_category = json.get('pricing_category')
  obj.project_name = json.get('project_name')
  obj.scientist = json.get('scientist')
  obj.status = json.get('status')
  obj.submitted = datetime.fromisoformat(json.get('submitted', '')) if json.get('submitted') else None

  return obj

def serializeEstimateRequest(obj: EstimateRequest) -> dict:
  json = {}
  json['accepted'] = obj.accepted.isoformat() if obj.accepted else None
  json['completed'] = obj.completed.isoformat() if obj.completed else None
  json['cost_assignment'] = obj.cost_assignment
  json['group'] = obj.group
  json['id'] = obj.id
  json['long_seqtype'] = obj.long_seqtype
  json['pricing_category'] = obj.pricing_category
  json['project_name'] = obj.project_name
  json['scientist'] = obj.scientist
  json['status'] = obj.status
  json['submitted'] = obj.submitted.isoformat() if obj.submitted else None

  return json


@dataclass
class EstimateRequest:
  accepted: typing.Optional[datetime] = None
  completed: typing.Optional[datetime] = None
  cost_assignment: typing.Optional[str] = None
  group: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  long_seqtype: typing.Optional[str] = None
  pricing_category: typing.Optional[str] = None
  project_name: typing.Optional[str] = None
  scientist: typing.Optional[str] = None
  status: typing.Optional[str] = None
  submitted: typing.Optional[datetime] = None

  
  

# ---

def plainToVirtualBill(json: dict) -> VirtualBill:
  obj = VirtualBill()
  obj.category_totals = json.get('category_totals')
  obj.invoices = [ plainToInvoice(o) for o in json['invoices'] ] if json.get('invoices') else []
  obj.total = json.get('total')

  return obj

def serializeVirtualBill(obj: VirtualBill) -> dict:
  json = {}
  json['category_totals'] = obj.category_totals
  if obj.invoices is not None:
    json['invoices'] = [ serializeInvoice(o) for o in obj.invoices ]
  json['total'] = obj.total

  return json


@dataclass
class VirtualBill:
  category_totals: typing.Optional[dict] = None
  invoices: list[Invoice]=field(default_factory=list)
  total: typing.Optional[typing.Union[int, float]] = None

  
  

# ---

def plainToFormConfig(json: dict) -> FormConfig:
  obj = FormConfig()
  obj.control_samples = bool(json.get('control_samples'))
  obj.expand_multis = bool(json.get('expand_multis'))
  obj.filters = json.get('filters')

  return obj

def serializeFormConfig(obj: FormConfig) -> dict:
  json = {}
  json['control_samples'] = obj.control_samples
  json['expand_multis'] = obj.expand_multis
  json['filters'] = obj.filters

  return json


@dataclass
class FormConfig:
  control_samples: typing.Optional[bool] = None
  expand_multis: typing.Optional[bool] = None
  filters: typing.Optional[typing.Any] = None

  
  

# ---

def plainToTimelineEvent(json: dict) -> TimelineEvent:
  obj = TimelineEvent()
  obj.date = datetime.fromisoformat(json.get('date', '')) if json.get('date') else None
  obj.description = json.get('description')
  obj.event_type = json.get('event_type')
  obj.ids = json.get('ids')
  obj.newstatus = json.get('newstatus')
  obj.obj_type = json.get('obj_type')
  obj.oldstatus = json.get('oldstatus')

  return obj

def serializeTimelineEvent(obj: TimelineEvent) -> dict:
  json = {}
  json['date'] = obj.date.isoformat() if obj.date else None
  json['description'] = obj.description
  json['event_type'] = obj.event_type
  json['ids'] = obj.ids
  json['newstatus'] = obj.newstatus
  json['obj_type'] = obj.obj_type
  json['oldstatus'] = obj.oldstatus

  return json


@dataclass
class TimelineEvent:
  date: typing.Optional[datetime] = None
  description: typing.Optional[str] = None
  event_type: typing.Optional[str] = None
  ids: typing.Optional[str] = None
  newstatus: typing.Optional[str] = None
  obj_type: typing.Optional[str] = None
  oldstatus: typing.Optional[str] = None

  
  

# ---

def plainToSequencedBarcode(json: dict) -> SequencedBarcode:
  obj = SequencedBarcode()
  obj.adaptor_number = json.get('adaptor_number')
  obj.adaptor_secondary_number = json.get('adaptor_secondary_number')
  obj.adaptor_secondary_tag = json.get('adaptor_secondary_tag')
  obj.adaptor_secondary_tagname = json.get('adaptor_secondary_tagname')
  obj.adaptor_tag = json.get('adaptor_tag')
  obj.adaptor_tagname = json.get('adaptor_tagname')
  obj.adaptor_type = json.get('adaptor_type')
  obj.is_pool = bool(json.get('is_pool'))
  obj.is_spikein = bool(json.get('is_spikein'))
  obj.multi_id = json.get('multi_id')
  obj.pool_ratio = json.get('pool_ratio')
  obj.pooled_by_user = bool(json.get('pooled_by_user'))
  obj.request_id = json.get('request_id')
  obj.requested_ratio = json.get('requested_ratio')
  obj.required_ratio = json.get('required_ratio')
  obj.required_reads = json.get('required_reads')
  obj.sample_id = json.get('sample_id')
  obj.share_required_ratio = json.get('share_required_ratio')
  obj.share_status = json.get('share_status')
  obj.unit_id = json.get('unit_id')
  obj.vendor_id = json.get('vendor_id')

  return obj

def serializeSequencedBarcode(obj: SequencedBarcode) -> dict:
  json = {}
  json['adaptor_number'] = obj.adaptor_number
  json['adaptor_secondary_number'] = obj.adaptor_secondary_number
  json['adaptor_secondary_tag'] = obj.adaptor_secondary_tag
  json['adaptor_secondary_tagname'] = obj.adaptor_secondary_tagname
  json['adaptor_tag'] = obj.adaptor_tag
  json['adaptor_tagname'] = obj.adaptor_tagname
  json['adaptor_type'] = obj.adaptor_type
  json['is_pool'] = obj.is_pool
  json['is_spikein'] = obj.is_spikein
  json['multi_id'] = obj.multi_id
  json['pool_ratio'] = obj.pool_ratio
  json['pooled_by_user'] = obj.pooled_by_user
  json['request_id'] = obj.request_id
  json['requested_ratio'] = obj.requested_ratio
  json['required_ratio'] = obj.required_ratio
  json['required_reads'] = obj.required_reads
  json['sample_id'] = obj.sample_id
  json['share_required_ratio'] = obj.share_required_ratio
  json['share_status'] = obj.share_status
  json['unit_id'] = obj.unit_id
  json['vendor_id'] = obj.vendor_id

  return json


@dataclass
class SequencedBarcode:
  adaptor_number: typing.Optional[typing.Union[int, float]] = None
  adaptor_secondary_number: typing.Optional[typing.Union[int, float]] = None
  adaptor_secondary_tag: typing.Optional[str] = None
  adaptor_secondary_tagname: typing.Optional[str] = None
  adaptor_tag: typing.Optional[str] = None
  adaptor_tagname: typing.Optional[str] = None
  adaptor_type: typing.Optional[str] = None
  is_pool: typing.Optional[bool] = None
  is_spikein: typing.Optional[bool] = None
  multi_id: typing.Optional[typing.Union[int, float]] = None
  pool_ratio: typing.Optional[typing.Union[int, float]] = None
  pooled_by_user: typing.Optional[bool] = None
  request_id: typing.Optional[typing.Union[int, float]] = None
  requested_ratio: typing.Optional[typing.Union[int, float]] = None
  required_ratio: typing.Optional[typing.Union[int, float]] = None
  required_reads: typing.Optional[typing.Union[int, float]] = None
  sample_id: typing.Optional[typing.Union[int, float]] = None
  share_required_ratio: typing.Optional[typing.Union[int, float]] = None
  share_status: typing.Optional[str] = None
  unit_id: typing.Optional[typing.Union[int, float]] = None
  vendor_id: typing.Optional[str] = None

  
  

# ---

def plainToZammadTicket(json: dict) -> ZammadTicket:
  obj = ZammadTicket()
  obj.created_at = datetime.fromisoformat(json.get('created_at', '')) if json.get('created_at') else None
  obj.customer = json.get('customer')
  obj.group = json.get('group')
  obj.id = json.get('id')
  obj.multi = json.get('multi')
  obj.note = json.get('note')
  obj.number = json.get('number')
  obj.organization = json.get('organization')
  obj.owner = json.get('owner')
  obj.request = json.get('request')
  obj.sample = json.get('sample')
  obj.state = json.get('state')
  obj.title = json.get('title')
  obj.updated_at = datetime.fromisoformat(json.get('updated_at', '')) if json.get('updated_at') else None
  obj.url = json.get('url')

  return obj

def serializeZammadTicket(obj: ZammadTicket) -> dict:
  json = {}
  json['created_at'] = obj.created_at.isoformat() if obj.created_at else None
  json['customer'] = obj.customer
  json['group'] = obj.group
  json['id'] = obj.id
  json['multi'] = obj.multi
  json['note'] = obj.note
  json['number'] = obj.number
  json['organization'] = obj.organization
  json['owner'] = obj.owner
  json['request'] = obj.request
  json['sample'] = obj.sample
  json['state'] = obj.state
  json['title'] = obj.title
  json['updated_at'] = obj.updated_at.isoformat() if obj.updated_at else None
  json['url'] = obj.url

  return json


@dataclass
class ZammadTicket:
  created_at: typing.Optional[datetime] = None
  customer: typing.Optional[str] = None
  group: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  multi: typing.Optional[str] = None
  note: typing.Optional[str] = None
  number: typing.Optional[typing.Union[int, float]] = None
  organization: typing.Optional[str] = None
  owner: typing.Optional[str] = None
  request: typing.Optional[str] = None
  sample: typing.Optional[str] = None
  state: typing.Optional[str] = None
  title: typing.Optional[str] = None
  updated_at: typing.Optional[datetime] = None
  url: typing.Optional[str] = None

  
  

# ---

def plainToDataEntryField(json: dict) -> DataEntryField:
  obj = DataEntryField()
  obj.id = json.get('id')
  obj.name = json.get('name')
  obj.type = json.get('type')

  return obj

def serializeDataEntryField(obj: DataEntryField) -> dict:
  json = {}
  json['id'] = obj.id
  json['name'] = obj.name
  json['type'] = obj.type

  return json


@dataclass
class DataEntryField:
  id: typing.Optional[typing.Union[int, float]] = None
  name: typing.Optional[str] = None
  type: typing.Optional[typing.Any] = None

  
  

# ---

def plainToDataEntryFlag(json: dict) -> DataEntryFlag:
  obj = DataEntryFlag()
  obj.id = json.get('id')
  obj.name = json.get('name')
  obj.severity = json.get('severity')

  return obj

def serializeDataEntryFlag(obj: DataEntryFlag) -> dict:
  json = {}
  json['id'] = obj.id
  json['name'] = obj.name
  json['severity'] = obj.severity

  return json


@dataclass
class DataEntryFlag:
  id: typing.Optional[typing.Union[int, float]] = None
  name: typing.Optional[str] = None
  severity: typing.Optional[typing.Union[int, float]] = None

  
  

# ---

def plainToExptype(json: dict) -> Exptype:
  obj = Exptype()
  obj.description = json.get('description')
  obj.exptype = json.get('exptype')

  return obj

def serializeExptype(obj: Exptype) -> dict:
  json = {}
  json['description'] = obj.description
  json['exptype'] = obj.exptype

  return json


@dataclass
class Exptype:
  description: typing.Optional[str] = None
  exptype: typing.Optional[str] = None

  
  

# ---

def plainToMessageType(json: dict) -> MessageType:
  obj = MessageType()
  obj.admin_cc = bool(json.get('admin_cc'))
  obj.admin_message = bool(json.get('admin_message'))
  obj.attach_report = bool(json.get('attach_report'))
  obj.attach_reqsheet = bool(json.get('attach_reqsheet'))
  obj.configurable = bool(json.get('configurable'))
  obj.deferred = bool(json.get('deferred'))
  obj.groupable = bool(json.get('groupable'))
  obj.id = json.get('id')
  obj.name = json.get('name')
  obj.sensitive = bool(json.get('sensitive'))
  obj.template = json.get('template')

  return obj

def serializeMessageType(obj: MessageType) -> dict:
  json = {}
  json['admin_cc'] = obj.admin_cc
  json['admin_message'] = obj.admin_message
  json['attach_report'] = obj.attach_report
  json['attach_reqsheet'] = obj.attach_reqsheet
  json['configurable'] = obj.configurable
  json['deferred'] = obj.deferred
  json['groupable'] = obj.groupable
  json['id'] = obj.id
  json['name'] = obj.name
  json['sensitive'] = obj.sensitive
  json['template'] = obj.template

  return json


@dataclass
class MessageType:
  admin_cc: typing.Optional[bool] = None
  admin_message: typing.Optional[bool] = None
  attach_report: typing.Optional[bool] = None
  attach_reqsheet: typing.Optional[bool] = None
  configurable: typing.Optional[bool] = None
  deferred: typing.Optional[bool] = None
  groupable: typing.Optional[bool] = None
  id: typing.Optional[typing.Union[int, float]] = None
  name: typing.Optional[str] = None
  sensitive: typing.Optional[bool] = None
  template: typing.Optional[str] = None

  
  

# ---

def plainToNoteFlag(json: dict) -> NoteFlag:
  obj = NoteFlag()
  obj.id = json.get('id')
  obj.name = json.get('name')
  obj.severity = json.get('severity')

  return obj

def serializeNoteFlag(obj: NoteFlag) -> dict:
  json = {}
  json['id'] = obj.id
  json['name'] = obj.name
  json['severity'] = obj.severity

  return json


@dataclass
class NoteFlag:
  id: typing.Optional[typing.Union[int, float]] = None
  name: typing.Optional[str] = None
  severity: typing.Optional[typing.Union[int, float]] = None

  
  

# ---

def plainToObjType(json: dict) -> ObjType:
  obj = ObjType()
  obj.db_table = json.get('db_table')
  obj.id = json.get('id')
  obj.name = json.get('name')

  return obj

def serializeObjType(obj: ObjType) -> dict:
  json = {}
  json['db_table'] = obj.db_table
  json['id'] = obj.id
  json['name'] = obj.name

  return json


@dataclass
class ObjType:
  db_table: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  name: typing.Optional[str] = None

  
  

# ---

def plainToOrganism(json: dict) -> Organism:
  obj = Organism()
  obj.bloom_filter_name = json.get('bloom_filter_name')
  obj.common_name = json.get('common_name')
  obj.sci_name = json.get('sci_name')
  obj.taxonomy_id = json.get('taxonomy_id')

  return obj

def serializeOrganism(obj: Organism) -> dict:
  json = {}
  json['bloom_filter_name'] = obj.bloom_filter_name
  json['common_name'] = obj.common_name
  json['sci_name'] = obj.sci_name
  json['taxonomy_id'] = obj.taxonomy_id

  return json


@dataclass
class Organism:
  bloom_filter_name: typing.Optional[str] = None
  common_name: typing.Optional[str] = None
  sci_name: typing.Optional[str] = None
  taxonomy_id: typing.Optional[typing.Union[int, float]] = None

  
  

# ---

def plainToReadmode(json: dict) -> Readmode:
  obj = Readmode()
  obj.asym = bool(json.get('asym'))
  obj.available = bool(json.get('available'))
  obj.celltype = json.get('celltype')
  obj.celltype_description = json.get('celltype_description')
  obj.custom_readlengths = bool(json.get('custom_readlengths'))
  obj.duration = json.get('duration')
  obj.flowcell_type = json.get('flowcell_type')
  obj.id = json.get('id')
  obj.lane_count = json.get('lane_count')
  obj.long_seqtype = json.get('long_seqtype')
  obj.movielength = json.get('movielength')
  obj.ontcell_type = json.get('ontcell_type')
  obj.paired = bool(json.get('paired'))
  obj.platform = json.get('platform')
  obj.prep_duration = json.get('prep_duration')
  obj.pricing_item_name = json.get('pricing_item_name')
  obj.rapid_mode = bool(json.get('rapid_mode'))
  obj.read_minimum = json.get('read_minimum')
  obj.read_typical = json.get('read_typical')
  obj.readlen = json.get('readlen')
  obj.selfservice = bool(json.get('selfservice'))
  obj.sharable = bool(json.get('sharable'))
  obj.short_seqtype = json.get('short_seqtype')
  obj.smrtcell_type = json.get('smrtcell_type')

  return obj

def serializeReadmode(obj: Readmode) -> dict:
  json = {}
  json['asym'] = obj.asym
  json['available'] = obj.available
  json['celltype'] = obj.celltype
  json['celltype_description'] = obj.celltype_description
  json['custom_readlengths'] = obj.custom_readlengths
  json['duration'] = obj.duration
  json['flowcell_type'] = obj.flowcell_type
  json['id'] = obj.id
  json['lane_count'] = obj.lane_count
  json['long_seqtype'] = obj.long_seqtype
  json['movielength'] = obj.movielength
  json['ontcell_type'] = obj.ontcell_type
  json['paired'] = obj.paired
  json['platform'] = obj.platform
  json['prep_duration'] = obj.prep_duration
  json['pricing_item_name'] = obj.pricing_item_name
  json['rapid_mode'] = obj.rapid_mode
  json['read_minimum'] = obj.read_minimum
  json['read_typical'] = obj.read_typical
  json['readlen'] = obj.readlen
  json['selfservice'] = obj.selfservice
  json['sharable'] = obj.sharable
  json['short_seqtype'] = obj.short_seqtype
  json['smrtcell_type'] = obj.smrtcell_type

  return json


@dataclass
class Readmode:
  asym: typing.Optional[bool] = None
  available: typing.Optional[bool] = None
  celltype: typing.Optional[str] = None
  celltype_description: typing.Optional[str] = None
  custom_readlengths: typing.Optional[bool] = None
  duration: typing.Optional[typing.Union[int, float]] = None
  flowcell_type: typing.Optional[str] = None
  id: typing.Optional[typing.Union[int, float]] = None
  lane_count: typing.Optional[typing.Union[int, float]] = None
  long_seqtype: typing.Optional[str] = None
  movielength: typing.Optional[typing.Union[int, float]] = None
  ontcell_type: typing.Optional[str] = None
  paired: typing.Optional[bool] = None
  platform: typing.Optional[str] = None
  prep_duration: typing.Optional[typing.Union[int, float]] = None
  pricing_item_name: typing.Optional[str] = None
  rapid_mode: typing.Optional[bool] = None
  read_minimum: typing.Optional[typing.Union[int, float]] = None
  read_typical: typing.Optional[str] = None
  readlen: typing.Optional[typing.Union[int, float]] = None
  selfservice: typing.Optional[bool] = None
  sharable: typing.Optional[bool] = None
  short_seqtype: typing.Optional[str] = None
  smrtcell_type: typing.Optional[str] = None

  
  

# ---

def plainToStatus(json: dict) -> Status:
  obj = Status()
  obj.description = json.get('description')
  obj.obj_type = json.get('obj_type')
  obj.ord = json.get('ord')
  obj.status = json.get('status')

  return obj

def serializeStatus(obj: Status) -> dict:
  json = {}
  json['description'] = obj.description
  json['obj_type'] = obj.obj_type
  json['ord'] = obj.ord
  json['status'] = obj.status

  return json


@dataclass
class Status:
  description: typing.Optional[str] = None
  obj_type: typing.Optional[str] = None
  ord: typing.Optional[typing.Union[int, float]] = None
  status: typing.Optional[str] = None

  
  

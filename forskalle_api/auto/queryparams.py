from forskalle_api.fsk_query import *

class ChangesetFilters:
  def __init__(self, file_id=None, form=None, username=None):
    self.file_id = file_id
    self.form = form
    self.username = username

class ChangesetSorts:
  def __init__(self, date=None):
    self.date = date


class DataEntryFilters:
  def __init__(self, deleted=None, form=None, obj_id=None, obj_type=None, username=None):
    self.deleted = deleted
    self.form = form
    self.obj_id = obj_id
    self.obj_type = obj_type
    self.username = username

class DataEntrySorts:
  def __init__(self, date=None):
    self.date = date


class GroupFilters:
  def __init__(self, billing_type=None, email=None, institute=None, name=None):
    self.billing_type = billing_type
    self.email = email
    self.institute = institute
    self.name = name

class GroupSorts:
  pass


class IlluminaRunFilters:
  def __init__(self, comments=None, flowcell=None, machine=None, preparation_date=None, readmode_id=None, sequenced_after=None, sequenced_before=None, status=None, username=None, vendor_id=None):
    self.comments = comments
    self.flowcell = flowcell
    self.machine = machine
    self.preparation_date = preparation_date
    self.readmode_id = readmode_id
    self.sequenced_after = sequenced_after
    self.sequenced_before = sequenced_before
    self.status = status
    self.username = username
    self.vendor_id = vendor_id

class IlluminaRunSorts:
  def __init__(self, flowcell=None, id=None, machine=None, preparation_date=None, readmode_long_seqtype=None, sequencing_date=None, status=None, vendor_id=None):
    self.flowcell = flowcell
    self.id = id
    self.machine = machine
    self.preparation_date = preparation_date
    self.readmode_long_seqtype = readmode_long_seqtype
    self.sequencing_date = sequencing_date
    self.status = status
    self.vendor_id = vendor_id


class MultiplexFilters:
  def __init__(self, available_samples=None, description=None, group=None, platform=None, received_after=None, received_before=None, sample_antibody=None, sample_celltype=None, sample_description=None, sample_exptype=None, sample_genotype=None, sample_organism=None, sample_tissue_type=None, sample_treatment=None, scientist=None):
    self.available_samples = available_samples
    self.description = description
    self.group = group
    self.platform = platform
    self.received_after = received_after
    self.received_before = received_before
    self.sample_antibody = sample_antibody
    self.sample_celltype = sample_celltype
    self.sample_description = sample_description
    self.sample_exptype = sample_exptype
    self.sample_genotype = sample_genotype
    self.sample_organism = sample_organism
    self.sample_tissue_type = sample_tissue_type
    self.sample_treatment = sample_treatment
    self.scientist = scientist

class MultiplexSorts:
  def __init__(self, group=None, id=None, received=None, scientist=None):
    self.group = group
    self.id = id
    self.received = received
    self.scientist = scientist


class OntRunFilters:
  def __init__(self, comments=None, machine=None, name=None, preparation_date=None, readmode_id=None, run_id=None, sequenced_after=None, sequenced_before=None, status=None, username=None, vendor_id=None):
    self.comments = comments
    self.machine = machine
    self.name = name
    self.preparation_date = preparation_date
    self.readmode_id = readmode_id
    self.run_id = run_id
    self.sequenced_after = sequenced_after
    self.sequenced_before = sequenced_before
    self.status = status
    self.username = username
    self.vendor_id = vendor_id

class OntRunSorts:
  def __init__(self, id=None, machine=None, preparation_date=None, readmode_long_seqtype=None, sequencing_date=None, status=None, vendor_id=None):
    self.id = id
    self.machine = machine
    self.preparation_date = preparation_date
    self.readmode_long_seqtype = readmode_long_seqtype
    self.sequencing_date = sequencing_date
    self.status = status
    self.vendor_id = vendor_id


class PacbioRunFilters:
  def __init__(self, comments=None, machine=None, name=None, preparation_date=None, readmode_id=None, run_id=None, sequenced_after=None, sequenced_before=None, status=None, username=None, vendor_id=None):
    self.comments = comments
    self.machine = machine
    self.name = name
    self.preparation_date = preparation_date
    self.readmode_id = readmode_id
    self.run_id = run_id
    self.sequenced_after = sequenced_after
    self.sequenced_before = sequenced_before
    self.status = status
    self.username = username
    self.vendor_id = vendor_id

class PacbioRunSorts:
  def __init__(self, id=None, machine=None, preparation_date=None, readmode_long_seqtype=None, sequencing_date=None, status=None, vendor_id=None):
    self.id = id
    self.machine = machine
    self.preparation_date = preparation_date
    self.readmode_long_seqtype = readmode_long_seqtype
    self.sequencing_date = sequencing_date
    self.status = status
    self.vendor_id = vendor_id


class ProjectFilters:
  def __init__(self, completed_after=None, completed_before=None, control=None, cost_assignment=None, created_after=None, created_before=None, group=None, last_request_after=None, last_request_before=None, name=None, scientist=None, status=None):
    self.completed_after = completed_after
    self.completed_before = completed_before
    self.control = control
    self.cost_assignment = cost_assignment
    self.created_after = created_after
    self.created_before = created_before
    self.group = group
    self.last_request_after = last_request_after
    self.last_request_before = last_request_before
    self.name = name
    self.scientist = scientist
    self.status = status

class ProjectSorts:
  def __init__(self, cost_assignment=None, created=None, group=None, last_request=None, name=None, request_count=None, scientist=None):
    self.cost_assignment = cost_assignment
    self.created = created
    self.group = group
    self.last_request = last_request
    self.name = name
    self.request_count = request_count
    self.scientist = scientist


class RequestFilters:
  def __init__(self, accepted_after=None, accepted_before=None, align=None, completed_after=None, completed_before=None, cost_assignment=None, group=None, long_seqtype=None, project_name=None, quarter=None, request_lane_status=None, sample_celltype=None, sample_comments=None, sample_description=None, sample_exptype=None, sample_genotype=None, sample_organism=None, sample_preparation_kit=None, sample_preparation_type=None, sample_primer=None, sample_tissue_type=None, scientist=None, short_seqtype=None, status=None, submitted_after=None, submitted_before=None):
    self.accepted_after = accepted_after
    self.accepted_before = accepted_before
    self.align = align
    self.completed_after = completed_after
    self.completed_before = completed_before
    self.cost_assignment = cost_assignment
    self.group = group
    self.long_seqtype = long_seqtype
    self.project_name = project_name
    self.quarter = quarter
    self.request_lane_status = request_lane_status
    self.sample_celltype = sample_celltype
    self.sample_comments = sample_comments
    self.sample_description = sample_description
    self.sample_exptype = sample_exptype
    self.sample_genotype = sample_genotype
    self.sample_organism = sample_organism
    self.sample_preparation_kit = sample_preparation_kit
    self.sample_preparation_type = sample_preparation_type
    self.sample_primer = sample_primer
    self.sample_tissue_type = sample_tissue_type
    self.scientist = scientist
    self.short_seqtype = short_seqtype
    self.status = status
    self.submitted_after = submitted_after
    self.submitted_before = submitted_before

class RequestSorts:
  def __init__(self, group=None, long_seqtype=None, project=None, scientist=None, short_seqtype=None):
    self.group = group
    self.long_seqtype = long_seqtype
    self.project = project
    self.scientist = scientist
    self.short_seqtype = short_seqtype


class RequestDraftFilters:
  def __init__(self, group_id=None, name=None, scientist_id=None, valid=None):
    self.group_id = group_id
    self.name = name
    self.scientist_id = scientist_id
    self.valid = valid

class RequestDraftSorts:
  def __init__(self, create_date=None, group=None, id=None, name=None, scientist=None):
    self.create_date = create_date
    self.group = group
    self.id = id
    self.name = name
    self.scientist = scientist


class RequestLaneFilters:
  def __init__(self, accepted_after=None, accepted_before=None, category=None, long_seqtype=None, request_lane=None, share_status=None, short_seqtype=None, size_analysis_done=None, status=None):
    self.accepted_after = accepted_after
    self.accepted_before = accepted_before
    self.category = category
    self.long_seqtype = long_seqtype
    self.request_lane = request_lane
    self.share_status = share_status
    self.short_seqtype = short_seqtype
    self.size_analysis_done = size_analysis_done
    self.status = status

class RequestLaneSorts:
  def __init__(self, objId=None, obj_id=None, short_seqtype=None, showId=None, show_id=None):
    self.objId = objId
    self.obj_id = obj_id
    self.short_seqtype = short_seqtype
    self.showId = showId
    self.show_id = show_id


class RunFilters:
  def __init__(self, comment=None, long_seqtype=None, machine=None, platform=None, preparation_date=None, readmode_id=None, sequencing_date=None, status=None, username=None, vendor_id=None):
    self.comment = comment
    self.long_seqtype = long_seqtype
    self.machine = machine
    self.platform = platform
    self.preparation_date = preparation_date
    self.readmode_id = readmode_id
    self.sequencing_date = sequencing_date
    self.status = status
    self.username = username
    self.vendor_id = vendor_id

class RunSorts:
  def __init__(self, id=None, machine=None, platform=None, preparation_date=None, sequencing_date=None, status=None, vendor_id=None):
    self.id = id
    self.machine = machine
    self.platform = platform
    self.preparation_date = preparation_date
    self.sequencing_date = sequencing_date
    self.status = status
    self.vendor_id = vendor_id


class SampleFilters:
  def __init__(self, antibody=None, available=None, celltype=None, changed_since=None, comments=None, description=None, exptype=None, genotype=None, group=None, id_from=None, id_to=None, multi_id=None, organism=None, platform=None, preparation_kit=None, preparation_type=None, ready_after=None, ready_before=None, received_after=None, received_before=None, request_id=None, request_status=None, scientist=None, status=None, tissue_type=None, treatment=None):
    self.antibody = antibody
    self.available = available
    self.celltype = celltype
    self.changed_since = changed_since
    self.comments = comments
    self.description = description
    self.exptype = exptype
    self.genotype = genotype
    self.group = group
    self.id_from = id_from
    self.id_to = id_to
    self.multi_id = multi_id
    self.organism = organism
    self.platform = platform
    self.preparation_kit = preparation_kit
    self.preparation_type = preparation_type
    self.ready_after = ready_after
    self.ready_before = ready_before
    self.received_after = received_after
    self.received_before = received_before
    self.request_id = request_id
    self.request_status = request_status
    self.scientist = scientist
    self.status = status
    self.tissue_type = tissue_type
    self.treatment = treatment

class SampleSorts:
  def __init__(self, group=None, id=None, ready=None, received=None, scientist=None):
    self.group = group
    self.id = id
    self.ready = ready
    self.received = received
    self.scientist = scientist


class ScientistFilters:
  def __init__(self, email=None, firstname=None, fullname=None, group=None, last_change_since=None, last_login_after=None, last_login_before=None, lastname=None, login_ok_max=None, login_ok_min=None, primary_group_name=None, username=None):
    self.email = email
    self.firstname = firstname
    self.fullname = fullname
    self.group = group
    self.last_change_since = last_change_since
    self.last_login_after = last_login_after
    self.last_login_before = last_login_before
    self.lastname = lastname
    self.login_ok_max = login_ok_max
    self.login_ok_min = login_ok_min
    self.primary_group_name = primary_group_name
    self.username = username

class ScientistSorts:
  def __init__(self, fullname=None, group=None, primary_group_name=None):
    self.fullname = fullname
    self.group = group
    self.primary_group_name = primary_group_name


class SequencedSampleFilters:
  def __init__(self, group_id=None, multi_id=[], project=None, request_id=[], sample_id=[], scientist_id=None, status=None):
    self.group_id = group_id
    self.multi_id = multi_id
    self.project = project
    self.request_id = request_id
    self.sample_id = sample_id
    self.scientist_id = scientist_id
    self.status = status

class SequencedSampleSorts:
  def __init__(self, request_id=None, sample_id=None, sequencing_date=None):
    self.request_id = request_id
    self.sample_id = sample_id
    self.sequencing_date = sequencing_date


class SuperMultiFilters:
  def __init__(self, short_seqtype=None):
    self.short_seqtype = short_seqtype

class SuperMultiSorts:
  pass


class WpTicketFilters:
  def __init__(self, assigned_agent=None, category=None, raised_by=None, status=None, subject=None, updated_after=None, updated_before=None):
    self.assigned_agent = assigned_agent
    self.category = category
    self.raised_by = raised_by
    self.status = status
    self.subject = subject
    self.updated_after = updated_after
    self.updated_before = updated_before

class WpTicketSorts:
  def __init__(self, id=None, updated=None):
    self.id = id
    self.updated = updated


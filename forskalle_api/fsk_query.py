
class SortSpec:
  def __init__(self, direction='asc', idx=0):
    self.direction = direction
    self.idx = idx

class FskQuery:
  def __init__(self, sorts=None, filters=None):
    self.sorts = sorts
    self.filters = filters
  
  def generate_params(self):
    params = {}
    if self.filters:
      for k, v in vars(self.filters).items():
        if v and ((type(v).__name__ == 'int' and v>0) or len(v) > 0):
          params['filter.'+k]=v
    if self.sorts:
      for k, v in vars(self.sorts).items():
        if v:
          params['sort.{idx}.{prop}'.format(idx=v.idx, prop=k)]=v.direction
    return params

class FskPagedQuery(FskQuery):
  def __init__(self, page=1, limit=20, *args, **kwargs):
    self.page = page
    self.limit = limit
    super().__init__(*args, **kwargs)
  
  def generate_params(self):
    params = super().generate_params()
    params['page'] = self.page
    params['limit'] = self.limit
    return params
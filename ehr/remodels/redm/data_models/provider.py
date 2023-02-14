from typing import List,Optional
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.provider import Provider

class New(Model):
    Providers: Optional[List[Provider]]

class Update(Model):
    Providers: Optional[List[Provider]]

class Activate(Model):
    Providers: Optional[List[Provider]]


class Deactivate(Model):
    Providers: Optional[List[Provider]]

class ProviderQuery(Model):
    Provider: Optional[Provider]

class ProviderQueryResponse(Model):
    Providers: Optional[List[Provider]]


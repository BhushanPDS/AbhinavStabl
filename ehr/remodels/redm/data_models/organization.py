from datetime import datetime
from typing import List,Optional
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.organization import Organization
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.search import RadiusSearch, NameSearch
from ehr.remodels.redm.schemas.paging import Paging

class New(Model):
    Directory: str = None
    Organizations: Optional[List[Organization]]


class Update(Model):
    Action: str = None
    Directory: str = None
    Organizations: Optional[List[Organization]]

class Query(Model):
    Directory: str = None
    Identifier: Optional[Identifier]
    NameSearch: Optional[NameSearch]
    Stage: Optional[str] 
    RadiusSearch: Optional[RadiusSearch]
    LastUpdate: Optional[datetime]
    Index: Optional[str] 
    Limit: Optional[str] 

class QueryResponse(Model):
    Directory: str = None
    Organizations: Optional[List[Organization]]
    Paging: Optional[Paging]

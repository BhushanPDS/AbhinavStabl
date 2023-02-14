from typing import List,Optional
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.orders import Order
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.location import Location
from ehr.remodels.redm.schemas.type_code import TypeCodeSet
from ehr.remodels.redm.schemas.time import TimeRange

class New(Model):
    Patient: Optional[Patient]
    Orders: Optional[List[Order]]
    Visit: Optional[Visit]

class NewUnsolicited(Model):
    Patient: Optional[Patient] 
    Orders: Optional[List[Order]]
    Visit: Optional[Visit]

class Query(Model):
    Patients: Optional[List[Patient]]
    Completion: Optional[TimeRange]
    ResultStatuses: Optional[List[str]]
    OrderIDs: Optional[List[str]]
    Procedures: Optional[List[TypeCodeSet]]
    Location: Optional[Location]
    LastUpdated: Optional[TimeRange]

class QueryResponse(Model):   #error
    Orders: Optional[List[Order]]

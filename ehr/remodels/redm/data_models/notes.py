from typing import List,Optional
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.orders import Order
from ehr.remodels.redm.schemas.note import Note

class New(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Note: Optional[Note]
    Orders: Optional[List[Order]]

class Replace(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Note: Optional[Note]
    Orders: Optional[List[Order]]

class Delete(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Note: Optional[Note]
    Orders: Optional[List[Order]]

class Query(Model):
    Patients: Optional[List[Patient]]
    VisitNumbers: Optional[List[str]]
    DocumentTypes: Optional[List[str]]
    DocumentIDs: Optional[List[str]]
    
class QueryResponse(Model):
    Notes: Optional[List[Note]]

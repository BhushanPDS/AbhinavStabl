from datetime import datetime
from typing import List,Optional
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.orders import Order
from ehr.remodels.redm.schemas.procedure import Procedure

class New(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Order: Optional[Order]

class Update(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Order: Optional[Order]

class Cancel(Model):
    Patient:Optional[Patient]
    Visit: Optional[Visit]
    Order: Optional[Order]

class GroupedOrders(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Orders: Optional[List[Order]]

class Query(Model):
    Patients: Optional[List[Patient]]
    VisitNumbers: Optional[List[str]]
    StartDateTime: Optional[datetime]
    EndDateTime: Optional[datetime]
    OrderIds: Optional[List[str]]
    Procedures: Optional[List[Procedure]]

class QueryResponse(Model):
    Orders: Optional[List[Order]]


from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.media import Media
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.orders import Order


class New(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Media: Optional[Media]
    Orders: Optional[Order]

class Replace(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Media: Optional[Media]
    Orders: Optional[Order]
    

class Delete(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Media: Optional[Media]
    Orders: Optional[Order]


class Query(Model):
    Patients: Optional[List[Patient]]
    VisitNumbers: Optional[List[str]]
    DocumentTypes: Optional[List[str]]
    DocumentIDs: Optional[List[str]]

class QueryResponse(Model):
    Media: Optional[List[Media]]

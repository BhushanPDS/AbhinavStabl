from typing import Optional,List
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.orders import Order
from ehr.remodels.redm.schemas.admistration import Administrations


class New(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Order: Optional[Order]

class Update(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Order: Optional[Order]

class Cancel(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Order: Optional[Order]


class Administration(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Administrations: Optional[List[Administrations]]

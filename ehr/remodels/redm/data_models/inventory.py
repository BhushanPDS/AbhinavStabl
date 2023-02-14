from typing import Optional,List
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.item import Item
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.visit import Visit


class Update(Model):
    Items: Optional[List[Item]]

class Deplete(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Items: Optional[List[Item]]



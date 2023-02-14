from typing import Optional,List
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.observations import Observation

class New(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Observations: Optional[List[Observation]]


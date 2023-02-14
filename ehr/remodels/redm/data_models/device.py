from typing import Optional, List
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.observations import Observation
from ehr.remodels.redm.schemas.device import Device


class New(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Device: Optional[Device] 
    Observations: Optional[List[Observation]]


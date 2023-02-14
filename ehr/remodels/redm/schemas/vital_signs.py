from datetime import datetime
from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.observations import Observations

class VitalSign(Model):
    DateTime: Optional[datetime]
    Observations: Optional[Observations]


class VitalSigns(Model):
    VitalSignsText: Optional[str] 
    VitalSigns: Optional[List[VitalSign]]

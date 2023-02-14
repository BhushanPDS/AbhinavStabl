from typing import List, Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.observations import Observation
from ehr.remodels.redm.schemas.supplies import Supplies

class FunctionalStatus(Model):
    FunctionalStatusText: Optional[str] 
    Observations: Optional[List[Observation]]
    Supplies: Optional[List[Supplies]] 
    
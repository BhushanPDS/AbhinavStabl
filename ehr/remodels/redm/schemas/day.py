from typing import List,Optional
from datetime import datetime
from ehr.remodels.redm.core.models import Model 
from ehr.remodels.redm.schemas.procedure import Procedure

class Day(Model):
    ID: Optional[str] 
    IDType: Optional[str] 
    Description: Optional[str] 
    ActivityDateTime: Optional[datetime] 
    EarliestDateTime: Optional[datetime]
    LatestDateTime: Optional[datetime]
    Procedures: Optional[List[Procedure]]
    
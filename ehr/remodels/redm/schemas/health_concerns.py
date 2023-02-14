from typing import List,Optional
from datetime import datetime
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.allergy import Commentss

class HealthConcen(TypeCode):
    Status: Optional[bool] = False
    StartDate: Optional[datetime]
    EndDate: Optional[datetime]
    Comments: Optional[List[Commentss]]
    

class HealthConcerns(Model):
    HealthConcernsText: Optional[str] 
    HealthConcerns: Optional[List[HealthConcen]] 

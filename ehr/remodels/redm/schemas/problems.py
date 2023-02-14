from datetime import datetime
from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.allergy import Commentss

class Problem(TypeCode):
    StartDate: Optional[datetime]
    Enddate: Optional[datetime] 
    Category: Optional[TypeCode] 
    HealthStatus: Optional[TypeCode] 
    Status: Optional[TypeCode] 
    Comment: Optional[str]
    Comments: Optional[List[Commentss]]
    Type: Optional[TypeCode] 
    DateTime: Optional[datetime]
    AgeAtOnset: Optional[str] 
    IsCauseOfDeath: Optional[bool] = False
     

class Problems(Model):
    ProblemsText: Optional[str] 
    Problems: Optional[List[Problem]] 
    
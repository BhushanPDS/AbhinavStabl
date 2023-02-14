from datetime import datetime
from typing import List, Type, Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.allergy import Commentss


class Goal(TypeCode):
    AltCodes: Optional[List[TypeCode]] 
    DateTime: Optional[datetime]
    CodeValue: Optional[TypeCode]
    Value: Optional[str] 
    Units: Optional[str] 
    StartDate: Optional[datetime]
    EndDate: Optional[datetime] 
    Priority: Optional[TypeCode] 
    AchievementStatus: Optional[TypeCode] 
    Milestones: Optional[List["Goal"]] 
    Goals: Optional[List[str]]
    Comments: Optional[List[str]]
    Comments: Optional[List[Commentss]]



class Goals(Model):
    GoalsText: Optional[str] 
    Goals: Optional[List[Goal]] 
from datetime import datetime, date
from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.observations import Observations
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.allergy import Commentss

class Pregnancy(TypeCode):
    StartDate: Optional[datetime]
    EndDate: Optional[datetime]
    EstimatedDelivery: Optional[datetime]
    Comments: Optional[List[Commentss]] 

class TobaccoUse(TypeCode):
    IsSmokingStatus: Optional[bool] = False
    StartDate: Optional[str]
    EndDate: Optional[date]
    Comments: Optional[List[Commentss]] 

class SocialHistory(Model):
    SocialHistoryText: Optional[str] 
    Observations: Optional[List[Observations]]
    Pregnancy: Optional[List[Pregnancy]] 
    TobaccoUse: Optional[List[TobaccoUse]] 

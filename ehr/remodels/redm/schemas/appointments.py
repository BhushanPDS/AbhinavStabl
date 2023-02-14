from typing import List,Optional
from datetime import datetime
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.provider import Provider
from ehr.remodels.redm.schemas.location import Location

class AppointmentInfo(Model):
    Code: Optional[str] 
    Codeset: Optional[str] 
    Description: Optional[str]
    Value: Optional[str] 

class Slot(Model):
    ID: Optional[str] 
    DateTime: Optional[datetime]
    Reason: Optional[str]
    Duration: Optional[int] = None
    Provider: Optional[Provider]
    Location: Optional[Location]
    Notes: Optional[List[str]]
    
    
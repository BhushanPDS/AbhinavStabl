from datetime import datetime
from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.procedure import Procedures

class Day(Model):
    ID: Optional[str] 
    IDType: Optional[str] 
    Description: Optional[str] 
    ActivityDateTime: Optional[datetime]
    EarliestDateTime: Optional[datetime]
    LatestDateTime: Optional[datetime]
    Procedures: Optional[Procedures]

class Cycle(Model):
    ID: Optional[str] 
    IDType: Optional[str] 
    Description: Optional[str] 
    StartDate: Optional[datetime]
    EndDate: Optional[datetime]
    Days: Optional[List[Day]]


class Protocol(Model):
    ID: Optional[str] 
    IDType: Optional[str] 
    Description: Optional[str] 
    Cycles: Optional[List[Cycle]]


class Protocols(Model):
    Protocols: Optional[List[Protocol]]

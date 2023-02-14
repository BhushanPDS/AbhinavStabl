from typing import List,Optional
from datetime import datetime
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.observations import Observation
from ehr.remodels.redm.schemas.services import Service
from ehr.remodels.redm.schemas.performer import Performers
from ehr.remodels.redm.schemas.allergy import Commentss
from ehr.remodels.redm.schemas.authorization import Authorization

class Procedure(Model):
    Code: Optional[str] 
    CodeSystem: Optional[str] 
    CodeSystemName: Optional[str] 
    Name: Optional[str]
    AltCodes: Optional[List[TypeCode]] 
    CodeSet: Optional[str] 
    Description: Optional[str] 
    Modifiers: Optional[List[str]] 
    status: Optional[str] 
    Datetime: datetime = None
    TargetSite: Optional[TypeCode]
    Comments: Optional[List[Commentss]]
    Notes: Optional[List[str]]
    Quantity: Optional[str]
    Units: Optional[str]
    StatusReason: Optional[str]
    Duration: int = None
    ProcedureInfo: Optional[List[TypeCode]]


class Procedures(Model):
    PrceduresText: Optional[str] 
    PerformedDateTime: Optional[datetime]
    Performers: Optional[List[Performers]]
    Observations: Optional[List[Observation]]
    Procedures: Optional[List[Procedure]]
    Services: Optional[List[Service]] 
    Authorization: Optional[Authorization]


class SubmittedProcedure(Procedure):
    pass

class AdjudicatedProcedure(Procedure):
    pass

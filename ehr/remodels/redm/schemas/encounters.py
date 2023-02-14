from datetime import datetime
from typing import List, Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.diagnosis import Diagnosis
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.reason_for_visit import ReasonForVisit
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.provider import Provider
from ehr.remodels.redm.schemas.location import Location
from ehr.remodels.redm.schemas.diagnosis import Diagnosis
from ehr.remodels.redm.schemas.reason_for_visit import ReasonForVisit
from ehr.remodels.redm.schemas.type_code import TypeCode

class Encounter(TypeCode):
    Identifiers: Optional[List[Identifier]] 
    Type: Optional[TypeCode]
    DateTime: datetime = None
    EndDateTime: Optional[datetime] 
    Providers: Optional[List[Provider]] 
    Locations: Optional[List[Location]] 
    Diagnosis: Optional[List[Diagnosis]] 
    ReasonForVisit: Optional[List[ReasonForVisit]]
    DischargeDisposition: Optional[TypeCode]
    Status: Optional[str]

    
class Encounters(Model):
    EncountersText: Optional[str]
    Encounters: Optional[List[Encounter]]
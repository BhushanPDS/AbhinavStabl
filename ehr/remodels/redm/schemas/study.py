from typing import List,Optional
from datetime import datetime
from ehr.remodels.redm.schemas.person import Person
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.location import Location
from ehr.remodels.redm.schemas.person import Person
from ehr.remodels.redm.schemas.sponsor import Sponsor
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.eligibility import Eligibility
from ehr.remodels.redm.schemas.provider import Provider


class Design(Model):
    Purpose: str
    Phase: str


class Study(Model):
    Identifiers: Optional[List[Identifier]]
    Title: Optional[str] 
    Type: Optional[str] 
    Sponsor: Optional[Sponsor]
    PrincipalInvestigator: Optional[Person]
    Coordinators: Optional[List[str]]
    Description: Optional[str] 
    Status: Optional[str] 
    StartDateTime: Optional[datetime]
    Conditions: Optional[List[TypeCode]]
    Design: Optional[Design]
    Eligiblity: Optional[Eligibility]
    Location: Optional[Location] 
    Coordinators: Optional[List[Provider]]
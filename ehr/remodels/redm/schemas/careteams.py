from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.organization import Organization
from ehr.remodels.redm.schemas.custodians import Telecom
from ehr.remodels.redm.schemas.encounters import Encounter
from ehr.remodels.redm.schemas.member import Members

class CareTeam(Model):
    Name: Optional[str]
    Status: Optional[str]
    Types: Optional[List[TypeCode]]
    Organization: Optional[Organization]
    Telecom: Optional[List[Telecom]]
    Encounter: Optional[Encounter]
    Members: Optional[List[Members]]

    

class CareTeams(Model):
    CareTeam: Optional[List[CareTeam]]
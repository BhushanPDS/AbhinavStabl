from typing import List,Optional
from datetime import datetime
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.custodians import Custodian
from ehr.remodels.redm.schemas.orderedby_verifiedby_enteredby import VerifiedBy


class AdvanceDirective(TypeCode):
    Type: Optional[TypeCode] 
    StartDate: datetime = None
    EndDate: Optional[datetime]
    ExtenalReference: Optional[str] 
    VerifiedBy: Optional[List[VerifiedBy]]
    Custodians: Optional[List[Custodian]]


class AdvanceDirectives(Model):
    AdvanceDirectives: Optional[List[AdvanceDirective]] 
    AdvanceDirectivesText: Optional[str] 
    
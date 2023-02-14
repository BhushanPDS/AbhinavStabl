from typing import List,Optional
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.core.models import Model



class ReasonForVisit(TypeCode):
    Name: Optional[str]
    ReasonForVisitText: Optional[str] 
    Category: Optional[TypeCode]
    
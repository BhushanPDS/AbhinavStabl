from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.type_code import TypeCode

class Substance(Model):
    Code: str = None
    CodeSystem: Optional[str]
    CodeSystemName: Optional[str] 
    Name: Optional[str] 
    AltCodes:Optional[List[TypeCode]]

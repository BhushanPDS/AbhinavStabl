from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.type_code import TypeCode

class Reaction(Model):
    Code: str = None
    Codeset: Optional[str]
    CodeSystem: Optional[str] 
    CodeSystemName: Optional[str] 
    Name: Optional[str] 
    AltCodes: Optional[List[TypeCode]] 
    Severity: Optional[TypeCode]
    Text: Optional[str] 
    
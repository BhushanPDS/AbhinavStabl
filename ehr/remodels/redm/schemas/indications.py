from typing import Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.type_code import TypeCode

class Indication(TypeCode):
    Code: Optional[str] 
    CodeSet: Optional[str] 
    Description: Optional[str] 
    
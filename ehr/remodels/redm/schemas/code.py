from typing import List,Optional
from ehr.remodels.redm.core.models import Model

class Code(Model):
    Code: Optional[str] 
    CodeSystem: Optional[str] 
    CodeSystemName: Optional[str] 
    Name: Optional[str] 
    AltCodes: Optional[List["Code"]] 
    CodeSet: Optional[str] 
    
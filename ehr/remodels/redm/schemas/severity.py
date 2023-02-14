from typing import Optional
from ehr.remodels.redm.core.models import Model

class Severity(Model):
    Code: Optional[str]
    Codeset: Optional[str]
    CodeSystem: Optional[str] 
    CodeSystemName: Optional[str] 
    Name: Optional[str] 

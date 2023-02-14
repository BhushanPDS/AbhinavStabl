from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.dose import Dose 

class Component(Model):
    Code: Optional[str] 
    CodeSystem: Optional[str] 
    CodeSystemName: Optional[str]
    Name: Optional[str] 
    Type: Optional[str] 
    Dose: Optional[Dose]
    ID: Optional[str]
    Value: Optional[str]
    Comments: Optional[str]

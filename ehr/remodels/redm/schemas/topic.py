from typing import Optional
from ehr.remodels.redm.core.models import Model 

class Topic(Model):
    Code: Optional[str] 
    CodeSet: Optional[str] 
    Description: Optional[str]
    
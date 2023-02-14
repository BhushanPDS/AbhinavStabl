from typing import Optional
from ehr.remodels.redm.core.models import Model

class Manufacturer(Model):
    Code: Optional[str] 
    CodeSet: Optional[str] 
    Name: Optional[str] 
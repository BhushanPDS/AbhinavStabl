from typing import Optional
from ehr.remodels.redm.core.models import Model

class ReferenceRange(Model):
    Low: Optional[int] = None 
    High: Optional[int] = None 
    Text: Optional[str] 
    
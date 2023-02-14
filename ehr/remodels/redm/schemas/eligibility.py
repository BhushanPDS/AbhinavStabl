from typing import Optional
from ehr.remodels.redm.core.models import Model

class Eligibility(Model):
    Gender: Optional[str] 
    MinimumAge: Optional[int] = None
    MaximumAge: Optional[int] = None
    
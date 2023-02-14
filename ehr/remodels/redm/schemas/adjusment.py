from typing import Optional
from ehr.remodels.redm.core.models import Model 

class Adjustments(Model):
    Amount: Optional[str]
    Quantity: Optional[str]
    Type: Optional[str]
    Reason: Optional[str]
    ReasonGroup: Optional[str]
    
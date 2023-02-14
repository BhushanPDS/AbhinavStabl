from typing import Optional
from ehr.remodels.redm.core.models import Model 


class Frequency(Model):
    Period: Optional[int] = None
    PeriodMax: Optional[int] = None
    Unit: Optional[str] 
    EventCode: Optional[str]
    InstitutionSpecified: Optional[bool] = False
    

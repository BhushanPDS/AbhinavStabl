from typing import List,Optional
from ehr.remodels.redm.core.models import Model 

class Asignee(Model):
    Learner: Optional[str] 
    ContentType: Optional[str] 
    Readiness: Optional[str] 
    Response: Optional[str] 
    Notes: Optional[List[str]]
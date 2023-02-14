from datetime import datetime
from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.type_code import TypeCodeSet
from ehr.remodels.redm.schemas.assignment import Assignment

class Education(Model):
    Subject: Optional[TypeCodeSet]
    InstanceID: Optional[str] 
    CreatedDateTime: Optional[datetime]
    Status: Optional[str] 
    ActionStatus: Optional[str] 
    ActionDateTime: Optional[datetime]
    Assignments: Optional[List[Assignment]]

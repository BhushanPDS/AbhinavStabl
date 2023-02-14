from typing import List,Optional
from datetime import datetime
from ehr.remodels.redm.schemas.type_code import TypeCodeSet
from ehr.remodels.redm.schemas.asignees import Asignee

class Assignment(TypeCodeSet):
    Topic: Optional[TypeCodeSet]
    InstanceID: Optional[str] 
    CreatedDateTime: Optional[datetime]
    Status: Optional[str] 
    ActionStatus: Optional[str] 
    ActionDateTime: Optional[datetime]
    Assignees: List[Asignee]

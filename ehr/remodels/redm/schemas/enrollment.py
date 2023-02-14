from typing import Optional, List
from datetime import datetime
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.coordinators import Coordinator

class Enrollment(Model):
    SubjectStatus: Optional[str] 
    StartDateTime: Optional[datetime]
    EndDateTime: Optional[datetime]
    Coordinators: Optional[List[Coordinator]]
    
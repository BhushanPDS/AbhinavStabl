from typing import Optional
from datetime import datetime
from ehr.remodels.redm.core.models import Model

class TimeRange(Model):
    StartDateTime: Optional[datetime]
    EndDateTime: Optional[datetime]

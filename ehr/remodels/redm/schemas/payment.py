from typing import List,Optional
from pydantic import Field
from datetime import datetime
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.claim import Claims
# from ehr.remodels.redm.schemas.identifier import Identifier


class Payments(Model):
    DateTime: Optional[datetime]
    Patient: Optional[Patient]
    Claim: Optional[Claims]
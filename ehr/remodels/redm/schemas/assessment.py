from typing import Optional,List
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.diagnosis import Diagnosis


class Assessment(Model):
    AssessmentText: Optional[str] 
    Diagnoses: Optional[List[Diagnosis]]

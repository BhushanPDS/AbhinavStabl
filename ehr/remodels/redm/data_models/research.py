from typing import List,Optional
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.study import Study
from ehr.remodels.redm.schemas.protocol import Protocol
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.enrollment import Enrollment

class study(Model):
    Study: Optional[Study]
    Protocols: Optional[List[Protocol]]

class SubjectUpdate(Model):
    Enrollment: Optional[Enrollment]
    Patient: Optional[Patient]
    Study: Optional[Study]

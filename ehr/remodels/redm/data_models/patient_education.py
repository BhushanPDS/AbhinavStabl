from typing import Optional, List
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.education import Education

class New(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Education: Optional[List[Education]]

class Update(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit] 
    Education: Optional[List[Education]]

class Delete(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Education: Optional[List[Education]]

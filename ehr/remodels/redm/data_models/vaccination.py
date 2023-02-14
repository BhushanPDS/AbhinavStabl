from typing import List,Optional
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.patient import PotentialMatches,Patient
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.vaccination import Vaccination

class New(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Vaccinations: Optional[List[Vaccination]]

class Administration(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Vaccinations: Optional[List[Vaccination]]

class PatientQuery(Model):
    Patient: Optional[Patient]


class PatientQueryResponse(Model):
    Patient: Optional[Patient]
    PotentialMatches: Optional[List[PotentialMatches]]
    

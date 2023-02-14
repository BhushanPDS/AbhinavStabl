from typing import List,Optional
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.patient import PotentialMatches
from ehr.remodels.redm.schemas.patient import Patient

class Query(Model):
    Patient: Optional[Patient]

class Response(Model):
    Patient: Optional[Patient]
    PotentialMatches: Optional[List[PotentialMatches]]

class LocationQuery(Model):
    Patient: Optional[Patient]

class LocationQueryResponse(Model):
    Patients: Optional[List[Patient]]
    

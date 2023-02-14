from datetime import datetime
from typing import List,Optional
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.visit import Visit

class Arrival(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    
class Cancel(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit] 

class Discharge(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]

class NewPatient(Model):
    Patient: Optional[Patient]

class PatientUpdate(Model):
    Patient: Optional[Patient]

class PatientMerge(Model):
    Patient: Optional[Patient]

class PreAdmit(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit] 

class Registration(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]

class Transfer(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit] 

class VisitMerge(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit] 

class VisitUpdate(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]

class CensusQuery(Model):
    PatientClasses: Optional[List[str]]
    Departments: Optional[List[str]]
    Facilities: Optional[List[str]]

class CensusQueryResponse(Model):
    Patients: Optional[List[Patient]]

class VisitQuery(Model):
    PatientClasses: Optional[List[str]]
    Departments: Optional[List[str]]
    Facilities: Optional[List[str]]
    Patients: Optional[List[Patient]]
    VisitNumbers: Optional[List[str]]
    VisitStartDateTime: Optional[datetime]

class VisitQueryResponse(Model):
    Patients: Optional[List[Patient]]

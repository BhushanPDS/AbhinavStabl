from datetime import datetime
from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.allergy import Commentss

class Diagnosis(TypeCode):
    StartDate: Optional[datetime]
    EndDate: Optional[datetime]
    IsNegativeIndicator: Optional[bool] = False
    Type: Optional[str]
    DocumentedDateTime: Optional[datetime]
    Comments: Optional[List[Commentss]]
    Value: Optional[str]
    DateTime: Optional[datetime]
    Codes: Optional[List[TypeCode]]
    Codeset: Optional[str]
    Notes: Optional[List[str]]
    
class Diagnoses(Model):
    Diagnoses: Optional[List[Diagnosis]]
    
class AdmissionDiagnosis(Diagnosis):
    AdmissionDiagnosisText: Optional[str] 
    AdmissionDiagnosis: Optional[List[Diagnosis]]

class DischargeDiagnosis(Model):
    DischargeDiagnosisText: Optional[str] 
    DischargeDiagnosis: Optional[List[Diagnosis]]
    
from typing import List,Optional
from ehr.remodels.redm.core.models import Model 
from ehr.remodels.redm.schemas.qa import Question
from ehr.remodels.redm.schemas.provider import Provider
from datetime import date , datetime
from ehr.remodels.redm.schemas.adjusment import Adjustments
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.diagnosis import Diagnosis
from ehr.remodels.redm.schemas.procedure import Procedures
from ehr.remodels.redm.schemas.services import Services



class AdditionalDates(Model):
    DateTime: Optional[date]
    Type: Optional[str]

class ReferenceNumbers(Model):
    ID: Optional[str]
    IDType: Optional[str]


class Lines(Model):
    ID: Optional[str]
    Amount: Optional[str]
    Diagnoses: Optional[List[Diagnosis]]
    Procedure: Optional[Procedures]
    ServiceDateTime: Optional[date]
    ServiceEndDateTime: Optional[datetime]
    RevenueCode: Optional[str]
    UnitCount: Optional[str]
    Units: Optional[str]
    IsEmergency: Optional[bool] = False
    Notes: Optional[str]
    


class Claims(Model):
    ID: Optional[str]
    Number: Optional[str]
    SubmissionNumber: Optional[str]
    Type: Optional[str]
    TotalAmount: Optional[str]
    CopayAmount:Optional[str]
    IsProviderSignatureOnFile: Optional[bool] = False
    IsReleaseOfInformationOnFile: Optional[bool] = False
    ProviderAcceptanceCode: Optional[str]
    BenefitsAssignmentCode: Optional[bool] = False
    # AdditionalDates: List[str]
    AdditionalDates: Optional[List[AdditionalDates]]
    ReferenceNumbers: Optional[List[ReferenceNumbers]]
    Diagnoses: Optional[List[Diagnosis]]
    DiagnosisRelatedGroup: Optional[str]
    Providers: Optional[List[Provider]]
    Services: Optional[List[Services]]
    Visit: Optional[Visit]
    ControlNumber: Optional[str]
    ReceivedDate: Optional[datetime]
    StartDateTime: Optional[datetime]
    EndDateTime: Optional[datetime]
    Status: Optional[str]
    ChargedAmount: Optional[str]
    PaymentAmount: Optional[str]
    PatientResponsibilityAmount: Optional[str]
    Adjustments: Optional[List[Adjustments]]
    Procedures: Optional[Procedures]
    Lines: Optional[List[Lines]]
    ReceivedDate: Optional[date]
    ServiceDateTime: Optional[datetime]
    ServiceEndDateTime: Optional[datetime]








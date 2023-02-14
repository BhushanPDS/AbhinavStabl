from typing import List,Optional
from datetime import datetime
from ehr.remodels.redm.core.models import Model 
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.medications import Medications
from ehr.remodels.redm.schemas.indications import Indication
from ehr.remodels.redm.schemas.provider import Provider
from ehr.remodels.redm.schemas.provider import ResultCopyProviders
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.orderedby_verifiedby_enteredby import EnteredBy
from ehr.remodels.redm.schemas.orderedby_verifiedby_enteredby import VerifiedBy
from ehr.remodels.redm.schemas.pharmacy import Pharmacy
from ehr.remodels.redm.schemas.specimen import Specimen
from ehr.remodels.redm.schemas.procedure import Procedure
from ehr.remodels.redm.schemas.diagnosis import Diagnoses, Diagnosis
from ehr.remodels.redm.schemas.clinical_info import ClinicalInfo
# from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.results import Result


class OrderingFacility(Model):
    Name: Optional[str]
    Address: Optional[Address]
    PhoneNumber: Optional[str]

    


class Order(Model):
    Code: Optional[str] 
    CodeSystem: Optional[str] 
    CodeSystemName: Optional[str] 
    Name: Optional[str] 
    AltCodes: Optional[List[TypeCode]] 
    Status: str = None
    Datetime: Optional[datetime] 
    ID: str = None
    Notes: Optional[List[str]]
    Medication: Optional[Medications]
    Indications: Optional[List[Indication]]
    Provider: Optional[Provider]
    EnteredBy: Optional[EnteredBy]
    VerifiedBy: Optional[VerifiedBy]
    Priority: Optional[str]
    Pharmacy: Optional[Pharmacy]
    StartDate: datetime = None
    EndDate: Optional[datetime]
    Quantity: Optional[str]
    Units: Optional[str]
    NumberOfRefillsRemaining: Optional[int]
    ApplicationOrderID: Optional[str]
    TransactionDateTime: Optional[datetime]
    CollectionDateTime: Optional[datetime]
    Specimen: Optional[Specimen]
    Procedure: Optional[Procedure]
    ResultCopyProviders: Optional[List[ResultCopyProviders]]
    OrderingFacility: Optional[OrderingFacility]
    Expiration: Optional[str]
    Comments: Optional[str]
    Diagnoses: Optional[List[Diagnosis]]
    ClinicalInfo: Optional[List[ClinicalInfo]]
    Patients: Optional[List['schemas.Patient']]
    Visit: Optional[Visit]
    CompletionDateTime: Optional[datetime]
    ResultsStatus: Optional[str]
    ResponseFlag: Optional[str]
    Results: Optional[List[Result]]
    LastUpdated: Optional[str]
    EHRID: Optional[str]

from datetime import date, datetime
from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.qa import Question
from ehr.remodels.redm.schemas.drug import Drug
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.adjusment import Adjustments
from ehr.remodels.redm.schemas.diagnosis import Diagnoses
# from ehr.remodels.redm.schemas.procedure import SubmittedProcedure
# from ehr.remodels.redm.schemas.procedure import AdjudicatedProcedure
from ehr.remodels.redm.schemas.allergy import Commentss
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber

class Quantity(Model):
    Value: Optional[str]
    Units: Optional[str]

class ReferenceNumbers(Model):
    ID: Optional[str]
    IDType: Optional[str]

class SubmittedService(Question):
     Modifiers: Optional[str]

class AdjudicatedService(Question):
     Modifiers: Optional[str]

class Service(TypeCode):
    Status: Optional[str]
    DateTime: Optional[date]
    Modifiers: Optional[List[str]]
    Amount: Optional[str]
    StartDateTime: Optional[datetime]
    EndDateTime: Optional[datetime]
    RevenueCode: Optional[str]
    Quantity: Optional[Quantity]
    IsEmergency: Optional[bool] = False
    Diagnoses: Optional[Diagnoses]
    Drug: Optional[Drug]
    Notes: Optional[List[str]]
    ChargedAmount: Optional[str]
    PaymentAmount: Optional[str]
    ChargedUnits: Optional[str]
    PaymentUnits: Optional[str]
    AllowedAmount: Optional[str]
    SubmittedService: Optional[SubmittedService]
    AdjudicatedService: Optional[AdjudicatedService]
    Adjustments: Optional[List[Adjustments]]
    ReferenceNumbers: Optional[List[ReferenceNumbers]]
    DeductibleAmount: Optional[str]
    SubmittedProcedure: Optional[List['schemas.SubmittedProcedure']]
    AdjudicatedProcedure: Optional[List['schemas.AdjudicatedProcedure']]
    ServiceDateTime: Optional[datetime]
    ServiceEndDateTime: Optional[datetime]
    CodeSet: Optional[str] 
    Description: Optional[str]
    Comments: Optional[List[Commentss]]
    Identifiers: Optional[List[Identifier]]
    Type: Optional[str]
    PhoneNumber: Optional[PhoneNumber]
    ServiceDate: Optional[date]
    AuthorizationNumber: Optional[str]
    Decision: Optional[str]
    DecisionReason: Optional[str]
    IssueDate: Optional[date]
    EffectiveDate: Optional[date]
    ExpirationDate: Optional[date]
    



class Services(Model):
    Services: Optional[List[Service]]
    
    

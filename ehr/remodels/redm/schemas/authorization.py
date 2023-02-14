from typing import List,Optional
from datetime import date, datetime
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.company import Company
from ehr.remodels.redm.schemas.diagnosis import Diagnoses
from ehr.remodels.redm.schemas.services import Service
from ehr.remodels.redm.schemas.provider import Provider

class Plan(Model):
    ID: Optional[str]
    IDType: Optional[str]
    Name: Optional[str]

class Request(Plan):
    pass

class Quantity(Model):
    Value: Optional[str]
    Units: Optional[str]

class AdditionalDates(Model):
    DateTime: Optional[datetime]
    Type: Optional[str]



class Authorization(Model):
    Plan: Optional[Plan]
    Company: Optional[Company]
    DateTime: Optional[datetime]
    ExpirationDateTime: Optional[datetime]
    Number: Optional[str]
    ReimbursementLimit: Optional[str]
    RequestedTreatmentCount: Optional[str]
    RequestedTreatmentUnits: Optional[str]
    AuthorizedTreatmentCount: Optional[str]
    Notes: Optional[List[str]]
    Request: Optional[Request]
    AlternateID: Optional[str]
    Type: Optional[str]
    Category: Optional[str]
    CertificationCode: Optional[str]
    ServiceType: Optional[str]
    ServiceLocation: Optional[str]
    RelatedCause: Optional[str]
    ServiceLevel: Optional[str]
    EventDate: Optional[date]
    Quantity: Optional[Quantity]
    AdmissionSource: Optional[str]
    AdmissionType: Optional[str]
    AdditionalDates: Optional[List[AdditionalDates]]
    Diagnoses: Optional[Diagnoses]
    Services: Optional[List[Service]]
    Decision: Optional[str]
    DecisionReason: Optional[str]
    IssueDate: Optional[date]
    EffectiveDate: Optional[date]
    ExpirationDate: Optional[date]
    Providers: Optional[List[Provider]]


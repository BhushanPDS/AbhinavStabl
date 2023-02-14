from typing import List , Optional
from datetime import date, datetime
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.company import Company

class Insured(Model):
    Identifiders: Optional[List[Identifier]]
    LastName: Optional[str] 
    MiddleName: Optional[str] 
    FirstName: Optional[str] 
    SSN: Optional[str] 
    Relationship: Optional[str] 
    DOB: Optional[date]
    Sex: Optional[str] 
    Address: Optional[Address]

class Plan(Identifier):
    Name: Optional[str] 
    Type: Optional[str] 

class Insurance(Model):
    Plan: Optional[Plan]
    MemberNumber: Optional[str]
    Company: Optional[Company]
    GroupNumber: Optional[str]
    GroupName: Optional[str] 
    EffectiveDate: Optional[date] 
    ExpirationDate: Optional[date]
    PolicyNumber: Optional[str]
    Priority: Optional[str]
    AgreementType: Optional[str] 
    CoverageType: Optional[str] 
    Insured: Optional[Insured]
        
class Insurances(Model):
    InsurancesText: Optional[str] 
    Insurances: Optional[List[Insurance]] 

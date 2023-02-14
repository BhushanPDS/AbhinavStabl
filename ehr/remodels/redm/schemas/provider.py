from typing import List,Optional
from ehr.remodels.redm.core.models import Model 
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber
from ehr.remodels.redm.schemas.location import Location
from ehr.remodels.redm.schemas.type_code import TypeCode
# from ehr.remodels.redm.schemas.day import Day
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.demographics import Demographics
from ehr.remodels.redm.schemas.qualifications import Qualifications
from ehr.remodels.redm.schemas.roles import Roles

class Specialty(Model):
    ID: Optional[str] 
    Description: Optional[str] 


class Provider(Model):
    NPI: Optional[str] 
    ID: str = None
    IDType: Optional[str] 
    FirstName: Optional[str] 
    LastName: Optional[str] 
    Credentails: Optional[List[str]]
    Address: Optional[Address]
    EmailAddresses: Optional[List[str]] 
    PhoneNumber: Optional[PhoneNumber]
    Location: Optional[Location]
    Role: Optional[TypeCode] 
    Role:Optional[str]
    Specialty: Optional[Specialty]
    Identifiers: Optional[List[Identifier]]
    IsActive: Optional[bool] = False
    Demographics: Optional[Demographics]
    Qualifications: Optional[List[Qualifications]]
    Roles: Optional[List[Roles]]
    Type: Optional[str]
    ContactInfo: Optional[str]



class AttendingProvider(Provider):
    pass

class ReferringProvider(Provider):
    pass

class ConsultingProvider(Provider):
    pass

class OrderingProviders(Provider):
    pass

class AdministeringProvider(Provider):
    pass

class ResultCopyProviders(Provider):
    pass

class AdmittingProvider(Provider):
    pass

class VisitProvider(Provider):
    pass




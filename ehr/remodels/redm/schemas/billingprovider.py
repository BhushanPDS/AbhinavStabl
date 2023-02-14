from typing import List, Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber
from ehr.remodels.redm.schemas.day import Day  #taking id and description attribute in speciality


class BillingProvider(Model):
    Identifiers: Optional[List[Identifier]]
    Name: Optional[str]
    Address: Optional[Address]
    EmailAddress: Optional[str]
    PhoneNumber: Optional[PhoneNumber]
    Specialty: Optional[Day]
    ID: Optional[str]
    IDType: Optional[str]
    TIN: Optional[str]
    FirstName: Optional[str]
    MiddleName: Optional[str]
    LastName: Optional[str]
    OrganizationName: Optional[str]
    
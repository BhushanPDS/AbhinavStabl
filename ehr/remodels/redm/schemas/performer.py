from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber
from ehr.remodels.redm.schemas.location import Location

class Performers(Model):
    ID: Optional[str]
    IDType: Optional[str]
    FirstName: Optional[str]
    LastName: Optional[str]
    Credentials: Optional[List[str]]
    Address: Optional[Address]
    EmailAddresses: Optional[List[str]]
    PhoneNumber: Optional[PhoneNumber]
    Location: Optional[Location]
    





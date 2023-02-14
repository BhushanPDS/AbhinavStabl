from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber
from ehr.remodels.redm.schemas.location import Location

class Author(Model):
    ID: Optional[str]
    IDType: Optional[str] 
    FirstName: Optional[str]
    LastName: Optional[str] 
    Credentails: Optional[List[str]]
    Address: Optional[Address]
    PhoneNumber: Optional[PhoneNumber]
    Type: Optional[str]
    Location: Optional[Location]
    EmailAddresses: Optional[List[str]]
    
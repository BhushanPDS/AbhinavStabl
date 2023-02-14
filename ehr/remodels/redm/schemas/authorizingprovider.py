from ehr.remodels.redm.core.models import Model
from typing import List,Optional
from ehr.remodels.redm.schemas.address import Address
from typing import Optional
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber
from ehr.remodels.redm.schemas.location import Location

class AuthorizingProvider(Model):
    ID: Optional[str]
    IDType: Optional[str]
    FirstName: Optional[str]
    LastName: Optional[str]
    Credentials: Optional[List[str]]
    Address: Optional[Address] 
    EmailAddresses:Optional[List[str]]
    PhoneNumber: Optional[PhoneNumber]
    Location: Optional[Location]


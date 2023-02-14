from typing import List,Optional
from pydantic import EmailStr
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber
from ehr.remodels.redm.schemas.location import Location


class PCP(Model):
    NPI: Optional[str]
    ID: Optional[str] 
    IDType: Optional[str] 
    FirstName: Optional[str] 
    LastName: Optional[str] 
    Credentails: Optional[List[str]] 
    Address: Optional[Address] 
    EmailAddresses: Optional[List[EmailStr]] 
    PhoneNumber: Optional[PhoneNumber]
    Location: Optional[Location]
    Type: Optional[str]
    
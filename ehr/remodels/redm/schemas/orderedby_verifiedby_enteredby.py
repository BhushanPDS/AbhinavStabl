from datetime import datetime
from typing import List,Optional
from pydantic import EmailStr
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.location import Location
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber


class OrderedBy(Model):
    ID: Optional[str] 
    IDType: Optional[str] 
    FirstName: Optional[str] 
    LastName: Optional[str] 
    Credentails: Optional[List[str]] 
    Address: Optional[Address]
    EmailAddresses: Optional[List[EmailStr]] 
    PhoneNumber: Optional[PhoneNumber]
    Location: Optional[Location]
    DateTime: Optional[datetime]


class VerifiedBy(OrderedBy):
    pass

class EnteredBy(OrderedBy):
    pass


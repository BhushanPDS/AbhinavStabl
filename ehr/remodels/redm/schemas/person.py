from typing import List,Optional
from pydantic import EmailStr
from datetime import datetime
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber
# from ehr.remodels.redm.schemas.location import Location

class Person(Model):
    ID: Optional[str] 
    IDType: Optional[str] 
    FirstName: Optional[str] 
    LastName: Optional[str] 
    Credentials: Optional[List[str]] 
    DateTime: Optional[datetime] 
    Address: Optional[Address]
    EmailAddresses: Optional[List[EmailStr]]
    PhoneNumber: Optional[PhoneNumber]
    Locations: Optional['schemas.Location']
    
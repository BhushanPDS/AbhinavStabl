from typing import List,Optional
from datetime import datetime ,time
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.location import Location
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber

class SurgeryStaff(Identifier):
    FirstName: Optional[str] 
    LastName: Optional[str] 
    Credentils: Optional[List[str]]
    Address: Optional[Address]
    PhoneNumber: Optional[PhoneNumber]
    Location: Optional[Location]
    Role: Optional[TypeCode]
    StartDateTime: Optional[datetime]
    Duration: Optional[time]

class SurgicalInfo(Model):
    Code: Optional[str]
    CodeSet: Optional[str]
    Description: Optional[str]
    Value: Optional[str]

class SurgicalCase(Model):
    Number: Optional[str]
    Status: Optional[str] 
    
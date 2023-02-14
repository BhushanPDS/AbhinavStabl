from typing import List, Optional
from ehr.remodels.redm.core.models import Model 
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.custodians import Telecom
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber


class Location(Model):
    Department: str = None
    Type: Optional[str]
    Facility: Optional[str]
    Room: Optional[str]
    Bed: Optional[str]
    Address: Optional[Address]
    ID: Optional[str]
    Bin: Optional[str]
    Identifiers: Optional[List[Identifier]]
    Telecom: Optional[List[Telecom]]
    Types: List[TypeCode] = None
    Name: Optional[str]
    Status: Optional[str]
    Description: Optional[str]
    EmailAddresses: Optional[List[str]]
    PhoneNumber: Optional[PhoneNumber]





class PreviousLocation(Location):
    pass

class DischargeLocation(Location):
    pass

from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.contact import Contacts
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.endpoint import Endpoint
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.custodians import Telecom
from ehr.remodels.redm.schemas.type_code import SVType

class Type(Model):
    Type: Optional[str] 
    System: Optional[str]
    Value: Optional[str] 

class PartOf(Model):
    Identifier: Optional[Type]

class Organization(Model):
    Active: bool = None
    Name: str = None
    Aliases: Optional[List[str]]
    Identifiers: Optional[List[Identifier]]
    Type: Optional[str]
    Type: Optional[SVType]
    PartOf: Optional[PartOf]
    Contacts: Optional[List[Contacts]]
    Address: Optional[Address]
    Endpoints: Optional[List[Endpoint]]
    Telecom: Optional[List[Telecom]]
    DestinationID: Optional[str]
    ManagingOrg: Optional[str]
    IsActive: Optional[str]
    




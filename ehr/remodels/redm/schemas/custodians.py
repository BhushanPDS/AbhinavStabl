from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.person import Person
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.type_code import TypeCode


class Telecom(Model):
    Value: Optional[str]
    Use: Optional[str]
    System: Optional[str]

class Custodian(Person):
    Address: Optional[Address]
    Identifiers: Optional[List[Identifier]]
    Name: Optional[str]
    Type: Optional[TypeCode]
    Telecom: Optional[List[Telecom]]


    



    


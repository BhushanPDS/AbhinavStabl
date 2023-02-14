from datetime import datetime
from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.custodians import Telecom
from ehr.remodels.redm.schemas.type_code  import TypeCode

class Members(Model):
    Identifier: Optional[List[Identifier]]
    FirstName: Optional[str]
    MiddleName: Optional[str]
    LastName: Optional[str]
    Credentials: Optional[str]
    Address: Optional[Address]
    Telecom: Optional[List[Telecom]]
    StartDateTime: Optional[datetime]
    EndDateTime: Optional[datetime]
    Roles: Optional[List[TypeCode]]


    


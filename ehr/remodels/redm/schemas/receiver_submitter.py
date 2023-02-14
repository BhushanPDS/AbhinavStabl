from typing import List , Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber

class Base(Model):
    Identifiers: Optional[List[Identifier]]
    Name: Optional[str]
    Address: Optional[Address]
    EmailAddress: Optional[str]
    PhoneNumber: Optional[PhoneNumber]



class Receiver(Base):
    pass

class Submitter(Base):
    pass

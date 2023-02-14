from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber



class BaseM(Model):
    ID: Optional[str]
    IDType: Optional[str]
    Name: Optional[str]
    Address: Optional[Address]
    EmailAddress: Optional[str]
    PhoneNumber: Optional[PhoneNumber]


class Payer(BaseM):
    pass
    

class Payee(BaseM):
    pass
    





from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.address import Address


class Company(Model):
    ID: Optional[str] 
    IDType: Optional[str] 
    Name: Optional[str] 
    Address: Optional[Address]
    PhoneNumber: Optional[str]


    

    
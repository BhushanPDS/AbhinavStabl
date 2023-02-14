from datetime import datetime
from typing import List , Optional
from ehr.remodels.redm.core.models import Model 
from ehr.remodels.redm.schemas.qa import Question
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber


class Pharmacy(Question):
    Address: Optional[Address]
    PhoneNumber: Optional[PhoneNumber]



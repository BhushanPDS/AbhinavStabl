from datetime import datetime
from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber

class Contacts(Model):
    FirstName: Optional[str]
    MiddleName: Optional[str]
    LastName: Optional[str]
    Address: Optional[Address]
    PhoneNumber: Optional[PhoneNumber]
    RelationToPatient: Optional[str]
    EmailAddresses: Optional[List[str]]
    Roles: Optional[List[str]]
    Purpose: Optional[str]
    Name: Optional[str]



class Consent(Model):
    Status: Optional[str]
    EffectiveDate: Optional[datetime]
    Notification: Optional[str]
    
from datetime import datetime
from typing import Optional
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.orders import Order
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber

class SignOn(Model):
    Subject: str = None
    Expiration: datetime = None
    IssuedAt: datetime = None
    UserId: Optional[str] 
    Name: Optional[str] 
    FirstName: Optional[str] 
    LastName: Optional[str]
    MiddleName: Optional[str] 
    EmailAddress: Optional[str] 
    NPI: Optional[str] 
    ProviderSpeciality: Optional[str] 
    TimeZone: Optional[str] 
    Locale: Optional[str] 
    PhoneNumber: Optional[PhoneNumber] 
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Order: Optional[Order]


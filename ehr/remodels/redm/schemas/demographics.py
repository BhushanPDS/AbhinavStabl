from ast import Add
from datetime import datetime
from typing import List,Optional
from pydantic import EmailStr
from datetime import date
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.type_code import Confidentiality

 
class EmailAddres(Model):
    Address: Optional[str]


class Demographics(Model):
    FirstName: str = None
    MiddleName: Optional[str]
    LastName: str = None
    DOB: date = None
    SSN: Optional[str]
    Sex: str = None
    Address: Optional[Address]
    PhoneNumber: Optional[PhoneNumber]
    EmailAddresses: Optional[List[str]]
    Language: Optional[str]
    Race: Optional[str]
    Ethnicity: Optional[str] 
    Religion: Optional[str]
    MaritalStatus: Optional[str]
    PCP: Optional[str] 
    Citizenship: Optional[List[str]]
    Credentails: Optional[List[str]] 
    IsHispanic: Optional[bool] = False
    IsDeceased: Optional[bool] = False
    DeathDateTime: Optional[datetime]
    EmailAddresses: Optional[List[EmailAddres]]
    RaceCodes: Optional[List[TypeCode]]
    EthnicGroupCodes: Optional[List[Confidentiality]]
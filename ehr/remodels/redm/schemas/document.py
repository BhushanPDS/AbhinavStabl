from datetime import datetime
from typing import Optional,List
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.author import Author
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.type_code import Confidentiality
from ehr.remodels.redm.schemas.custodians import Custodian
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.type_code import TypeCodeSet
from ehr.remodels.redm.schemas.location import Location

class Document(Model):
    ID: str = None
    Author: Optional[Author]
    Locale: str = None
    Title: str = None
    DateTime: datetime = None
    Type: Optional[str]
    TypeCode: Optional[TypeCode]
    Confidentiality: Optional[Confidentiality]
    Custodian: Optional[Custodian]
    Visit: Optional[Visit]
    StartDate: Optional[datetime]
    EndDate: Optional[datetime]
    Types: Optional[TypeCodeSet]
    Location: Optional[Location]


from datetime import datetime
from typing import List,Optional
from datetime import datetime
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.product import Product
from ehr.remodels.redm.schemas.dose import Dose
from ehr.remodels.redm.schemas.orders import Order
from ehr.remodels.redm.schemas.provider import Provider
from ehr.remodels.redm.schemas.location import Location
from ehr.remodels.redm.schemas.clinical_info import ClinicalInfo

class Vaccination(Model):
    DateTime: datetime = None
    Product: Optional[Product]
    Route: Optional[TypeCode]
    Site: Optional[TypeCode]
    Dose: Optional[Dose]
    Order: Optional[Order]
    ClinicalInfo: Optional[List[ClinicalInfo]]
    Notes: Optional[List[str]]
    RefusalReason: Optional[str]
    Provider: Optional[Provider]
    Location: Optional[Location]
    Action: str = None
    RefusalReason: Optional[str]
    
                        # New, Update, Cancel

class Vaccinations(Model):
    Vaccinations: Optional[List[Vaccination]]

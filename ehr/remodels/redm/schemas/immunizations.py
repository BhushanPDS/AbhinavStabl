from typing import List,Optional
from datetime import datetime
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.product import Product
from ehr.remodels.redm.schemas.dose import Dose

class Immunization(Model):
    DateTime: datetime = None
    Route: Optional[TypeCode] 
    Product: Optional[Product] 
    Dose: Optional[Dose]
    Status: Optional[str]

class Immunizations(Model):
    ImmunizationText: Optional[str] 
    Immunizations: Optional[List[Immunization]] 

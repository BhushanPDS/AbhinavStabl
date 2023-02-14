from datetime import datetime
from typing import Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.dose import Dose 
from ehr.remodels.redm.schemas.rate import Rate 
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.frequency import Frequency
from ehr.remodels.redm.schemas.product import Product

class MedicationAdministration(Model):
    Status: Optional[str] 
    Dose: Optional[Dose] 
    Rate: Optional[Rate] 
    Route: Optional[TypeCode]
    StartDate: datetime = None 
    EndDate: Optional[datetime]
    Frequency: Optional[Frequency]
    Product: Optional[Product]

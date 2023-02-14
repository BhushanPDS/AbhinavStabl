from datetime import datetime
from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.dose import Dose
from ehr.remodels.redm.schemas.rate import Rate
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.frequency import Frequency
from ehr.remodels.redm.schemas.product import Product
from ehr.remodels.redm.schemas.indications import Indication
from ehr.remodels.redm.schemas.orders import Order


class DischargeMedication(Model):
    Prescription: bool = None
    FreeTextSig: Optional[str] 
    Dose: Optional[Dose]
    Rate: Optional[Rate]
    Route: Optional[TypeCode] 
    Status: Optional[str] 
    StartDate: datetime = None
    EndDate: Optional[datetime]
    Frequency: Optional[Frequency]
    NumberOfReffilsRemaining: Optional[int] = None 
    IsPRN: Optional[bool] = False
    Product: Optional[Product]
    Indications: Optional[List[Indication]]
    SupplyOrder: Optional[Order] 

class DischargeMedications(Model):
    DischargeMedicationsText: Optional[str] 
    DischargeMedications: Optional[List[DischargeMedication]]
    
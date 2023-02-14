from typing import List,Optional
from pydantic import Required
from datetime import datetime
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.dose import Dose 
from ehr.remodels.redm.schemas.rate import Rate 
from ehr.remodels.redm.schemas.product import Product
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.frequency import Frequency
from ehr.remodels.redm.schemas.indications import Indication
# from ehr.remodels.redm.schemas.orders import Order
from ehr.remodels.redm.schemas.components import Component
from ehr.remodels.redm.schemas.dispense import Dispense

class Medication(Model):
    Prescription: bool = None
    FreeTextSig: Optional[str] 
    Dose: Optional[Dose]
    Rate: Optional[Rate]
    Route: Optional[TypeCode]
    Status: Optional[str] 
    StartDate: datetime = None
    EndDate: Optional[datetime] 
    Frequency: Optional[Frequency]
    NumberOfRefillsRemaining: Optional[int] = None 
    IsPRN: Optional[bool] = False 
    Product: Optional[Product]
    Indications: Optional[List[Indication]] 
    SupplyOrder: Optional[List['schemas.Order']]
    LotNumber: Optional[str]
    Components: Optional[List[Component]]
    Dispense: Optional[Dispense]



class Medications(Model):
    MedicationsText: Optional[str] 
    Medications: Optional[List[Medication]] 
    
class MedicationsAdministered(Model):
    MedicationsAdministeredText: Optional[str] 
    MedicationsAdministered: Optional[List[Medication]]
    ReasonNotGiven: Optional[str]
    
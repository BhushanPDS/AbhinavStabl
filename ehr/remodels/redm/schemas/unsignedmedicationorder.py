from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.frequency import Frequency
from ehr.remodels.redm.schemas.product import Product
from ehr.remodels.redm.schemas.dose import Dose
from ehr.remodels.redm.schemas.qa import Questions



class MixtureComponent(Model):
    Code: Optional[str]
    CodeType: Optional[str]
    Dose: Optional[Dose]



class UnsignedMedicationOrder(Model):
    Priority: Optional[str]
    Mode: Optional[str]
    Route: Optional[str]
    StartDate: Optional[str]
    EndDate: Optional[str]
    MixtureType: Optional[str]
    Identifiers: Optional[List[Identifier]]
    Frequency: Optional[Frequency]
    Product: Optional[Product]
    Dose: Optional[Dose]
    Questions: Optional[List[Questions]]
    Notes: Optional[List[str]]
    MixtureType: Optional[str]
    MixtureComponents: Optional[List[MixtureComponent]]
    
    
class UnsignedMedicationorders(Model):
    UnsignedMedicationOrders:Optional[List[str]]
    UnsignedMedicationOrders = Optional[List[UnsignedMedicationOrder]]





from typing import List,Optional
from pydantic import Required
from datetime import datetime
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.product import Product
from ehr.remodels.redm.schemas.allergy import Commentss
from ehr.remodels.redm.schemas.procedure import Procedure


class MedicalHistory(Model):
    MedicalHistoryText: Optional[str]


class MedicalEquipmentSchema(Model):
    Status: str = None
    StartDate: Optional[datetime] 
    Quantity: Optional[str] 
    Prodcut: Optional[Product]
    Procedure: Optional[Procedure]
    Comments: Optional[List[Commentss]]
    


class MedicalEquipment(Model):
    MedicalEquipmentText: Optional[str] 
    MedicalEquipment: Optional[List[MedicalEquipmentSchema]] 

from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.orders import Order
from ehr.remodels.redm.schemas.procedure import Procedure
from ehr.remodels.redm.schemas.encounters import Encounter
from ehr.remodels.redm.schemas.supplies import Supplies
from ehr.remodels.redm.schemas.medication_administration import MedicationAdministration
from ehr.remodels.redm.schemas.services import Service

class PlanOfCare(Model):
    PlanOfCareText: Optional[str] 
    Orders: Optional[List[Order]]
    Procedures: Optional[List[Procedure]] 
    Encounters: Optional[List[Encounter]] 
    MedicationAdministration: Optional[List[MedicationAdministration]] 
    Supplies: Optional[List[Supplies]] 
    Services: Optional[List[Service]] 

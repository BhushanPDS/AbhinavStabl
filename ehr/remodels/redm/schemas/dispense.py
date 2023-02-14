from typing import Optional
from ehr.remodels.redm.core.models import Model


class Dispense(Model):
    Amount: Optional[int] = None 
    Units: Optional[str] 
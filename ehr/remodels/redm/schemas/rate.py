from typing import Optional
from ehr.remodels.redm.core.models import Model


class Rate(Model):
    Quantity: Optional[str] 
    Units: Optional[str] 
from typing import Optional
from ehr.remodels.redm.core.models import Model

class Dose(Model):
    Quantitiy: Optional[int] = None 
    Units: Optional[str]

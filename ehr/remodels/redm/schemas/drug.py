from ehr.remodels.redm.core.models import Model
from typing import List,Optional

class Quantity(Model):
    Value: Optional[str]
    Units: Optional[str]

class Drug(Model):
    PrescriptionID: Optional[str]
    NDC: Optional[str]
    Quantity: Optional[Quantity]

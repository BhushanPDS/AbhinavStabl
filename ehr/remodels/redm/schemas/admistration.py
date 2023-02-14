from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.medications import Medications
from ehr.remodels.redm.schemas.provider import AdministeringProvider
from ehr.remodels.redm.schemas.orderedby_verifiedby_enteredby  import OrderedBy
from ehr.remodels.redm.schemas.orderedby_verifiedby_enteredby  import VerifiedBy



class Administrations(Model):
    Status: str = None
    Medication: Optional[Medications]
    StartDate: Optional[str]
    EndDate: Optional[str]
    AdministeringProvider: Optional[AdministeringProvider]
    OrderedBy: Optional[OrderedBy]
    VerifiedBy: Optional[VerifiedBy]


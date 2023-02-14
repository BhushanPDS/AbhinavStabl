from typing import Optional
from ehr.remodels.redm.core.models import Model


class status(Model):
    Code: str = None
    CodeSystem: Optional[str]
    CodeSystemName: Optional[str]
    Name: Optional[str]
    
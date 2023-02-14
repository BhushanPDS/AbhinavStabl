from typing import Optional
from ehr.remodels.redm.core.models import Model


class Criticality(Model):
    Code: Optional[str]
    CodeSystem: Optional[str]
    CodeSystemName: Optional[str]
    Name: Optional[str]
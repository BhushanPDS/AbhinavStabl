from typing import Optional
from ehr.remodels.redm.core.models import Model


class Paging(Model):
    Count: Optional[int] = None
    Index: Optional[int] = None

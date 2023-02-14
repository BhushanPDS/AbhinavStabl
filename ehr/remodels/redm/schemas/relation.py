from typing import List,Optional
from pydantic import Required
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.demographics import Demographics


class Relation(Model):
    Code: str = None
    CodeSystem: Optional[str] 
    CodeSystemName: Optional[str] 
    Name: Optional[str]
    Demographics: Optional[Demographics]
    IsDeceased: Optional[bool] = False
    
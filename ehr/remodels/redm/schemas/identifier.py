from typing import Optional,List
from ehr.remodels.redm.core.models import Model
from pydantic import validator
from pydantic import Field



class Identifier(Model):
    Type: Optional[str] 
    System: Optional[str]
    Value: Optional[str]
    Identifiers: List[str] = None
    ID: str
    IDType: str
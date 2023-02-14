from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.type_code import SVType

class Attributes(Model):
    Transaction: Optional[str]
    Actor: Optional[SVType]
    Version: Optional[SVType]
    UseCases: Optional[List[SVType]]
    PurposeOfUse: Optional[List[SVType]]
    Roles: Optional[List[SVType]]
    

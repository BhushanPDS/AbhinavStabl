from typing import Optional
from ehr.remodels.redm.core.models import Model

class NameSearch(Model):
    SearchType: Optional[str]
    Value: Optional[str] 

class RadiusSearch(Model):
    ZipCode: Optional[str] 
    Radius: Optional[str] 

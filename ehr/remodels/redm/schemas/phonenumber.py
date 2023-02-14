from typing import Optional
from ehr.remodels.redm.core.models import Model

class PhoneNumber(Model):
    Home: Optional[str] 
    Office: Optional[str] 
    Mobile: Optional[str]
    Fax: Optional[str]
    Business: Optional[str]
    Work: Optional[str]
    
    

    
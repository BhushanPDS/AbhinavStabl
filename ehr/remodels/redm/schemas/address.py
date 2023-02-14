from typing import Optional
from ehr.remodels.redm.core.models import Model

class Address(Model):
    use: Optional[str]
    StreetAddress: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip: Optional[str]
    county: Optional[str] 
    country: Optional[str]

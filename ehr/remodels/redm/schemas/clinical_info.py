from typing import List,Optional
from datetime import datetime
from ehr.remodels.redm.core.models import Model

class ClinicalInfo(Model):
    Code: Optional[str]
    CodeSet: Optional[str]
    Description: Optional[str]
    Value: Optional[str]
    ValueType: Optional[str] 
    Units: Optional[str]
    Notes: Optional[List[str]]
    CompletionDateTime: Optional[datetime]
    RelatedGroupID: Optional[str] 
    Abbreviation: Optional[str]
    
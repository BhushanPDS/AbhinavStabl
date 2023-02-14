from typing import Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.document import Document
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.pcp import PCP

class Header(Model):
    Document: Optional[Document] 
    Patient: Optional[Patient]
    DirectAddressFrom: Optional[str]
    DirectAddressTo: Optional[str] 
    PCP: Optional[PCP]
    
    
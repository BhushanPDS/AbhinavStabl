from datetime import datetime
from typing import List,Optional
from pydantic import Required
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.provider import Provider
from ehr.remodels.redm.schemas.authorizingprovider import AuthorizingProvider

class Media(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    FileType: str = None
    FileContents: str = None
    DocumentType: str = None
    DocumentID: str = None
    DocumentDescription: Optional[str]
    CreationDateTime: Optional[datetime]
    ServiceDateTime: Optional[datetime]
    FileName: str = None
    DirectAddressFrom: Optional[str]
    DirectAddressTo: Optional[str]
    Provider: Optional[Provider]
    Authenticated: Optional[str]
    Authenticator: Optional[AuthorizingProvider]
    Availability: str = None
    Notifications: Optional[List[AuthorizingProvider]]
    OriginalDocumentID: str = None


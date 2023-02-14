from typing import List,Optional
from datetime import datetime
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.authorization import Authorization
from ehr.remodels.redm.schemas.diagnosis import Diagnoses
from ehr.remodels.redm.schemas.procedure import Procedure
from ehr.remodels.redm.schemas.provider import Provider
from ehr.remodels.redm.schemas.visit import Visit


class Referral(Model):
    ID: Optional[str]
    IDType: Optional[str]
    AlternateID: Optional[str]
    Type: Optional[str]
    Category: Optional[str]
    Priority: Optional[str]
    Status: Optional[str]
    DateTime: Optional[datetime]
    ExpirationDateTime: Optional[str]
    ProcessDateTime: Optional[str]
    Reason: Optional[str]
    ProviderSpecialty: Optional[str]
    DepartmentSpecialty: Optional[str]
    Notes: Optional[List[str]]
    Authorization:Optional[Authorization]
    Diagnoses: Optional[Diagnoses]
    Procedures: Optional[List[Procedure]]
    Providers: Optional[List[Provider]]
    Visit: Optional[Visit]
    ServiceLocation: Optional[str]
    RequestType: Optional[str]
    RelatedCause: Optional[str]
    StatusReason: Optional[str]
    
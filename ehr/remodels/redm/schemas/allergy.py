from datetime import datetime
from typing import List, Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.substance import Substance
from ehr.remodels.redm.schemas.reaction import Reaction
from ehr.remodels.redm.schemas.severity import Severity
from ehr.remodels.redm.schemas.criticality import Criticality
from ehr.remodels.redm.schemas.status import status

class Commentss(Model):
    Text: Optional[str]


class Allergy(TypeCode):
    Type: Optional[TypeCode]
    Substance: Optional[Substance]
    Reaction: Optional[List[Reaction]]
    Severity: Optional[Severity]
    Criticality: Optional[Criticality]
    Status: Optional[str]
    Statuss: Optional[status]
    StartDate: Optional[datetime]
    EndDate: Optional[datetime]
    Comment: Optional[str]
    AltCodes: Optional[List[TypeCode]]
    Comments: Optional[List[str]]
    Comments:Optional[List[Commentss]]
    Codeset: Optional[str]
    OnsetDateTime: Optional[str]


class Allergies(Model):
    AllergyText: Optional[str]
    Allergies: Optional[List[Allergy]]
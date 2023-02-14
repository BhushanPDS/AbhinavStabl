from typing import List,Optional
from datetime import datetime,date
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.type_code import TypeCodeSet

class Qualifications(TypeCodeSet):
    Identifiers: Optional[List[Identifier]]
    StartDate: Optional[date]
    EndDate: Optional[datetime]




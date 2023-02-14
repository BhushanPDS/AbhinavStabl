from datetime import datetime
from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from datetime import datetime
from ehr.remodels.redm.schemas.status import status
from ehr.remodels.redm.schemas.observations import Observations
from ehr.remodels.redm.schemas.identifier import Identifier


class Specimen(Model):
    CollectionDateTime: Optional[datetime]
    Source: Optional[status]
    Identifiers: Optional[List[Identifier]]
    TargetSite: Optional[status]
    Observations: Optional[List[Observations]]
    Source: Optional[str]
    BodySite: Optional[str]
    ID: Optional[str]
    










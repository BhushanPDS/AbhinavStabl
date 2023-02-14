from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.qa import Question
from ehr.remodels.redm.schemas.qa import Answer


class Session(Model):
    Questions: Optional[List[Question]]
    Answer: Optional[List[Answer]]
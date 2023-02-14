from typing import List, Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.problems import Problem
from ehr.remodels.redm.schemas.relation import Relation


class FamilyHistoryBase(Model):
    Relation: Optional[Relation]
    Problems: Optional[List[Problem]]

class FamilyHistory(Model):
    FamilyHistoryText: Optional[str]
    FamilyHistory: Optional[List[FamilyHistoryBase]]
    
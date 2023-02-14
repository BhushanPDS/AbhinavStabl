from lib2to3.pgen2.token import OP
from ehr.remodels.redm.core.models import Model
from datetime import datetime
from typing import List, Optional
from pydantic import Required
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.status import status
from ehr.remodels.redm.schemas.allergy import Commentss

class ResolvedProblem(TypeCode):
    StartDate: Optional[datetime]
    EndDate: Optional[datetime]
    Category: Optional[TypeCode]
    Status: Optional[status]
    Comment: Optional[str]
    Comment: Optional[List[Commentss]]




class ResolvedProblems(Model):
    ResolvedProblemsText: Optional[str]
    ResolvedProblems: Optional[List[ResolvedProblem]]

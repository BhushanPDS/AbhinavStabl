from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.qa import Question
from ehr.remodels.redm.schemas.qa import Answer
from ehr.remodels.redm.schemas.qa import Questions



class UnsignedProcedureOrder(Model):
    Code: Optional[str]
    Codeset: Optional[str]
    Description: Optional[str]
    Identifiers: Optional[List[Identifier]]
    ScheduledDate: Optional[str]
    Mode: Optional[str]
    BodySite: Optional[Question]
    StartDate: Optional[str]
    EndDate: Optional[str]
    Questions: Optional[List[Questions]]
    Notes: Optional[List[str]]



class UnsignedProcedureOrders(Model):
    UnsignedProcedureOrders:Optional[List[str]]
    UnsignedProcedureOrders:Optional[List[UnsignedProcedureOrder]]

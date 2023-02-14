from ehr.remodels.redm.core.models import Model
from typing import List,Optional
from ehr.remodels.redm.schemas.qa import Question
from ehr.remodels.redm.schemas.qa import Answer

class BaseM(Model):
    ID: Optional[str]
    IDType: Optional[str]
    Title: Optional[str]

class RemovableUnsignedOrders(BaseM):
    pass

class AdditionalUnsignedOrders(BaseM):
    Questions: Optional[List[Question]]


class Question(Question):
    Answers: Optional[List[Answer]]

class Note(Model):
    Text: Optional[str]
    Display: Optional[str]

class DecisionSupport(Model):
    DecisionSupport: Optional[List[Question]]

class AdditionalInfo(Model):
    DecisionSupport: Optional[DecisionSupport]
    Link: Optional[str]



class Error(Model):
    Errors: Optional[List[Question]]


class Advisorie(Model):
    ShowAlert: Optional[bool] = False
    Session: str = None
    RemovableUnsignedOrders: Optional[List[RemovableUnsignedOrders]]
    AdditionalUnsignedOrders: Optional[List[AdditionalUnsignedOrders]]
    Description: Optional[str]
    Notes: Optional[List[Note]]
    AdditionalInfo: Optional[List[AdditionalInfo]]
    Errors: Optional[List[Error]]



class Advisories(Model):
    Advisories: Optional[List[str]]
    Advisories: Optional[List[Advisorie]]
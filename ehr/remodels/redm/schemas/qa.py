from typing import Optional
from ehr.remodels.redm.core.models import Model

class Question(Model):
    Code: str = None
    CodeSet: Optional[str] 
    Description: Optional[str]

class Answer(Model):
    Code: Optional[str] 
    CodeSet: Optional[str] 
    Description: Optional[str]
    Comment:Optional[str]

class Questions(Model):
    Question: Optional[Question]
    Answer: Optional[Answer]

class Chargeable(Question):
    Quantity: Optional[str]
    Amount: Optional[int] = None

class Department(Question):
    Name: Optional[str]

class NDC(Question):
    pass
from typing import List, Optional
from datetime import datetime,date
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.reference_range import ReferenceRange
from ehr.remodels.redm.schemas.supplies import Supplies
from ehr.remodels.redm.schemas.allergy import Commentss
from ehr.remodels.redm.schemas.type_code import AltCodes



class Observer(Model):
    ID: Optional[str]
    IDType: Optional[str]
    FirstName: Optional[str]
    LastName: Optional[str]

class value(Model):
    Code: str = None
    CodeSystem: Optional[str] 
    CodeSystemName: Optional[str] 
    Name: Optional[str] 
    AltCodes: Optional[List[AltCodes]]


class Observation(TypeCode):
    DateTime: Optional[date]
    ValueType: Optional[str]
    Value: Optional[str]
    Units: Optional[str]
    Status: Optional[str]
    Notes: Optional[List[str]]
    Observer: Optional[Observer]
    ReferenceRange: Optional[ReferenceRange]
    AbnormalFlag: Optional[str]
    Code: Optional[str]
    CodeSet: Optional[str] 
    Description: Optional[str]
    CodedValue: Optional[TypeCode]
    Comments:Optional[List[Commentss]]
    Supplies: Optional[List[Supplies]]
    TargetSite: Optional[TypeCode]
    ValueText: Optional[str]
    StartDate: Optional[datetime]
    EndDate: Optional[datetime]
    Interpretation: Optional[str]



class Observations(Model):
    Value: Optional[value]
    Observations: Optional[List[Observation]]
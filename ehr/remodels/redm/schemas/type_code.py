from datetime import datetime
from pydantic import Required
from typing import List,Optional
from ehr.remodels.redm.core.models import Model


class SVType(Model):
    System: Optional[str] 
    Value: Optional[str] 

class TypeCodeSet(Model):
    Code: Optional[str] 
    CodeSet: Optional[str] 
    Description: Optional[str] 
    Name: Optional[str]

class AltCodes(Model):
    Code: str = None
    CodeSystem: Optional[str] 
    CodeSystemName: Optional[str] 
    Name: Optional[str] 

class TypeCode(TypeCodeSet):
    Code: str = None
    CodeSystem: Optional[str] 
    CodeSystemName: Optional[str] 
    Name: Optional[str] 
    AltCodes: Optional[List[AltCodes]]

class Confidentiality(TypeCode):
    pass

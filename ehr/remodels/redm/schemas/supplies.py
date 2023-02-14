from datetime import datetime,date
from typing import Optional
from ehr.remodels.redm.schemas.type_code import TypeCode


class Supplies(TypeCode):
    Status: Optional[str] 
    DateTime: Optional[date] 
    
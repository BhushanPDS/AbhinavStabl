from datetime import datetime
from typing import List,Optional 
from pydantic import Required
from ehr.remodels.redm.schemas.manufacturer import Manufacturer
from ehr.remodels.redm.schemas.code import Code
from ehr.remodels.redm.core.models import Model 
from ehr.remodels.redm.schemas.qa import Question
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.status import status

class Product(Model):
    Manufacturer: Optional[Manufacturer]
    Code: str = None
    CodeSystem: Optional[str] 
    CodeSystemName: Optional[str] 
    Name: Optional[str] 
    AltCodes: Optional[List[TypeCode]]
    LotNumber: Optional[str] 
    CodeSet: Optional[str] 
    Description: Optional[str] 
    ExpirationDate: Optional[datetime]
    Indications: Optional[List[Question]]
    Identifiers: Optional[List[Identifier]]
    DeviceID: Optional[str]
    Issuer: Optional[str]
    SerialNumber: Optional[str]
    DistinctID: Optional[str]
    ManufacturerName: Optional[str]
    LotNumber: Optional[str]
    ManufactureDate: Optional[datetime]
    BrandName: Optional[str]
    ModelNumber: Optional[str]
    CatalogNumber: Optional[str]
    Status: Optional[status]
    SafetyObservations: Optional[List[TypeCode]]













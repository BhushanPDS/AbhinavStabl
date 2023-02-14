from typing import List, Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.procedure import Procedure
from ehr.remodels.redm.schemas.location import Location
from ehr.remodels.redm.schemas.provider import OrderingProviders


class Vendor(Model):
    ID: Optional[str]
    Name: Optional[str]
    CatalogNumber: Optional[str]

class Item(Model):
    Identifiers: Optional[List[Identifier]]
    Description: Optional[str]
    Quantity: Optional[int] = None
    Type: Optional[str]
    Units: Optional[str]
    Procedure: Optional[Procedure]
    Notes: Optional[str]
    Vendor: Optional[Vendor]
    Status: Optional[str]
    IsChargeable: Optional[bool] = False
    ContainsLatex: Optional[bool] = False
    Price: Optional[int] = None
    Location: Optional[Location]
    WastedQuantity: Optional[int] = None
    UsedQuantity: Optional[int] = None
    SerialNumber: Optional[str]
    LotNumber: Optional[str]
    OrderingProvider: Optional[OrderingProviders]

class Items(Model):
    Items: Optional[List[Item]]
    



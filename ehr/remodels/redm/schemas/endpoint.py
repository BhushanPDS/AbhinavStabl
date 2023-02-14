from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.attributes import Attributes

class ConnectionType(Model):
    System: Optional[str] 
    Value: Optional[str]

class Endpoint(Model):
    Identifiers: Optional[List[Identifier]]
    ConnectionType: Optional[ConnectionType]
    Name: Optional[str] 
    Address: Optional[str]
    MIMEType: Optional[str]
    Attributes: Optional[Attributes] 
    DestinationID: Optional[str] 

from datetime import datetime
from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.observations import Observation
from ehr.remodels.redm.schemas.encounters import Encounter
from ehr.remodels.redm.schemas.specimen import Specimen
from ehr.remodels.redm.schemas.provider import Provider
from ehr.remodels.redm.schemas.reference_range import ReferenceRange

class Producer(Identifier):
    Name: Optional[str] 
    Address: Optional[Address]




class Result(TypeCode):
    Status: str = None
    Producer: Optional[Producer]
    Observations: Optional[List[Observation]]
    Encounter: Optional[Encounter]
    Specimen: Optional[Specimen]
    RelatedGroupID: Optional[str]
    Value: Optional[str]
    ValueType: Optional[str]
    CompletionDateTime: Optional[datetime]
    FileType: Optional[str]
    Units: Optional[str]
    Notes: Optional[List[str]]
    AbnormalFlag: Optional[str]
    PrimaryResultsInterpreter: Optional[Provider]
    Performer: Optional[Provider]
    ReferenceRange: Optional[ReferenceRange]
    ObservationMethod: Optional[TypeCode]


class Results(Model):
    RestultText: Optional[str] 
    Results: Optional[List[Result]] 

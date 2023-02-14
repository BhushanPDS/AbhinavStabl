from typing import List,Optional
from datetime import time
from ehr.remodels.redm.core.models import Model 
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.organization import Organization
from ehr.remodels.redm.schemas.type_code import TypeCodeSet
from ehr.remodels.redm.schemas.location import Location
from ehr.remodels.redm.schemas.services import Service


class Availability(Model):
    Days: Optional[List[str]]
    AvailableStartTime: Optional[time]
    AvailableEndTime: Optional[time]




class Roles(Model):
    Identifiers: Optional[List[Identifier]]
    Organization:  Optional[Organization]
    Specialties: Optional[List[TypeCodeSet]]
    Locations: Optional[List[Location]]
    Services: Optional[List[Service]]
    Availability: Optional[List[Availability]]



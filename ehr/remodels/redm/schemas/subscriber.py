from typing import List, Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.demographics import Demographics
from ehr.remodels.redm.schemas.insurances import Insurances
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.address import Address



class Subscribers(Model):
    Identifiers: Optional[List[Identifier]]
    Demographics: Optional[Demographics]
    OrganizationName: Optional[str]
    ResponsibilityLevel: Optional[str]
    Insurance: Optional[Insurances]
    Patients: Optional[List[Patient]]
    ID: Optional[str]
    IDType: Optional[str]
    FirstName: Optional[str]
    MiddleName: Optional[str]
    LastName: Optional[str]
    Address: Optional[Address]
    DOB: Optional[str]
    Sex: Optional[str]
    RelationToPatientP: Optional[str]
    ResponsibilityLevel: Optional[str]
    
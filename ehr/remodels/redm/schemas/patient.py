from typing import List, Optional
from ehr.remodels.redm.core.models import Model 
from ehr.remodels.redm.schemas.demographics import Demographics
from ehr.remodels.redm.schemas.identifier import Identifier
from ehr.remodels.redm.schemas.contact import Contacts
from ehr.remodels.redm.schemas.claim import Claims
from ehr.remodels.redm.schemas.organization import Organization
from ehr.remodels.redm.schemas.diagnosis import Diagnosis
from ehr.remodels.redm.schemas.allergy import Allergies
from ehr.remodels.redm.schemas.pcp import PCP
from ehr.remodels.redm.schemas.visit import Guarantor
from ehr.remodels.redm.schemas.insurances import Insurance
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.contact import Consent
from ehr.remodels.redm.schemas.vaccination import Vaccination


class PatientQuery(Model):
    Identifiers: List[Identifier]
    
class Patient(Model):
    Identifiers: Optional[List[Identifier]]
    Demographics: Optional[Demographics]
    Insurances: Optional[List[str]]
    Contacts: Optional[List[Contacts]]
    Notes: Optional[List[str]]
    RelationToSubscriber: Optional[str]
    Claims: Optional[List[Claims]]
    Weight: Optional[str]
    IsPregnant: Optional[str]
    Allergies: Optional[List[Allergies]]
    Organization: Optional[Organization]
    Diagnoses: Optional[List[Diagnosis]]
    PCP: Optional[PCP]
    Guarantor: Optional[Guarantor]
    Insurances: Optional[List[Insurance]]
    Visits: Optional[List[Visit]]
    Consent: Optional[Consent]
    Vaccinations: Optional[List[Vaccination]]


class PotentialMatches(Patient):
    pass


    

    


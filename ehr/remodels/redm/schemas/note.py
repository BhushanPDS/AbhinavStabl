from typing import List,Optional
from datetime import datetime
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.provider import Provider
from ehr.remodels.redm.schemas.person import Person
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.encounters import Encounters
from ehr.remodels.redm.schemas.components import Component
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.visit import Visit

class Note(TypeCode):
    ContentType: str = None
    FileContents: str = None
    FileName: Optional[str] 
    FileType: Optional[str] 
    DocumentType: str = None
    DocumentID: str = None
    DocumentDescription: Optional[str] 
    ServiceDateTime: Optional[datetime]
    DocumentationDateTime: Optional[datetime]
    Status: Optional[str] 
    Availability: Optional[str] 
    Provider: Optional[Provider]
    Authenticator: Optional[Person] 
    Notifications: Optional[List[Person]]
    DateTime: Optional[datetime]
    Encounter: Optional[Encounters]
    Components: Optional[List[Component]]
    OriginalDocumentID: str = None
    Patient: Optional[Patient]
    Visit: Optional[Visit]



class NoteSection(TypeCode):
    Title: str = None
    Text: Optional[str]
    Notes: Optional[List[Note]]
    Encounter: Optional[List[Encounters]]


class NoteSections(Model):
    NoteSections: Optional[List[NoteSection]]


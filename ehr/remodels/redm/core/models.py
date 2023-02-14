from typing import List, Dict, Tuple, Union, Optional
from pydantic import BaseModel
from datetime import datetime

from ehr.remodels.redm.core.enums import DataModels, EventTypes

class Model(BaseModel):
    pass

class Source(Model):
    ID: Optional[str] 
    Name: Optional[str]

class Destination(Model):
    ID: Optional[str] 
    Name: Optional[str]

class Log(Model):
    ID: Optional[str]
    AttemptID: Optional[str]

class Message(Model):
    ID: Optional[str] 

class Transmission(Model):
    ID: Optional[str] 

class Meta(Model):
    """
    Meta data for the API
    """
    DataModel: DataModels
    EventType: EventTypes
    EventDateTime: Optional[datetime]
    Test: Optional[bool] = False
    CanceledEvent: Optional[str] 
    Source: Optional[Source]
    Destinations: Optional[List[Destination]]
    Logs: Optional[List[Log]]
    Message: Optional[Message]
    MessageID: Optional[int] = None
    Transmission: Optional[Transmission]
    FacilityCode: Optional[str]
    IsIncomplete: Optional[bool]= False
    BatchID: Optional[str]
    CurrentBatch: Optional[int] = None
    TotalBatches: Optional[int] = None


class DataModelBase(Model):
    """
    Base class for all data models
    """
    Meta: Optional[Meta]

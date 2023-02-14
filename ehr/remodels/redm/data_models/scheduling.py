from datetime import datetime
from typing import List,Optional
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.appointments import AppointmentInfo, Slot

class New(Model):
    Patient: Optional[Patient]
    AppointmentInfo: Optional[List[AppointmentInfo]]
    Visit: Optional[Visit]

class Reschedule(Model):
    Patient: Optional[Patient]
    AppointmentInfo: Optional[List[AppointmentInfo]]
    Visit: Optional[Visit]

class Modification(Model):
    Patient: Optional[Patient]
    AppointmentInfo: Optional[List[AppointmentInfo]]
    Visit: Optional[Visit]

class Cancel(Model):
    Patient: Optional[Patient]
    AppointmentInfo: Optional[List[AppointmentInfo]]
    Visit: Optional[Visit]

class NoShow(Model):
    Patient: Optional[Patient]
    AppointmentInfo: Optional[List[AppointmentInfo]]
    Visit: Optional[Visit]


class PushSlots(Model):
    Slots: Optional[List[Slot]]

class AvailableSlots(Model):
    Patient: Optional[Patient]
    StartDateTime: Optional[datetime]
    EndDateTime: Optional[datetime]
    Visit: Optional[Visit]

class AvailableSlotsResponse(Model):
    AvailableSlots: Optional[List[Slot]]


class Booked(Model):    #error
    StartDateTime: Optional[datetime]
    EndDateTime: Optional[datetime]
    Visit: Optional[Visit]

class BookedResponse(Model):
    Visits: Optional[List[Visit]]

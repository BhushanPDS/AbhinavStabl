from typing import List,Optional
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.procedure import Procedures
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.surgical import SurgeryStaff, SurgicalCase, SurgicalInfo


class New(Model):
    Patient: Optional[Patient]
    Procedures: Optional[List[Procedures]]
    SurgeryStaff: Optional[List[SurgeryStaff]]
    SurgicalInfo: Optional[List[SurgicalInfo]]
    Visit: Optional[Visit] 
    SurgicalCase: Optional[SurgicalCase]

class Reschedule(Model):
    Patient: Optional[Patient]
    Procedures: Optional[List[Procedures]]
    SurgeryStaff: Optional[List[SurgeryStaff]]
    SurgicalInfo: Optional[List[SurgicalInfo]]
    Visit: Optional[Visit]
    SurgicalCase: Optional[SurgicalCase]

class Modification(Model):
    Patient: Optional[Patient]
    Procedures: Optional[List[Procedures]]
    SurgeryStaff: Optional[List[SurgeryStaff]]
    SurgicalInfo: Optional[List[SurgicalInfo]]
    Visit: Optional[Visit]
    SurgicalCase: Optional[SurgicalCase]


class Cancel(Model):
    Patient: Optional[Patient]
    Procedures: Optional[List[Procedures]]
    SurgeryStaff: Optional[List[SurgeryStaff]]
    SurgicalInfo: Optional[List[SurgicalInfo]]
    Visit: Optional[Visit]
    SurgicalCase: Optional[SurgicalCase]

class NoShow(Model):
    Patient: Optional[Patient]
    Procedures: Optional[List[Procedures]]
    SurgeryStaff: Optional[List[SurgeryStaff]]
    SurgicalInfo: Optional[List[SurgicalInfo]]
    Visit: Optional[Visit]
    SurgicalCase: Optional[SurgicalCase]

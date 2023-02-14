from typing import Optional,List
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.session import Session
from ehr.remodels.redm.schemas.provider import OrderingProviders
from ehr.remodels.redm.schemas.authorizingprovider import AuthorizingProvider
from ehr.remodels.redm.schemas.unsignedmedicationorder import UnsignedMedicationOrder
from ehr.remodels.redm.schemas.UnsignedProcedureOrders import UnsignedProcedureOrder
from ehr.remodels.redm.schemas.advisories import Advisorie


class Request(Model):
    Session: Optional[Session]
    Patient: Optional[Patient]
    OrderingProvider: Optional[OrderingProviders]
    AuthorizingProvider: Optional[AuthorizingProvider]
    UnsignedMedicationOrders: Optional[List[UnsignedMedicationOrder]]
    UnsignedProcedureOrders: Optional[List[UnsignedProcedureOrder]]


class Response(Model):
    Advisories: Optional[List[Advisorie]]
     

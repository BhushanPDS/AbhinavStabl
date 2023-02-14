from typing import Optional,List
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.referral import Referral
from ehr.remodels.redm.schemas.authorization import Authorization

class New(Model):
    Referral: Optional[Referral]
    Patient: Optional[Patient]
    Visit: Optional[Visit]

class Modify(Model):
    Referral: Optional[Referral]
    Patient: Optional[Patient]
    Visit: Optional[Visit]

class Cancel(Model):
    Referral: Optional[Referral] 
    Patient: Optional[Patient]
    Visit: Optional[Visit]

class AuthReview(Model):
    Referral: Optional[Referral]
    Patient: Optional[Patient]
    Authorization: Optional[Authorization]

class AuthResponse(Model):
    Referral: Optional[Referral]
    Patient: Optional[Patient]
    Authorization: Optional[Authorization]

class Query(Model):
    Patient: Optional[Patient]

class QueryResponse(Model):
    Referrals: Optional[List[Referral]]
    
from typing import List, Optional
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.transaction import Transaction

class Transaction(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]
    Transactions: Optional[List[Transaction]]

class AccountUpdate(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]



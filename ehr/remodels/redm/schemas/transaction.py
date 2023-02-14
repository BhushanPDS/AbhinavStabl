from datetime import datetime
from typing import List, Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.receiver_submitter import Submitter
from ehr.remodels.redm.schemas.receiver_submitter import Receiver
from ehr.remodels.redm.schemas.submission import Submission
from ehr.remodels.redm.schemas.payment import Payments
from ehr.remodels.redm.schemas.performer import Performers
from ehr.remodels.redm.schemas.procedure import Procedure
from ehr.remodels.redm.schemas.diagnosis import Diagnoses, Diagnosis
from ehr.remodels.redm.schemas.provider import OrderingProviders
from ehr.remodels.redm.schemas.qa import Chargeable
from ehr.remodels.redm.schemas.qa import Department
from ehr.remodels.redm.schemas.qa import NDC


class Transaction(Model):
    ID: str = None
    IDType: str = None
    Type: Optional[str]
    Submitter: Optional[Submitter]
    Receiver: Optional[Receiver]
    Submissions: Optional[List[Submission]]
    TotalPaymentAmount: Optional[str]
    CreditOrDebit: Optional[str]
    PaymentMethod: Optional[str]
    PaymentDateTime: Optional[str]
    TrackingNumber: Optional[str]
    Payments: Optional[List[Payments]]
    DateTimeOfService: datetime = None
    EndDateTime: Optional[datetime]
    Department: Optional[Department]
    Chargeable: Optional[Chargeable]
    Diagnoses: Optional[List[Diagnosis]]
    Performers: Optional[List[Performers]]
    OrderingProviders: Optional[List[OrderingProviders]]
    OrderID: Optional[str]
    Procedure: Optional[Procedure]
    NDC: Optional[NDC]
   









    


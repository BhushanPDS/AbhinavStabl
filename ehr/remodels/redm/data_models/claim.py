from typing import List,Optional
from ehr.remodels.redm.core.models import DataModelBase as Model
from ehr.remodels.redm.schemas.transaction import Transaction
from ehr.remodels.redm.schemas.billingprovider import BillingProvider
from ehr.remodels.redm.schemas.subscriber import Subscribers
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.claim import Claims
from ehr.remodels.redm.schemas.payer import Payer
from ehr.remodels.redm.schemas.payer import Payee
from ehr.remodels.redm.schemas.payment import Payments



class SubmissionBatch(Model):
    Transactions: Optional[List[Transaction]]


class PaymentBatch(Model):
    Transactions:Optional[List[Transaction]]

class Submission(Model):
    Transaction: Optional[Transaction]
    BillingProvider: Optional[BillingProvider]
    Subscriber: Optional[Subscribers]
    Patient: Optional[Patient]
    Claims: Optional[List[Claims]]

class Payment(Model):
    Transaction: Optional[Transaction]
    Payer: Optional[Payer]
    Payee: Optional[Payee]
    Payments: Optional[List[Payments]]



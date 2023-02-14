from ehr.remodels.redm.core.models import Model
from typing import List,Optional
from ehr.remodels.redm.schemas.billingprovider import BillingProvider
from ehr.remodels.redm.schemas.subscriber import Subscribers

class Submission(Model):
    BillingProvider: Optional[BillingProvider]
    Subscribers: Optional[List[Subscribers]]
    
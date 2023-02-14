
from ehr.epic.client import EpicFHIRClient
from ehr.epic.urls import EPIC_R4_URLS


class Coverage(EpicFHIRClient):
    def __init__(self, customer_id, connection_id) -> None:
        super().__init__(customer_id, connection_id)

    def search_insurance(self, **kwargs):

        url = self.build_url(
            EPIC_R4_URLS['Financial']['Coverage']['search_coverage']['path'],

        )
        return self.get(url, params=kwargs)

from ehr.epic.client import EpicFHIRClient
from ehr.epic.urls import EPIC_R4_URLS


class MedicationRequest(EpicFHIRClient):
    def __init__(self, customer_id, connection_id) -> None:
        super().__init__(customer_id, connection_id)

    def get_orders(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Medication"]["MedicationRequest"]["search_orders"]["path"],
        )

        return self.get(url, params={"patient": kwargs.get("patientid")})

from ehr.epic.client import EpicFHIRClient
from ehr.epic.urls import EPIC_R4_URLS


class DocumentReference(EpicFHIRClient):
    def __init__(self, customer_id, connection_id) -> None:
        super().__init__(customer_id, connection_id)
        
    def search_external_CCDA_document(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["DocumentReference"][
                "search_external_CCDA_document"
            ]["path"],
        )

        return self.get(url, params=kwargs)

    def search_clinical_notes(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["DocumentReference"]["search_clinical_notes"][
                "path"
            ],
        )
        return self.get(url, params=kwargs)

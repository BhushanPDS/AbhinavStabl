from ehr.epic.client import EpicFHIRClient
from ehr.epic.urls import EPIC_R4_URLS


class AllergyIntolerance(EpicFHIRClient):
    def __init__(self, customer_id, connection_id) -> None:
        super().__init__(customer_id, connection_id)

    def create_new_allergy_intolerance(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Clinic"]["AllergyIntolerance"][
                "create_new_allergy_intolerance"
            ]["path"]
        )
        payload = self.build_payload(945, **kwargs)
        return self.post(url, data=payload)

    def get_specific_allergy_intolerance(self, ID):
        url = self.build_url(
            EPIC_R4_URLS["Clinic"]["AllergyIntolerance"][
                "get_specific_allergy_intolerance"
            ]["path"],
            ID=ID,
        )

        return self.get(url)

    def search_allergy_intolerance(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Clinic"]["AllergyIntolerance"]["search_allergy_intolerance"][
                "path"
            ]
        )
        return self.get(url, params=kwargs)

class Condition(EpicFHIRClient):
    def __init__(self, customer_id, connection_id) -> None:
        super().__init__(customer_id, connection_id)


    def search_encounter_diagnosis(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Clinic"]["Condition"]["search_encounter_diagnosis"][
                "path"
            ]
        )
        return self.get(url, params=kwargs)


class Procedure(EpicFHIRClient):
    def __init__(self, customer_id, connection_id) -> None:
        super().__init__(customer_id, connection_id)

    def get_specific_orders(self, ID):
        url = self.build_url(
            EPIC_R4_URLS["Clinic"]["Procedure"]["get_specific_orders"]["path"], ID=ID
        )

        return self.get(url)

    def get_specific_surgeries(self, ID):
        url = self.build_url(
            EPIC_R4_URLS["Clinic"]["Procedure"]["get_specific_surgeries"]["path"], ID=ID
        )

        return self.get(url)

    def get_specific_surgical_history(self, ID):
        url = self.build_url(
            EPIC_R4_URLS["Clinic"]["Procedure"]["get_specific_surgical_history"][
                "path"
            ],
            ID=ID,
        )

        return self.get(url)

    def search_patient_procedure(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Clinic"]["Procedure"]["search_procedure"]["path"],
        )
        return self.get(url, params=kwargs)

    def search_surgeries(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Clinic"]["Procedure"]["search_surgeries"]["path"], **kwargs
        )

        return self.get(url)

    def search_surgical_history(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Clinic"]["Procedure"]["search_surgical_history"]["path"],
            **kwargs
        )

        return self.get(url)

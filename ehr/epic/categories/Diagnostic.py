from ehr.epic.client import EpicFHIRClient
from ehr.epic.urls import EPIC_R4_URLS


class Observation(EpicFHIRClient):
    def __init__(self, customer_id, connection_id) -> None:
        super().__init__(customer_id, connection_id)

    def create_new_LDA_W(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["create_new_LDA_W"]["path"]
        )
        payload = self.build_payload(962, **kwargs)
        return self.post(url, data=payload)

    def create_new_vitals(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["create_new_vitals"]["path"]
        )
        payload = self.build_payload(963, **kwargs)
        return self.post(url, data=payload)

    def get_activities_of_daily_living(self, ID):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["get_activities_of_daily_living"][
                "path"
            ],
            ID=ID,
        )

        return self.get(url)

    def get_core_characteristics(self, ID):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["get_core_characteristics"][
                "path"
            ],
            ID=ID,
        )

        return self.get(url)

    def get_labs(self, ID):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["get_labs"]["path"], ID=ID
        )

        return self.get(url)

    def get_LDA_W(self, ID):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["get_LDA_W"]["path"], ID=ID
        )

        return self.get(url)

    def get_specific_obstetric_details(self, ID):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["get_specific_obstetric_details"][
                "path"
            ],
            ID=ID,
        )

        return self.get(url)

    def get_specific_periodontal(self, ID):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["get_specific_periodontal"][
                "path"
            ],
            ID=ID,
        )

        return self.get(url)

    def get_smart_data_elements(self, ID):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["get_smart_data_elements"][
                "path"
            ],
            ID=ID,
        )

        return self.get(url)

    def get_social_history(self, ID):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["get_social_history"]["path"],
            ID=ID,
        )

        return self.get(url)

    def get_specific_vatals(self, ID):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["get_specific_vatals"]["path"],
            ID=ID,
        )

        return self.get(url)

    def search_activities_of_daily_living(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"][
                "search_activities_of_daily_living"
            ]["path"],
            **kwargs
        )

        return self.get(url)

    def search_core_characteristics(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["search_core_characteristics"][
                "path"
            ],
            **kwargs
        )

        return self.get(url)

    def search_labs(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["search_labs"]["path"], **kwargs
        )

        return self.get(url)

    def search_LDA_W(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["search_LDA_W"]["path"], **kwargs
        )

        return self.get(url)

    def search_obstetric_details(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["search_obstetric_details"][
                "path"
            ],
            **kwargs
        )

        return self.get(url)

    def search_periodontal(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["search_periodontal"]["path"],
            **kwargs
        )

        return self.get(url)

    def search_smart_data_elements(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["search_smart_data_elements"][
                "path"
            ],
            **kwargs
        )

        return self.get(url)

    def search_social_history(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["search_social_history"]["path"],
            **kwargs
        )

        return self.get(url)

    def search_vitals(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["search_vitals"]["path"]
        )

        return self.get(url, params=kwargs)

    def update_LDA_W(self, ID, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Diagnostic"]["Observation"]["update_LDA_W"]["path"], ID=ID
        )
        payload = self.build_payload(974, **kwargs)
        return self.put(url, data=payload)


class ServiceRequest(EpicFHIRClient):
    def __init__(self, customer_id, connection_id) -> None:
        super().__init__(customer_id, connection_id)

    def search_patient_order(self, **kwargs):

        url = self.build_url(
            EPIC_R4_URLS['Diagnostic']['ServiceRequest']['search_orders']['path'],
        )
        return self.get(url, params={"patient": kwargs.get("patientid")})

    def get_patient_order(self, order_id, **kwargs):

        url = self.build_url(
            EPIC_R4_URLS['Diagnostic']['ServiceRequest']['get_orders']['path'],
            ID=order_id
        )
        return self.get(url)
    
    
class DiagnosticReport(EpicFHIRClient):
    def __init__(self, customer_id, connection_id) -> None:
        super().__init__(customer_id, connection_id)

    def search_diagnosis(self, **kwargs):

        url = self.build_url(
            EPIC_R4_URLS['Diagnostic']['DiagnosticReport']['search_results']['path'],
        )
        return self.get(url, params={"patient": kwargs.get("patientid")})

    def get_diagnosis(self, lab_id, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS['Diagnostic']['DiagnosticReport']['get_results']['path'],
            ID=lab_id
        )
        return self.get(url)
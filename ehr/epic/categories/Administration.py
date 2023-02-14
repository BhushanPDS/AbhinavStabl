from ehr.epic.client import EpicFHIRClient
from ehr.epic.urls import EPIC_R4_URLS


class Patient(EpicFHIRClient):
    def __init__(self, customer_id, connection_id) -> None:
        super().__init__(customer_id, connection_id)

    def get_specific_patient(self, ID):
        url = self.build_url(
            EPIC_R4_URLS["Administration"]["Patient"]["get_specific_patient"]["path"],
            ID=ID,
        )

        return self.get(url)

    def search_patient(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Administration"]["Patient"]["search_patient"]["path"],
            **kwargs
        )

        return self.get(url)


class Practitioner(EpicFHIRClient):
    def __init__(self, customer_id, connection_id) -> None:
        super().__init__(customer_id, connection_id)

    def get_specific_practitioner(self, ID):
        url = self.build_url(
            EPIC_R4_URLS["Administration"]["Practitioner"]["get_specific_practitioner"][
                "path"
            ],
            ID=ID,
        )

        return self.get(url)

    def search_practitioner(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Administration"]["Practitioner"]["search_practitioner"][
                "path"
            ],
            **kwargs
        )

        return self.get(url)


class Organization(EpicFHIRClient):
    def __init__(self, customer_id, connection_id) -> None:
        super().__init__(customer_id, connection_id)

    def get_specific_organization(self, ID):
        url = self.build_url(
            EPIC_R4_URLS["Administration"]["Organization"]["get_specific_organization"][
                "path"
            ],
            ID=ID,
        )

        return self.get(url)

    def search_organization(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Administration"]["Organization"]["search_organization"][
                "path"
            ],
            **kwargs
        )

        return self.get(url)


class Location(EpicFHIRClient):
    def __init__(self, customer_id, connection_id) -> None:
        super().__init__(customer_id, connection_id)

    def get_specific_location(self, ID):
        url = self.build_url(
            EPIC_R4_URLS["Administration"]["Location"]["get_specific_location"]["path"],
            ID=ID,
        )
        return self.get(url)

    def search_location(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Administration"]["Location"]["search_location"]["path"],
            **kwargs
        )

        return self.get(url)


class List(EpicFHIRClient):
    def __init__(self, customer_id, connection_id) -> None:
        super().__init__(customer_id, connection_id)


    def search_medication(self, **kwargs):
        url = self.build_url(
            EPIC_R4_URLS["Administration"]["List"]["search_medications"]["path"]
        )
        
        return self.get(url,params=kwargs)
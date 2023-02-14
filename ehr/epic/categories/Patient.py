from ehr.epic.client import EpicFHIRClient
from ehr.epic.urls import EPIC_R4_URLS


class Patient(EpicFHIRClient):
    def __init__(self, customer_id, connection_id) -> None:
        super().__init__(customer_id, connection_id)

    def create_new_patient(self, **kwargs):
        return self.client.resource("Patient", **kwargs).save()


    def get_specific_patient(self, ID):

        url = self.build_url(
            EPIC_R4_URLS["Administration"]['Patient']['get_specific_patient']['path'],
            ID=ID
        )
        return self.get(url)

    # def search_patient(self, **kwargs):
    #     url = self.build_url(
    #         EPIC_R4_URLS["Administration"]["Patient"]["search_patient"]["path"],
    #     )

    #     return self.get(
    #         url,
    #         params={
    #             "name": kwargs.get("firstname"),
    #             "family": kwargs.get("lastname"),
    #             "birthdate": kwargs.get("dob"),
    #         },
    #     )
    def search_patient(self, **kwargs):

        url = self.build_url(
            EPIC_R4_URLS["Administration"]["Patient"]["search_patient"]["path"],
        )
        return self.get(url, params=kwargs)
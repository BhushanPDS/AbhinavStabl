from ehr.epic.client import EpicFHIRClient


class Organization(EpicFHIRClient):
    def __init__(self, customer_id, connection_id) -> None:
        super().__init__(customer_id, connection_id)

    def get_specific_organization(self, ID):
        return self.client.reference("Organization", ID).to_resource().serialize()

    def search_organization(self, **kwargs):
        response_list = [
            response.serialize()
            for response in self.client.resources("Organization")
            .search(**kwargs)
            .fetch()
        ]
        return response_list

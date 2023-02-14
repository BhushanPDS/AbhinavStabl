from ehr.epic.client import EpicFHIRClient


class Practitioner(EpicFHIRClient):
    def __init__(self, customer_id, connection_id) -> None:
        super().__init__(customer_id, connection_id)

    def get_specific_practitioner(self, ID):
        return self.client.reference("Practitioner", ID).to_resource().serialize()

    def search_practitioner(self, **kwargs):
        response_list = [
            response.serialize()
            for response in self.client.resources("Practitioner")
            .search(**kwargs)
            .fetch()
        ]
        return response_list

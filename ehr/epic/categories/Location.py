from ehr.epic.client import EpicFHIRClient


class Location(EpicFHIRClient):
    def __init__(self, customer_id, connection_id) -> None:
        super().__init__(customer_id, connection_id)
        
    def get_specific_location(self, ID):
        return self.client.reference("Location", ID).to_resource().serialize()

    def search_location(self, **kwargs):
        response_list = [
            response.serialize()
            for response in self.client.resources("Location").search(**kwargs).fetch()
        ]
        return response_list

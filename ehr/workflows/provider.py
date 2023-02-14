from rest_framework import status
from rest_framework.response import Response

from ehr.epic.transformers.provider import ProviderQueryTransformer 


class ProviderQuery:
    def __init__(self, data, ehr_id, customer_uuid, ehr_name, **kwargs):
        self.source_data = data
        self.ehr_name = ehr_name
        self.ehr_id = ehr_id
        self.customer_id = customer_uuid
        self.kwargs = kwargs

    def provider_query(self):

        provider_query = ProviderQueryTransformer(
            self.source_data, self.customer_id, self.ehr_id, **self.kwargs)

        try:
            provider_query = provider_query.transform()

            if type(provider_query) == Response:
                return provider_query

            return Response(provider_query)

        except Exception:
            return Response(
                {"Error": "Server time out"}, status=status.HTTP_504_GATEWAY_TIMEOUT
            )

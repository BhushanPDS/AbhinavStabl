from rest_framework import status
from ehr.epic.client import EpicFHIRClient
from rest_framework.response import Response

from ehr.remodels.redm.data_models.provider import ProviderQuery

from ehr.epic.categories.Administration import Practitioner


class ProviderQueryTransformer(EpicFHIRClient):
    def __init__(self, source_data, customer_id, ehrid, **kwargs):
        self.source_json = source_data
        self.customer_id = customer_id
        self.connection = ehrid
        self.destination_json = {}
        self.destination_response = {
            "Meta": {
                "DataModel": "Provider",
                "EventType": "ProviderQueryResponse",
                "Raw": [],
            },
        }

    def transform(self):
        try:
            ProviderQuery(**self.source_json)
            provider = Practitioner(self.customer_id, self.connection)

            provider.authenticate()

            for i in self.source_json.get("Provider")["Identifiers"]:
                if i['IDType'] == 'EHRID':
                    self.destination_json['ID'] = i['ID']

            provider_response = provider.get_specific_practitioner(
                **self.destination_json)

            if self.source_json.get("Meta").get("Test"):
                self.destination_response["Meta"]["Raw"].append(
                    provider_response)

            try:
                self.destination_response["Providers"] = [{
                    "Identifiers": [{}],
                    "IsActive": {},
                    "Demographics": {
                        "FirstName": {},
                        "LastName": {},
                        "Sex": {},
                        "Language": {},
                        "DOB": {},
                        "PhoneNumber": {
                            "Office": {},
                        },
                        "Addresses": [{
                            "StreetAddress": {},
                            "City": {},
                            "State": {},
                            "Country": {},
                            "ZIP": {}
                        }],
                        "EmailAddresses": [],
                    },
                    "Qualifications":[{
                        "Code": {},
                        "Codeset": {},
                        "StartDate": {},
                    }]
                }]
                self.destination_response['Providers'][0]['Identifiers'][0]['ID'] = provider_response.get(
                    'id')
                self.destination_response['Providers'][0]['IsActive'] = provider_response.get(
                    'active') if provider_response.get('active') else None
                self.destination_response['Providers'][0]['Demographics']['Sex'] = provider_response.get(
                    'gender') if provider_response.get('gender') else None
                self.destination_response['Providers'][0]['Demographics']['FirstName'] = provider_response.get(
                    'name')[0].get('given')[0] if provider_response.get('name')[0].get('given') else None
                self.destination_response['Providers'][0]['Demographics']['MiddleName'] = provider_response.get(
                    'name')[0].get('given')[1] if len(provider_response.get('name')[0].get('given')) > 1 else None
                self.destination_response['Providers'][0]['Demographics']['LastName'] = provider_response.get(
                    'name')[0].get('family') if provider_response.get('name')[0].get('family') else None
                self.destination_response['Providers'][0]['Demographics']['Addresses'][0]['StreetAddress'] = provider_response.get('address')[
                    0]['line'][0] if provider_response.get('address') else None
                self.destination_response['Providers'][0]['Demographics']['Addresses'][0]['City'] = provider_response.get('address')[
                    0]['city'] if provider_response.get('address') else None
                self.destination_response['Providers'][0]['Demographics']['Addresses'][0]['State'] = provider_response.get('address')[
                    0]['state'] if provider_response.get('address') else None
                self.destination_response['Providers'][0]['Demographics']['Addresses'][0]['ZIP'] = provider_response.get('address')[
                    0]['postalCode'] if provider_response.get('address') else None
                self.destination_response['Providers'][0]['Demographics']['Addresses'][0]['Country'] = provider_response.get('address')[
                    0]['country'] if provider_response.get('address') else None
                self.destination_response['Providers'][0]['Qualifications'][0]['Code'] = provider_response.get(
                    'qualification')[0]['code']['coding'][0]['display'] if provider_response.get('qualification') else None
                self.destination_response['Providers'][0]['Qualifications'][0]['Codeset'] = provider_response.get(
                    'qualification')[0]['code']['coding'][0]['system'] if provider_response.get('qualification') else None

                return self.destination_response

            except Exception:
                return provider_response

        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

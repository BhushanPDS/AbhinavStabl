from copy import deepcopy
from ehr.epic.client import EpicFHIRClient
from rest_framework import status
from rest_framework.response import Response

from ehr.epic.categories.Administration import Patient
from ehr.epic.categories.Administration import List
from ehr.epic.categories.Clinic import AllergyIntolerance
from ehr.epic.categories.Financial import Coverage
from ehr.epic.categories.Clinic import Procedure

from ehr.remodels.redm.data_models.clinical_summary import PatientQuery


class PatientQueryTransformer(EpicFHIRClient):
    def __init__(self, source_data, customer_id, ehrid, **kwargs):
        self.source_json = source_data
        self.customer_id = customer_id
        self.connection = ehrid
        self.destination_json = {}
        self.destination_response = {
            "Meta": {
                "DataModel": "Clinical Summary",
                "EventType": "PatientQueryResponse",
                "Source": {"ID": self.customer_id, "Name": kwargs.get("name")},
                "Raw": [],
            },
        }

    def transform(self, event):
        try:

            PatientQuery(**self.source_json)
            for events in event:
                if events not in ('demographics', 'insurances', 'allergies', 'medications', 'procedure', 'all'):
                    return Response({f'Error': "Invalid event: {event}"}, status=status.HTTP_400_BAD_REQUEST)

            if events == 'demographics':
                patient = Patient(self.customer_id, self.connection)
                patient.authenticate()

                for i in self.source_json.get("Patient")["Identifiers"]:
                    if i['IDType'] == 'EHRID':
                        self.destination_json['ID'] = i['ID']

                # Demographic Data
                query_response = patient.get_specific_patient(
                    self.destination_json['ID']
                )
                try:
                    self.destination_response['Header'] = {
                        "Patient": {"Identifiers": [], "Demographics": {}}}

                    self.destination_response['Header']['Patient']['Identifiers'].append(
                        {"ID": query_response.get('id'), "IDType": "EHRID"})

                    self.destination_response['Header']['Patient']['Demographics']['FirstName'] = query_response.get(
                        'name')[0].get('given')[0] if query_response.get('name')[0].get('given') else None
                    self.destination_response['Header']['Patient']['Demographics']['MiddleName'] = query_response.get(
                        'name')[0].get('given')[1] if len(query_response.get('name')[0].get('given')) > 1 else None
                    self.destination_response['Header']['Patient']['Demographics']['LastName'] = query_response.get(
                        'name')[0].get('family') if query_response.get('name')[0].get('family') else None
                    self.destination_response['Header']['Patient']['Demographics']['Sex'] = query_response.get(
                        'gender') if query_response.get('gender') else None
                    self.destination_response['Header']['Patient']['Demographics']['language'] = query_response.get(
                        'communication')[0]['language'].get('text') if query_response.get('communication') else None
                    self.destination_response['Header']['Patient']['Demographics']['DOB'] = query_response.get(
                        'birthDate') if query_response.get('birthDate') else None
                    self.destination_response['Header']['Patient']['Demographics']['MaritalStatus'] = query_response.get(
                        'maritalStatus').get('text') if query_response.get('maritalStatus') else None
                    if query_response.get('address'):
                        self.destination_response['Header']['Patient']['Demographics']['Address'] = {
                        }
                        self.destination_response['Header']['Patient']['Demographics']['Address']['StreetAddress'] = query_response.get(
                            'address')[0]['line'][0] if query_response.get('address')[0].get('line') else None
                        self.destination_response['Header']['Patient']['Demographics']['Address']['City'] = query_response.get(
                            'address')[0].get('city') if query_response.get('address')[0].get('city') else None
                        self.destination_response['Header']['Patient']['Demographics']['Address']['Country'] = query_response.get(
                            'address')[0].get('country') if query_response.get('address')[0].get('country') else None
                        self.destination_response['Header']['Patient']['Demographics']['Address']['State'] = query_response.get(
                            'address')[0].get('state') if query_response.get('address')[0].get('state') else None
                        self.destination_response['Header']['Patient']['Demographics']['Address']['ZIP'] = query_response.get(
                            'address')[0].get('postalCode') if query_response.get('address')[0].get('postalCode') else None
                    if query_response.get('telecom'):
                        self.destination_response['Header']['Patient']['Demographics']['PhoneNumber'] = {
                        }
                        for phone in query_response.get('telecom'):
                            self.destination_response['Header']['Patient']['Demographics']['PhoneNumber'].update(
                                {phone.get('use').capitalize() if phone.get('use') else "Mobile": phone.get('value')})

                    if self.source_json["Meta"].get("Test"):
                        self.destination_response["Meta"]["Raw"].append(
                            query_response)
                    return self.destination_response

                except Exception:
                    return query_response

            if events == 'allergies':
                for i in self.source_json.get("Patient")["Identifiers"]:
                    if i['IDType'] == 'EHRID':
                        self.destination_json['patient'] = i['ID']

                allergies = AllergyIntolerance(
                    self.customer_id, self.connection)
                allergies.authenticate()
                query_response = allergies.search_allergy_intolerance(
                    **self.destination_json)
                try:
                    self.destination_response["Header"] = {
                        "Patient": {"Identifiers": []}}
                    self.destination_response['Header']['Patient']['Identifiers'].append({'ID': query_response.get(
                        'entry')[0].get('resource').get('patient').get('reference').split('/')[1]})
                    self.destination_response['Allergies'] = []
                    for allergies in query_response.get('entry'):
                        allergy = {
                            'Substance': {},
                            'Reaction': {},
                            'Criticality': {},
                            'Status': {},
                        }

                        allergy['Substance']['Code'] = allergies.get('resource').get('code').get(
                            'coding')[0].get('code') if allergies.get('resource').get('code') else None
                        allergy['Substance']['CodeSystem'] = allergies.get('resource').get('code').get(
                            'coding')[0].get('system') if allergies.get('resource').get('code') else None
                        allergy['Substance']['CodeSystemName'] = None
                        allergy['Substance']['Name'] = allergies.get('resource').get('code').get(
                            'coding')[0].get('display') if allergies.get('resource').get('code') else None
                        allergy['Substance']['AltCodes'] = [{"Code": codes.get("code"), "CodeSystem": codes.get("system")}for codes in allergies.get('resource').get('code').get(
                            'coding')[1:]]

                        allergy['Reaction']['Code'] = allergies.get('resource').get('reaction')[0].get('manifestation')[
                            0].get('coding')[0].get('code') if allergies.get('resource').get('reaction') else None
                        allergy['Reaction']['CodeSystem'] = allergies.get('resource').get('reaction')[0].get(
                            'manifestation')[0].get('coding')[0].get('system') if allergies.get('resource').get('reaction') else None
                        allergy['Reaction']['CodeSystemName'] = None
                        allergy['Reaction']['Name'] = allergies.get('resource').get('reaction')[0].get('manifestation')[
                            0].get('coding')[0].get('display') if allergies.get('resource').get('reaction') else None
                        allergy['Reaction']['AltCodes'] = []

                        allergy['Criticality']['Name'] = allergies.get('resource').get(
                            'criticality') if allergies.get('resource').get('criticality') else None
                        allergy['Criticality']['AltCodes'] = []

                        allergy['Status']['Code'] = allergies.get('resource').get('clinicalStatus').get(
                            'coding')[0].get('code') if allergies.get('resource').get('clinicalStatus') else None
                        allergy['Status']['CodeSystem'] = allergies.get('resource').get('clinicalStatus').get(
                            'coding')[0].get('system') if allergies.get('resource').get('clinicalStatus') else None
                        allergy['Status']['CodeSystemName'] = None
                        allergy['Status']['Name'] = allergies.get('resource').get('clinicalStatus').get(
                            'coding')[0].get('display') if allergies.get('resource').get('clinicalStatus') else None
                        allergy['Status']['AltCodes'] = []

                        allergy['StartDate'] = allergies.get('resource').get(
                            'recordedDate') if allergies.get('resource').get('recordedDate') else None

                        self.destination_response['Allergies'].append(
                            allergy)

                    if self.source_json["Meta"].get("Test"):
                        self.destination_response["Meta"]["Raw"].append(
                            query_response)

                    return self.destination_response
                except:
                    return query_response

            if events == 'medications':
                for i in self.source_json.get("Patient")["Identifiers"]:
                    if i['IDType'] == 'EHRID':
                        self.destination_json['patient'] = i['ID']
                # medications
                self.destination_json['code'] = 'medications'
                list = List(
                    self.customer_id, self.connection)
                list.authenticate()
                query_response = list.search_medication(
                    **self.destination_json)
                try:
                    self.destination_response['Header'] = {
                        "Patient": {"Identifiers": []}}
                    self.destination_response['Medications'] = []
                    self.destination_response['Header']['Patient']['Identifiers'].append(
                        {"ID": query_response.get('entry')[0].get('resource').get(
                            'subject').get('reference').split('/')[1], "IDType": "EHRID"}
                    )
                    for medication in query_response.get('entry'):
                        medications = {"Product": {},
                                       "Route": {}, "Dose": {}}
                        medications['Status'] = medication.get(
                            'resource').get('status')
                        if medication.get('resource').get('code').get('coding'):
                            medications['Product']['CodeSystem'] = medication.get(
                                'resource').get('code').get('coding')[0].get('system')
                            medications['Product']['Code'] = medication.get(
                                'resource').get('code').get('coding')[0].get('code')
                            medications['Product']['CodeSystemName'] = medication.get(
                                'resource').get('code').get('coding')[0].get('display')
                        medications['Product']['Name'] = medication.get(
                            'resource').get('code').get('text')
                        if medication.get('resource').get('dosage'):
                            medications['Route']['CodeSystem'] = medication.get(
                                'resource').get('dosage').get('route').get('coding')[0].get('system')
                            medications['Route']['CodeSystemName'] = medication.get(
                                'resource').get('dosage').get('route').get('coding')[0].get('display')
                            medications['Route']['Name'] = medication.get(
                                'resource').get('dosage').get('route').get('text')
                            medications['Dose']['Quntity'] = medication.get(
                                'resource').get('dosage').get('dose').get('value')
                        self.destination_response['Medications'].append(
                            medications)

                    if self.source_json["Meta"].get("Test"):
                        self.destination_response["Meta"]["Raw"].append(
                            query_response)

                    return self.destination_response
                except:
                    return query_response

            if events == 'insurances':
                for i in self.source_json.get("Patient")["Identifiers"]:
                    if i['IDType'] == 'EHRID':
                        self.destination_json['patient'] = i['ID']
                coverage = Coverage(self.customer_id, self.connection)
                coverage.authenticate()
                query_response = coverage.search_insurance(
                    **self.destination_json)

                if self.source_json["Meta"].get("Test"):
                    self.destination_response["Meta"]["Raw"].append(
                        query_response)

                try:
                    self.destination_response["Header"] = {
                        "Patient": {"Identifiers": [{}]}}
                    self.destination_response['Header']['Patient']['Identifiers'][0]["ID"] = query_response.get('entry')[0].get(
                        'resource').get('beneficiary').get('reference').split('/')[1]

                    self.destination_response["Insurances"] = []
                    for insurances in query_response.get('entry'):

                        insurance = {
                            "Plan": {},
                            "Company": {},
                            "Insured": {
                                "Identifiers": []
                            }

                        }
                        insurance['Plan']['ID'] = insurances.get(
                            "resource").get("id")
                        insurance['Company']['ID'] = insurances.get('resource').get('payor')[
                            0].get("reference").split('/')[1]
                        insurance['Company']['Name'] = insurances.get(
                            "resource").get('payor')[0].get('display')
                        insurance['EffectiveDate'] = insurances.get(
                            'resource').get('period').get('start')

                        insurance['Insured']['Identifiers'].append({"ID": insurances.get(
                            'resource').get('beneficiary').get('reference').split('/')[1]})
                        insurance['Insured']['LastName'], insurance['Insured']['FirstName'] = insurances.get(
                            'resource').get('beneficiary').get("display").split(',')
                        if insurances.get('resource').get('relationship'):
                            insurance['Insured']['Relationship'] = insurances.get(
                                'resource').get('relationship').get('text')

                        insurance['MemberNumber'] = insurances.get(
                            'resource').get('subscriberId')
                        if insurances.get('resource').get('class'):
                            insurance['Plan']['Name'] = insurances.get(
                                'resource').get('class')[0].get('name')
                            insurance['Plan']['ID'] = insurances.get(
                                'resource').get('class')[0].get('value')

                        self.destination_response['Insurances'].append(
                            insurance)

                    return self.destination_response

                except:
                    return query_response

            if events == 'procedure':
                for i in self.source_json.get("Patient")["Identifiers"]:
                    if i['IDType'] == 'EHRID':
                        self.destination_json['patient'] = i['ID']

                procedure = Procedure(self.customer_id, self.connection)
                procedure.authenticate()
                query_response = procedure.search_patient_procedure(
                    **self.destination_json)

                if self.source_json["Meta"].get("Test"):
                    self.destination_response["Meta"]["Raw"].append(
                        query_response)

                try:
                    self.destination_response["Header"] = {
                        "Patient": {"Identifiers": [{}]}}
                    self.destination_response['Header']['Patient']['Identifiers'][0]["ID"] = query_response.get('entry')[0].get(
                        'resource').get('subject').get('reference').split('/')[1]

                    self.destination_response["Procedures"] = []
                    for response in query_response.get('entry'):
                        procedure = {
                            "Code": {},
                            "CodeSystem": {},
                            "CodeSystemName": {},
                            "Name": {},
                            "AltCodes": []
                        }
                        procedure['Code'] = response.get('resource').get(
                            'category').get('coding')[0].get('code')
                        procedure['CodeSystem'] = response.get('resource').get(
                            'category').get('coding')[0].get('system')
                        procedure['CodeSystemName'] = response.get('resource').get(
                            'category').get('coding')[0].get('display')
                        procedure['CodeSystemName'] = response.get('resource').get(
                            'category').get('coding')[0].get('display')
                        self.destination_response['Procedures'].append(
                            procedure)
                    return self.destination_response

                except:
                    return query_response

        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

import unittest, json

from ehr.remodels.redm.data_models.clinical_summary import PatientQuery

valid_json = '{"Meta":{"DataModel":"Clinical Summary","EventType":"PatientQuery","EventDateTime":"2022-06-28T14:45:32.013Z","Test":true,"Destinations":[{"ID":"ef9e7448-7f65-4432-aa96-059647e9b357","Name":"Patient Query Endpoint"}],"Logs":[{"ID":"d9f5d293-7110-461e-a875-3beb089e79f3","AttemptID":"925d1617-2fe0-468c-a14c-f8c04b572c54"}],"FacilityCode":""},"Patient":{"Identifiers":[{"ID":"0000000001","IDType":"MR"},{"ID":"e167267c-16c9-4fe3-96ae-9cff5703e90a","IDType":"EHRID"},{"ID":"a1d4ee8aba494ca","IDType":"NIST"}]},"Location":{"Department":""}}'
invalid_json = '{"Meta":{"DataModel":"Clinical Summary","EventType":"PatientQuery","EventDateTime":"2022-06-28T14:45:32.013Z","Test":true,"Destinations":[{"ID":"ef9e7448-7f65-4432-aa96-059647e9b357","Name":"Patient Query Endpoint"}],"Logs":[{"ID":"d9f5d293-7110-461e-a875-3beb089e79f3","AttemptID":"925d1617-2fe0-468c-a14c-f8c04b572c54"}],"FacilityCode":""},"Patient":{"Identifiers":[{"ID":"0000000001","IDType":"MR"},{"ID":"e167267c-16c9-4fe3-96ae-9cff5703e90a","IDType":"EHRID"},{"ID":"a1d4ee8aba494ca","IDType":"NIST"}]},"Location":{"Department":""}}'

class PatientQueryTestCase(unittest.TestCase):
    def test_with_valid_payload(self):
        payload = json.loads(valid_json)
        patient_query = PatientQuery(**payload)
        self.assertEqual(patient_query.Meta.DataModel, 'Clinical Summary')
        self.assertEqual(patient_query.Meta.EventType, 'PatientQuery')
        self.assertEqual(patient_query.Meta.Test, True)
        self.assertEqual(patient_query.Meta.Destinations[0].ID, 'ef9e7448-7f65-4432-aa96-059647e9b357')
        self.assertEqual(patient_query.Meta.Destinations[0].Name, 'Patient Query Endpoint')
        self.assertEqual(patient_query.Meta.Logs[0].ID, 'd9f5d293-7110-461e-a875-3beb089e79f3')
        self.assertEqual(patient_query.Meta.Logs[0].AttemptID, '925d1617-2fe0-468c-a14c-f8c04b572c54')
        self.assertEqual(patient_query.Meta.FacilityCode, '')
        self.assertEqual(patient_query.Patient.Identifiers[0].ID, '0000000001')
        self.assertEqual(patient_query.Patient.Identifiers[0].IDType, 'MR')
        self.assertEqual(patient_query.Patient.Identifiers[1].ID, 'e167267c-16c9-4fe3-96ae-9cff5703e90a')
        self.assertEqual(patient_query.Patient.Identifiers[1].IDType, 'EHRID')
        self.assertEqual(patient_query.Patient.Identifiers[2].ID, 'a1d4ee8aba494ca')
        self.assertEqual(patient_query.Patient.Identifiers[2].IDType, 'NIST')
        self.assertEqual(patient_query.Location.Department, '')

    def test_with_invalid_payload(self):
        pass


if __name__ == '__main__':
    unittest.main()
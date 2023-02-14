from ehr.epic.transformers.clinical_summary import (
    PatientQueryTransformer as EpicPatientQuery,

)

from rest_framework import status
from rest_framework.response import Response


class PatientQuery:
    def __init__(self, data, ehr_id, customer_uuid, ehr_name, **kwargs):
        self.source_data = data
        self.ehr_name = ehr_name
        self.ehr_id = ehr_id
        self.customer_id = customer_uuid
        self.kwargs = kwargs

    def patient_query(self, event):

        patient_query = EpicPatientQuery(
            self.source_data, self.customer_id, self.ehr_id, **self.kwargs)

        try:
            patient_query = patient_query.transform(event)

            if type(patient_query) == Response:
                return patient_query

            return Response(patient_query)

        except Exception:
            return Response(
                {"Error": "Server time out"}, status=status.HTTP_504_GATEWAY_TIMEOUT
            )

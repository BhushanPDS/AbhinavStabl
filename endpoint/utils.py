from core.models import Customer
from core.models import Patient as PatientModel
from core.models import Provider as ProviderModel


def get_connection(request):
    name_type = request.get("Meta").get("Source").get("Name").lower()
    id_type = request["Meta"]["Source"].get("ID")
    if name_type == "customerid":
        customer_id = id_type
        customer_obj = Customer.objects.filter(uuid=customer_id).first()
        
        if customer_obj is None or customer_obj.connection is None:
            return None, None, None, None

        customer_connection = customer_obj.connection.get(app_type="system")
        return (
            customer_id,
            customer_connection.uuid,
            customer_connection.ehr_name,
            customer_obj.name,
        )
    elif name_type == "providerid":
        provider_id = id_type
        provider_obj = ProviderModel.objects.filter(uuid=provider_id).first()
        
        if provider_obj is None or provider_obj.customer.connection is None:
            return None, None, None, None
        
        customer_obj = provider_obj.customer

        customer_connection = customer_obj.connection.get(app_type="provider")
        return (
            provider_id,
            customer_connection.uuid,
            customer_connection.ehr_name,
            f"{provider_obj.firstname} {provider_obj.lastname}",
        )

    elif name_type == "patientid":
        patient_id = id_type
        patient_obj = PatientModel.objects.get(uuid=patient_id)
        if patient_obj is None or patient_obj.customer.connection is None:
            return None, None, None, None
        
        customer_obj = patient_obj.customer

        customer_connection = customer_obj.connection.get(app_type="patient")
        return (
            patient_id,
            customer_connection.uuid,
            customer_connection.ehr_name,
            patient_obj.firstname,
        )
    return (
        [
            False,
            "Source name should be (CustomerID, ProviderID, PatientID)",
        ],
        None,
        None,
        None,
    )

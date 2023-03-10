from enum import Enum

class DataModels(str, Enum):
    """
    Enum for the data models
    """
    CLAIM = "Claim"
    CLINICAL_DECISIONS = "Clinical Decisions"
    CLINICAL_SUMMARY = "Clinical Summary"
    DEVICE = "Device"
    FINANCIAL = "Financial"
    FLOWSHEET = "Flowsheet"
    INVENTORY = "Inventory"
    MEDIA = "Media"
    MEDICATIONS = "Medications"
    NOTES = "Notes"
    ORDER = "Order"
    ORGANIZATION = "Organization"
    PATIENT_ADMIN = "PatientAdmin"
    PATIENT_EDUCATION = "PatientEducation"
    PATIENT_SEARCH = "PatientSearch"
    PROVIDER = "Provider"
    REFERRAL = "Referral"
    RESEARCH = "Research"
    RESULTS = "Results"
    SCHEDULING = "Scheduling"
    SSO = "SSO"
    SURGICAL_SCHEDULING = "SurgicalScheduling"
    VACCINATION = "Vaccination"
    DEPARTMENT = "Department"


class EventTypes(str, Enum):
    """
    Enum for the event types
    """
    NEW = "New"
    QUERY_RESPONSE = "QueryResponse"
    QUERY = "Query"
    UPDATE = "Update"
    STUDY = "Study"
    SUBJECT_UPDATE = "SubjectUpdate"
    RESCHEDULE = "Reschedule"
    MODIFICATION = "Modification"
    CANCEL = "Cancel"
    GROUPED_ORDERS = "GroupedOrders"
    AUTH_RESPONSE = "AuthResponse"
    MODIFY = "Modify"
    AUTH_REVIEW = "AuthReview"
    ADMINISTRATION = "Administration"
    TRANSACTION = "Transaction"
    ACCOUNT_UPDATE = "AccountUpdate"
    AVAILABLE_SLOTS = "AvailableSlots"
    AVAILABLE_SLOTS_RESPONSE = "AvailableSlotsResponse"
    PUSH_SLOTS = "PushSlots"
    BOOKED_RESPONSE = "BookedResponse"
    BOOKED = "Booked"
    PROVIDER_QUERY = "ProviderQuery"
    ACTIVATE = "Activate"
    DEACTIVATE = "Deactivate"
    PROVIDER_QUERY_RESPONSE = "ProviderQueryResponse"
    NEW_UNSOLICITED = "NewUnsolicited"
    LOCATION_QUERY_RESPONSE = "LocationQueryResponse"
    LOCATION_QUERY = "LocationQuery"
    RESPONSE = "Response"
    DOCUMENT_QUERY_RESPONSE = "DocumentQueryResponse"
    VISIT_PUSH = "VisitPush"
    DOCUMENT_GET = "DocumentGet"
    PATIENT_PUSH = "PatientPush"
    PATIENT_QUERY = "PatientQuery"
    DOCUMENT_QUERY = "DocumentQuery"
    VISIT_QUERY_RESPONSE = "VisitQueryResponse"
    PATIENT_QUERY_RESPONSE = "PatientQueryResponse"
    VISIT_QUERY = "VisitQuery"
    DOCUMENT_GET_RESPONSE = "DocumentGetResponse"
    SIGN_ON = "Sign-on"
    REPLACE = "Replace"
    CENSUS_QUERY = "CensusQuery"
    VISIT_UPDATE = "VisitUpdate"
    PATIENT_MERGE = "PatientMerge"
    TRANSFER = "Transfer"
    ARRIVAL = "Arrival"
    REGISTRATION = "Registration"
    VISIT_MERGE = "VisitMerge"
    DISCHARGE = "Discharge"
    NEW_PATIENT = "NewPatient"
    PREADMIT = "PreAdmit"
    PATIENT_UPDATE = "PatientUpdate"
    CENSUS_QUERY_RESPONSE = "CensusQueryResponse"
    DEPLETE = "Deplete"
    REQUEST = "Request"
    SUBMISSION_BATCH = "SubmissionBatch"
    PAYMENT = "Payment"
    SUBMISSION = "Submission"
    PAYMENT_BATCH = "PaymentBatch"
    DELETE = "Delete"
    NOSHOW = "NoShow"

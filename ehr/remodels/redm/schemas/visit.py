from datetime import datetime, date
from typing import List,Optional
from ehr.remodels.redm.core.models import Model
from ehr.remodels.redm.schemas.location import Location
from ehr.remodels.redm.schemas.demographics import Demographics
from ehr.remodels.redm.schemas.address import Address
from ehr.remodels.redm.schemas.phonenumber import PhoneNumber
from ehr.remodels.redm.schemas.insurances import Insurance
from ehr.remodels.redm.schemas.diagnosis import Diagnosis
from ehr.remodels.redm.schemas.procedure import Procedures
from ehr.remodels.redm.schemas.provider import AttendingProvider
from ehr.remodels.redm.schemas.provider import ReferringProvider
from ehr.remodels.redm.schemas.provider import ConsultingProvider
from ehr.remodels.redm.schemas.location import PreviousLocation
from ehr.remodels.redm.schemas.type_code import TypeCode
from ehr.remodels.redm.schemas.provider import Provider
from ehr.remodels.redm.schemas.type_code import TypeCodeSet
from ehr.remodels.redm.schemas.provider import AdmittingProvider
from ehr.remodels.redm.schemas.location import DischargeLocation
from ehr.remodels.redm.schemas.provider import VisitProvider
# from ehr.remodels.redm.schemas.patient import Patient

class Employer(Model):
    Name: Optional[str]
    Address: Optional[Address]
    PhoneNumbers: Optional[PhoneNumber]


class Spouse(Model):
    FirstName: Optional[str]
    LastName: Optional[str]


class Guarantor(Demographics):
    Number: Optional[str]
    Address: Optional[Address]
    PhoneNumber: Optional[PhoneNumber]
    EmailAddresses: Optional[List[str]]
    Type: Optional[str]
    RelationToPatient: Optional[str]
    Employer: Optional[Employer]
    Spouse: Optional[Spouse]

class Equipment(TypeCodeSet):
    StartDateTime: Optional[datetime]
    Duration: Optional[int] = None

class VisitPreference(Model):
    Duration: Optional[int] = None
    DurationUnit: Optional[str]
    Day: Optional[List[str]]
    Time: Optional[List[str]]

class Visit(Model):
    ID: Optional[str]
    VisitNumber: str = None
    StartDateTime: Optional[datetime]
    EndDateTime: Optional[datetime]
    Location: Optional[Location]
    DateTime: Optional[date]
    DischargeDateTime: Optional[datetime]
    PreviousLocation: Optional[PreviousLocation]
    Type: Optional[str]
    AccountNumber: Optional[str]
    VisitDateTime: Optional[datetime]
    Guarantor: Optional[Guarantor]
    Insurances: Optional[List[Insurance]]
    PatientClass: Optional[str]
    AttendingProvider: Optional[AttendingProvider]
    ReferringProvider: Optional[ReferringProvider]
    ConsultingProvider: Optional[ConsultingProvider]
    Diagnoses: Optional[List[Diagnosis]]
    DiagnosisRelatedGroup: Optional[int] = None
    DiagnosisRelatedGroupType: Optional[int] = None
    Balance: Optional[int] = None
    Procedures: Optional[List[Procedures]]
    Reason: Optional[str]
    Type: Optional[TypeCode]
    DischargeDisposition: Optional[TypeCode]
    AdditionalStaff: Optional[List[Provider]]
    DischargeStatus: Optional[TypeCodeSet]
    Duration: Optional[int] = None
    Instructions: Optional[List[str]]
    AdmittingProvider: Optional[AdmittingProvider]
    DischargeLocation: Optional[DischargeLocation]
    VisitProvider: Optional[VisitProvider]
    Equipment: Optional[List[Equipment]]
    OldDateTime: Optional[datetime]
    Status: Optional[str]
    VisitType: Optional[TypeCodeSet]
    VisitPreference: Optional[List[VisitPreference]]
    Patients: Optional[List['schemas.Patient']]
    CancelReason: Optional[str]
    LastUpdated: Optional[datetime]
    ScheduledDateTime: Optional[datetime]
    CancelDateTime: Optional[datetime]
    AppointmentInfo: Optional[List[TypeCode]]
    Notes: Optional[List[str]]



    


    






    






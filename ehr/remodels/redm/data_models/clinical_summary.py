from typing import Optional, List
from ehr.remodels.redm.schemas.diagnosis import AdmissionDiagnosis, DischargeDiagnosis
from ehr.remodels.redm.schemas.document import Document
from ehr.remodels.redm.schemas.medications import MedicationsAdministered
from ehr.remodels.redm.schemas.reason_for_visit import ReasonForVisit
from ehr.remodels.redm.core.models import DataModelBase as Model 
from ehr.remodels.redm.schemas.location import Location
from ehr.remodels.redm.schemas.patient import Patient
from ehr.remodels.redm.schemas.header import Header
from ehr.remodels.redm.schemas.advance_directives import AdvanceDirectives
from ehr.remodels.redm.schemas.allergy import Allergies
from ehr.remodels.redm.schemas.encounters import Encounters
from ehr.remodels.redm.schemas.family_history import FamilyHistory
from ehr.remodels.redm.schemas.functional_status import FunctionalStatus
from ehr.remodels.redm.schemas.goals import Goals
from ehr.remodels.redm.schemas.health_concerns import HealthConcerns
from ehr.remodels.redm.schemas.immunizations import Immunizations
from ehr.remodels.redm.schemas.insurances import Insurances
from ehr.remodels.redm.schemas.medical_equipment import MedicalEquipment
from ehr.remodels.redm.schemas.medications import Medications
from ehr.remodels.redm.schemas.plan_of_care import PlanOfCare
from ehr.remodels.redm.schemas.problems import Problems
from ehr.remodels.redm.schemas.procedure import Procedures
from ehr.remodels.redm.schemas.results import Results
from ehr.remodels.redm.schemas.social_history import SocialHistory
from ehr.remodels.redm.schemas.vital_signs import VitalSigns
from ehr.remodels.redm.schemas.visit import Visit
from ehr.remodels.redm.schemas.assessment import Assessment
from ehr.remodels.redm.schemas.chief_complaint import ChiefComplaint
from ehr.remodels.redm.schemas.discharge_medications import DischargeMedications
from ehr.remodels.redm.schemas.history import HistoryOfPresentIllness
from ehr.remodels.redm.schemas.interventions import Interventions
from ehr.remodels.redm.schemas.objective import Objective
from ehr.remodels.redm.schemas.physical_exam import PhysicalExam
from ehr.remodels.redm.schemas.reason_for_referral import ReasonForReferral
from ehr.remodels.redm.schemas.review_of_systems import ReviewOfSystems
from ehr.remodels.redm.schemas.subjective import Subjective
from ehr.remodels.redm.schemas.careteams import CareTeams
from ehr.remodels.redm.schemas.resolvedproblem import ResolvedProblems
from ehr.remodels.redm.schemas.medical_equipment import MedicalHistory
from ehr.remodels.redm.schemas.note import NoteSection
from ehr.remodels.redm.schemas.instructions import Instructions

class PatientQuery(Model): 
    Patient: Patient
    Location: Optional[Location]

class PatientQueryResponse(Model): 
    Header: Optional[Header]
    AdvanceDirectives: Optional[AdvanceDirectives]
    Allergies: Optional[Allergies] 
    CareTeams: Optional[CareTeams]
    Encounters: Optional[Encounters] 
    FamilyHistory: Optional[FamilyHistory]
    FunctionalStatus: Optional[FunctionalStatus]
    Goals: Optional[Goals]
    HealthConcerns: Optional[HealthConcerns]
    Immunizations: Optional[Immunizations]
    Insurances: Optional[Insurances]
    MedicalEquipment: Optional[MedicalEquipment]
    Medications: Optional[Medications]
    PlanOfCare: Optional[PlanOfCare]
    Problems: Optional[Problems]
    Procedures: Optional[Procedures]
    ResolvedProblems: Optional[ResolvedProblems]
    Results: Optional[Results]
    SocialHistory: Optional[SocialHistory]
    VitalSigns: Optional[VitalSigns]

class PatientPush(Model):
    Header: Optional[Header]
    AdvanceDirectives: Optional[List[AdvanceDirectives]]
    Allergies: Optional[List[Allergies]]
    CareTeams: Optional[CareTeams]
    Encounters: Optional[List[Encounters]]
    FamilyHistory: Optional[FamilyHistory]
    FunctionalStatus: Optional[FunctionalStatus]
    Gaols: Optional[Goals]
    HealthConcerns: Optional[List[HealthConcerns]]
    Immunizations: Optional[List[Immunizations]]
    Insurances: Optional[List[Insurances]]
    MedicalHistory: Optional[List[MedicalHistory]]
    MedicalEquipment: Optional[List[MedicalEquipment]]
    Medications: Optional[List[Medications]]
    NoteSections: Optional[List[NoteSection]]
    PlanOfCare: Optional[PlanOfCare]
    Problems: Optional[List[Problems]]
    Procedures: Optional[Procedures]
    ResolvedProblems: Optional[List[ResolvedProblems]]
    Results: Optional[List[Results]]
    SocialHistory: Optional[SocialHistory]
    VitalSigns: Optional[VitalSigns]

class VisitQuery(Model):
    Patient: Optional[Patient]
    Visit: Optional[Visit]

class VisitQueryResponse(Model):
    Header: Optional[Header]
    AdmissionDiagnosis: Optional[AdmissionDiagnosis]
    AdvanceDirectives: Optional[List[AdvanceDirectives]]
    Allergies: Optional[List[Allergies]]
    Assessment: Optional[Assessment]
    CareTeams: Optional[CareTeams]
    ChiefComplaint: Optional[ChiefComplaint]
    DischargeDiagnosis: Optional[DischargeDiagnosis]
    DischargeMedications: Optional[DischargeMedications]
    Encounters: Optional[List[Encounters]]
    FamilyHistory: Optional[FamilyHistory]
    FunctionalStatus: Optional[FunctionalStatus]
    Goals: Optional[List[Goals]]
    HealthConcerns: Optional[List[HealthConcerns]]
    HistoryOfPresentIllness: Optional[HistoryOfPresentIllness]
    Immunizations: Optional[List[Immunizations]]
    Instructions: Optional[Instructions]
    Insurances: Optional[List[Insurances]]
    Interventions: Optional[Interventions]
    MedicalEquipment: Optional[List[MedicalEquipment]]
    Medications: Optional[List[Medications]]
    MedicationsAdministered: Optional[List[MedicationsAdministered]]
    Objective: Optional[Objective]
    PhysicalExam: Optional[PhysicalExam]
    PlanOfCare: Optional[PlanOfCare]
    Problems: Optional[List[Problems]]
    Procedures: Optional[Procedures]
    ResolvedProblems: Optional[List[ResolvedProblems]]
    ReasonForReferral: Optional[ReasonForReferral]
    ReasonForVisit: Optional[List[ReasonForVisit]]
    Results: Optional[List[Results]]
    ReviewOfSystems: Optional[ReviewOfSystems]
    SocialHistory: Optional[SocialHistory]
    Subjective: Optional[Subjective]
    VitalSigns: Optional[VitalSigns]

class VisitPush(Model):
    Header: Optional[Header]
    AdmissionDiagnosis: Optional[AdmissionDiagnosis]
    AdvanceDirectives: Optional[List[AdvanceDirectives]]
    Allergies: Optional[List[Allergies]]
    Assessment: Optional[Assessment]
    ChiefComplaint: Optional[ChiefComplaint]
    DischargeDiagnosis: Optional[DischargeDiagnosis]
    DischargeMedications: Optional[DischargeMedications]
    Encounters: Optional[List[Encounters]]
    FamilyHistory: Optional[FamilyHistory]
    FunctionalStatus: Optional[FunctionalStatus]
    Goals: Optional[List[Goals]]
    HealthConcerns: Optional[List[HealthConcerns]]
    HistoryOfPresentIllness: Optional[HistoryOfPresentIllness]
    Immunizations: Optional[List[Immunizations]]
    Instructions: Optional[Instructions]
    Insurances: Optional[List[Insurances]]
    Interventions: Optional[Interventions]
    MedicalEquipment: Optional[List[MedicalEquipment]]
    MedicalHistory: Optional[MedicalHistory]
    Medications: Optional[List[Medications]]
    MedicationsAdministered: Optional[List[MedicationsAdministered]]
    NoteSections: Optional[List[NoteSection]]
    Objective: Optional[Objective]
    PhysicalExam: Optional[PhysicalExam]
    PlanOfCare: Optional[PlanOfCare]
    Problems: Optional[List[Problems]]
    Procedures: Optional[Procedures]
    ReasonForReferral: Optional[ReasonForReferral]
    ReasonForVisit: Optional[List[ReasonForVisit]]
    ResolvedProblems: Optional[List[ResolvedProblems]]
    Results: Optional[List[Results]]
    ReviewOfSystems: Optional[ReviewOfSystems]
    SocialHistory: Optional[SocialHistory]
    Subjective: Optional[Subjective]
    VitalSigns: Optional[VitalSigns]


class DocumentQuery(Model):
    Patient: Optional[Patient]
    Location: Optional[Location]
    Visit: Optional[Visit]
    Document: Optional[Document]

class DocumentQueryResponse(Model):
    Patient: Optional[Patient]
    Documents: Optional[List[Document]]

class DocumentGet(Model):
    Document: Optional[Document]

class DocumentGetResponse(Model):
    Document: Optional[Document]
    FileType: str = None
    Data: str = None

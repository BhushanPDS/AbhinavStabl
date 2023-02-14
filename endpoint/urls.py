from django.urls import path
from . import views

urlpatterns = [
    path('clinical-summary/patient-query/demographics',
         views.clinical_summary_patient_query_demographics, name='patient-query-demographics'),
    path('clinical-summary/patient-query/insurances',
         views.clinical_summary_patient_query_insurances, name='patient-query-insurances'),
    path('clinical-summary/patient-query/allergies',
         views.clinical_summary_patient_query_allergies, name='patient-query-allergies'),
    path('clinical-summary/patient-query/medications',
         views.clinical_summary_patient_query_medications, name='patient-query-medications'),
     path('clinical-summary/patient-query/procedure',
         views.clinical_summary_patient_query_procedure, name='patient-query-procedure'),
    path('provider/provider-query/demographics',
         views.provider_query_demographics, name='provider-query-demographics'),
    path('redirect_uri', views.redirect_uri, name='redirect_uri'),
]

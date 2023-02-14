EHR_CHOICES = [
    ("epic", "EPIC")
]

APP_TYPE = [
    ("provider", "Provider Facing Application"),
    ("patient", "Patient Facing Application"),
    ("system", "Backend System"),
]

GRANT_TYPE = [
    ("client_credentials", "Client Credentials"),
    ("authorization_code", "Authorization Code"),
]


CONSTANTS = {
    "EPIC": {
        "system": {
            "base_url_test": "https://fhir.epic.com/interconnect-fhir-oauth",
            "base_url_prod": None,
            "auth_url_test": "https://fhir.epic.com/interconnect-fhir-oauth/oauth2/token",
            "auth_url_prod": None,
        },
        "provider": {
            "base_url_test": "https://fhir.epic.com/interconnect-fhir-oauth",
            "base_url_prod": "https://fhir.epic.com/interconnect-fhir-oauth",
            "auth_url_test": "https://fhir.epic.com/interconnect-fhir-oauth/oauth2/token",
            "auth_url_prod": "https://fhir.epic.com/interconnect-fhir-oauth/oauth2/token",
            "auth_code_test": "https://fhir.epic.com/interconnect-fhir-oauth/oauth2/authorize",
            "auth_code_prod": "https://fhir.epic.com/interconnect-fhir-oauth/oauth2/authorize",
        },
        "patient": {
            "base_url_test": "https://fhir.epic.com/interconnect-fhir-oauth",
            "base_url_prod": "https://fhir.epic.com/interconnect-fhir-oauth",
            "auth_url_test": "https://fhir.epic.com/interconnect-fhir-oauth/oauth2/token",
            "auth_url_prod": "https://fhir.epic.com/interconnect-fhir-oauth/oauth2/token",
            "auth_code_test": "https://fhir.epic.com/interconnect-fhir-oauth/oauth2/authorize",
            "auth_code_prod": "https://fhir.epic.com/interconnect-fhir-oauth/oauth2/authorize",
        },
    },

}

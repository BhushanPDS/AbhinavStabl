import uuid

from django.core.validators import URLValidator
from django.db import models

from core.constants import APP_TYPE, CONSTANTS, EHR_CHOICES, GRANT_TYPE


class BaseModel(models.Model):
    """
    Base model for all models
    """

    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']
        get_latest_by = 'created_at'


class EHRConnection(BaseModel):

    connection_name = models.CharField(max_length=250)
    ehr_name = models.CharField(choices=EHR_CHOICES, max_length=255)
    app_type = models.CharField(choices=APP_TYPE, max_length=255)
    grant_type = models.CharField(
        choices=GRANT_TYPE, max_length=255, blank=True, null=True
    )
    client_id = models.CharField(max_length=250, unique=True)
    client_secret = models.CharField(max_length=250, blank=True, null=True)
    redirect_uri = models.URLField(max_length=255, blank=True, null=True)
    scope = models.TextField(blank=True, null=True)
    audiance = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    nonce = models.CharField(max_length=255, blank=True, null=True)
    launch = models.CharField(max_length=255, blank=True, null=True)
    base_url_test = models.URLField(max_length=250, blank=True, null=True)
    base_url_prod = models.URLField(max_length=250, blank=True, null=True)
    auth_url_test = models.URLField(max_length=250, blank=True, null=True)
    auth_url_prod = models.URLField(max_length=250, blank=True, null=True)
    authorize_url_test = models.URLField(max_length=255, blank=True, null=True)
    authorize_url_prod = models.URLField(max_length=255, blank=True, null=True)
    customer_auth_url_test = models.TextField(
        validators=[URLValidator()], blank=True, null=True
    )
    customer_auth_url_prod = models.TextField(
        validators=[URLValidator()], blank=True, null=True
    )
    access_token = models.TextField(blank=True, null=True)
    private_key = models.TextField(blank=True, null=True)
    tenant = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.uuid}"

    def save(self, *args, **kwargs):

        ehr_obj = CONSTANTS[self.ehr_name.upper()]

        if self.app_type.lower() == "provider" or self.app_type.lower() == "patient":
            self.grant_type = "authorization_code"

        elif self.app_type.lower() == "system":
            self.grant_type = "client_credentials"

        self.base_url_test = ehr_obj[self.app_type].get("base_url_test")
        self.base_url_prod = ehr_obj[self.app_type].get("base_url_prod")
        self.auth_url_test = ehr_obj[self.app_type].get("auth_url_test")
        self.auth_url_prod = ehr_obj[self.app_type].get("auth_url_prod")
        self.authorize_url_test = ehr_obj[self.app_type].get(
            "auth_code_test")
        self.authorize_url_prod = ehr_obj[self.app_type].get(
            "auth_code_prod")

        super().save(*args, **kwargs)

        def save(self, *args, **kwargs):
            for provider in self.provider_set.all():
                provider.save()

            super().save(*args, **kwargs)


class Customer(BaseModel):
    name = models.CharField(max_length=255)
    connection = models.ManyToManyField(EHRConnection, blank=True, null=True)
    email = models.EmailField(
        max_length=70, unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.uuid}"


class Provider(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=250, blank=True, null=True)
    lastname = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=250, blank=True, null=True)
    ehr_id = models.CharField(max_length=250, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    authorize_code = models.TextField(blank=True, null=True)
    access_token = models.TextField(blank=True, null=True)
    refresh_token = models.TextField(blank=True, null=True)
    refresh_token_last_updated_at = models.DateTimeField(null=True, blank=True)
    authorization_uri_test = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.uuid}"

    def save(self, *args, **kwargs):

        connection_object = self.customer.connection.get()
        client_id = connection_object.client_id
        redirect_uri = connection_object.redirect_uri
        aud = connection_object.audiance
        state = self.uuid
        scope = connection_object.scope
        self.authorization_uri_test = f"{connection_object.customer_auth_url_test}?client_id={client_id}&response_type=code&aud={aud}&redirect_uri={redirect_uri}&state={state}&scope={scope}"
        super().save(*args, **kwargs)


class Patient(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=250, blank=True, null=True)
    ehr_id = models.CharField(max_length=250, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    authorize_code = models.TextField(blank=True, null=True)
    access_token = models.TextField(blank=True, null=True)
    refresh_token = models.TextField(blank=True, null=True)
    refresh_token_last_updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.uuid}"

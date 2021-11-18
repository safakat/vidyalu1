from django.db import models
from core.models.users import User


class Counsellor(models.Model):
    counsellor = models.OneToOneField(User, on_delete=models.CASCADE)
    agency = models.CharField(max_length=191, null=True, blank=True)
    details = models.TextField(blank=True, null=True)
    services = models.JSONField(null=True, blank=True)
    certificate = models.FileField(upload_to="documents/", null=True, blank=True)
    awards = models.JSONField(null=True, blank=True)
    is_adharcard = models.BooleanField(default=False)
    is_pancard = models.BooleanField(default=False)
    is_passport = models.BooleanField(default=False)
    id_proof = models.FileField(upload_to="documents/", null=True, blank=True)
    step =models.PositiveIntegerField(default=0)
    search = models.CharField(max_length=199, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "counsellors"
        verbose_name = "Counsellors"
        verbose_name_plural = "Counsellor"
from django.db import models
from core.models.users import User


class SocialAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    provider = models.CharField(max_length=191, null=True, blank=True)
    extra_data = models.JSONField(null=True, blank=True)
    auth_token = models.TextField(null=True, blank=True)
    id_token = models.TextField(null=True, blank=True)
    uid = models.CharField(max_length=191, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "social_account"

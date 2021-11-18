from django.db import models
from rest_framework import serializers
from social_auth.models import SocialAccount
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import AuthenticationFailed
from core.models.users import User


class GoogleUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    # profile_image = serializers.CharField(required=False)
    # profile_image = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "username",
            "photo_url",
            "is_verified_email",
            "google_id",
        ]

    def to_internal_value(self, data):
        # data._mutable = True
        data["T_password"] = data["password"]
        data["password"] = make_password(data["password"])
        data["is_verified_email"] = True
        data["google_id"]=data["id"]
        data["photo_url"] = data["profile_image"]
        # data["profile_image"] = None
        # if not data["role"]:
        #     data["role"] = ""
        # data.mutable = False
        return super().to_internal_value(data)


class GoogleSocialuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccount
        fields = "__all__"


class SocialUserSerializer(serializers.ModelSerializer):
    # id = serializers.CharField(required=False)
    # email = serializers.CharField(required=False)
    # first_name = serializers.CharField(required=False)
    # last_name = serializers.CharField(required=False)
    # username = serializers.CharField(required=False)
    # profile_image = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "username",
            "profile_image",
            "uid",
            "provider",
            "extra_data",
            "auth_token",
            "id_token",
        ]


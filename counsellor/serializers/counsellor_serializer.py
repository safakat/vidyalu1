from rest_framework import serializers
from core.models.users import User
from counsellor.models.counsellors import Counsellor
from core.serializers.auth_serializer import UserSerializer
from social_auth.models import SocialAccount


class CounsellorSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="counsellor.email", read_only=True)
    username = serializers.CharField(source="counsellor.username", read_only=True)
    full_name = serializers.CharField(source="counsellor.full_name", read_only=True)
    address = serializers.CharField(source="counsellor.address", read_only=True)
    state = serializers.CharField(source="counsellor.state", read_only=True)
    city = serializers.CharField(source="counsellor.city", read_only=True)
    phone = serializers.CharField(source="counsellor.phone", read_only=True)
    zip_code = serializers.CharField(source="counsellor.area_code", read_only=True)
    profile_img = serializers.ImageField(source="counsellor.profile_image", read_only=True)
    photo_url = serializers.CharField(source="counsellor.photo_url", read_only=True)
    # provider = serializers.SerializerMethodField()

    class Meta:
        model = Counsellor
        exclude = ("id",)
        extra_fields = [
            "email",
            "username",
            "full_name",
            "address",
            "state",
            "city",
            "phone",
            "zip_code",
            "profile_img",
            "photo_url"
        ]

    # def get_provider(self, obj):
    #     if obj.counsellor.google_id:
    #         return "Google"

class GoogleSocialuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccount
        fields = ["provider",]


class ConsUserbasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["full_name","phone","address","state","city","area_code"]

class ConsBasicinfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Counsellor
        fields = ['agency','details','step']


class ConsUserApplicationformSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["profile_image",]

class CounsellorApplicationformSerializer(serializers.ModelSerializer):
    # certificate = serializers.FileField()

    class Meta:
        model = Counsellor
        fields = ('services', 'awards', 'certificate','step')



class CounsellorUploaddocSerializer(serializers.ModelSerializer):
    # profile_image = serializers.CharField(source="teacher.profile_image", read_only=True)

    class Meta:
        model = Counsellor
        fields = ('is_adharcard', 'is_pancard', 'is_passport','id_proof','step','search')


class CounsellorUserProfileSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(required=False)
    class Meta:
        model = User
        fields = ("email","username","phone","profile_image","state","area_code","city","address")

    # def to_internal_value(self, data):
    #     # data._mutable = True
    #     if not data["profile_image"]:
    #         del data["profile_image"]
    #     return super().to_internal_value(data)


class CounsellorProfileSerializer(serializers.ModelSerializer):
    certificate = serializers.FileField(required=False)
    id_proof = serializers.FileField(required=False)

    class Meta:
        model = Counsellor
        fields = ('agency','details','services', 'awards', 'certificate','id_proof','is_adharcard','is_pancard','is_passport','search',)


    # def to_internal_value(self, data):
    #     # data._mutable = True
    #     if not data["certificate"]:
    #         del data["certificate"]
    #     if not data["id_proof"]:
    #         del data["id_proof"]
    #     return super().to_internal_value(data)


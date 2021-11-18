from rest_framework import serializers
from core.models.users import User
from teacher.models.teachers import Teacher
from social_auth.models import SocialAccount
from core.serializers.auth_serializer import UserSerializer



class TeacherSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="teacher.email", read_only=True)
    username = serializers.CharField(source="teacher.username", read_only=True)
    full_name = serializers.CharField(source="teacher.full_name", read_only=True)
    address = serializers.CharField(source="teacher.address", read_only=True)
    state = serializers.CharField(source="teacher.state", read_only=True)
    city = serializers.CharField(source="teacher.city", read_only=True)
    phone = serializers.CharField(source="teacher.phone", read_only=True)
    zip_code = serializers.CharField(source="teacher.area_code", read_only=True)
    profile_img = serializers.ImageField(source="teacher.profile_image", read_only=True)
    photo_url = serializers.CharField(source="teacher.photo_url", read_only=True)
    # profile_img = serializers.SerializerMethodField()


    class Meta:
        model = Teacher
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
            "photo_url",
        ]




class GoogleSocialuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccount
        fields = ["provider",]




class TeacherUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # exclude = ["__all__"]
        fields = ["email","full_name","address","state","phone","area_code","city",]

class TeacherBasicinfoSerializer(serializers.ModelSerializer):
    # edu_qualification = serializers.CharField()
    step = serializers.CharField(required=False)

    class Meta:
        model = Teacher
        fields = ('step',)

class TeacherEducationalSerializer(serializers.ModelSerializer):
    # edu_qualification = serializers.CharField()

    class Meta:
        model = Teacher
        fields = ('edu_qualification', 'description', 'certificate','step')


class UserTeacherTeachingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["profile_image", ]



class TeacherTeachingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('tch_information', 'competency_area', 'tch_resume','is_adharcard', 'is_pancard','is_passport','id_proof','step','search',)
        # exclude = ("id", "teacher")


class TeacherUserProfileSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(required=False)
    class Meta:
        model = User
        fields = ("email","username","phone","profile_image","state","area_code","city","address")





class TeacherProfileSerializer(serializers.ModelSerializer):
    certificate = serializers.FileField(required=False)
    tch_resume = serializers.FileField(required=False)
    id_proof = serializers.FileField(required=False)


    class Meta:
        model = Teacher
        fields = ('edu_qualification','description', 'certificate','tch_information', 'competency_area', 'tch_resume','id_proof','is_adharcard',
                  'is_pancard','is_passport','search',)





from rest_framework import serializers
from core.models.users import User
from student.models.students import Student
from core.serializers.auth_serializer import UserSerializer
from social_auth.models import SocialAccount
from counsellor.models.counsellors import Counsellor


class StudentSerializer(serializers.ModelSerializer):
    """
        serializer for get the student user details.
    """
    email = serializers.CharField(source="student.email", read_only=True)
    username = serializers.CharField(source="student.username", read_only=True)
    full_name = serializers.CharField(source="student.full_name", read_only=True)
    address = serializers.CharField(source="student.address", read_only=True)
    state = serializers.CharField(source="student.state", read_only=True)
    city = serializers.CharField(source="student.city", read_only=True)
    phone = serializers.CharField(source="student.phone", read_only=True)
    zip_code = serializers.CharField(source="student.area_code", read_only=True)
    # profile_img = serializers.SerializerMethodField()
    profile_img = serializers.ImageField(source="student.profile_image", read_only=True)
    photo_url = serializers.CharField(source="student.photo_url", read_only=True)

    class Meta:
        model = Student
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
    """
           serializer for get the social student user details.
    """
    class Meta:
        model = SocialAccount
        fields = ["provider",]


class StudentUserSerializer(serializers.ModelSerializer):
    """
           serializer for update  the student user details step-1.
    """

    class Meta:
        model = User
        # exclude = ["__all__"]
        fields = ["email","full_name","address","state","phone","area_code","city","profile_image",]


class StudentBasicinfoSerializer(serializers.ModelSerializer):
    """
               serializer for update  the student user details step-1.
    """
    # edu_qualification = serializers.CharField()
    step = serializers.CharField(required=False)

    class Meta:
        model = Student
        fields = ('step',)


class StudentUserProfileSerializer(serializers.ModelSerializer):
    """
               serializer for update  the student profile details.
    """
    profile_image = serializers.ImageField(required=False)
    class Meta:
        model = User
        fields = ("email","username","phone","profile_image","state","area_code","city","address")





class StudentProfileSerializer(serializers.ModelSerializer):
    """
                   serializer for update  the student profile details.
    """
    step = serializers.CharField(required=False)

    class Meta:
        model = Student
        fields = ('step',)


#     certificate = serializers.FileField(required=False)
#     tch_resume = serializers.FileField(required=False)
#     id_proof = serializers.FileField(required=False)
#
#
#     class Meta:
#         model = Student
#         fields = ('edu_qualification','description', 'certificate','tch_information', 'competency_area', 'tch_resume','id_proof','is_adharcard',
#                   'is_pancard','is_passport')
#
#


class StudentCounsellorSerializer(serializers.ModelSerializer):
    """
              serializer for  student can view the counsellor details.
    """
    email = serializers.CharField(source="counsellor.email", read_only=True)
    username = serializers.CharField(source="counsellor.username", read_only=True)
    full_name = serializers.CharField(source="counsellor.full_name", read_only=True)
    address = serializers.CharField(source="counsellor.address", read_only=True)
    state = serializers.CharField(source="counsellor.state", read_only=True)
    city = serializers.CharField(source="counsellor.city", read_only=True)
    phone = serializers.CharField(source="counsellor.phone", read_only=True)
    zip_code = serializers.CharField(source="counsellor.area_code", read_only=True)
    profile_img = serializers.ImageField(source="counsellor.profile_image", read_only=True)
    # provider = serializers.SerializerMethodField()

    class Meta:
        model = Counsellor
        exclude = ("id", "counsellor")
        extra_fields = [
            "email",
            "username",
            "full_name",
            "address",
            "country",
            "phone",
            "zip_code",
            "profile_img",
        ]


from student.models.students import Student
from teacher.models.teachers import Teacher
from rest_framework import serializers
from counsellor.models.counsellors import Counsellor
from core.models.users import User





class StudentSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="student.email", read_only=True)
    username = serializers.CharField(source="student.username", read_only=True)
    full_name = serializers.CharField(source="student.full_name", read_only=True)
    address = serializers.CharField(source="student.address", read_only=True)
    state = serializers.CharField(source="student.state", read_only=True)
    city = serializers.CharField(source="student.city", read_only=True)
    phone = serializers.CharField(source="student.phone", read_only=True)
    zip_code = serializers.CharField(source="student.area_code", read_only=True)
    profile_img = serializers.ImageField(source="student.profile_image", read_only=True)
    block_by_admin = serializers.BooleanField(source="student.block_by_admin", read_only=True)
    photo_url = serializers.CharField(source="student.photo_url", read_only=True)

    class Meta:
        model = Student
        fields = '__all__'
        # exclude = ("id", "student")

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
            "block_by_admin",
        ]


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
    block_by_admin = serializers.BooleanField(source="teacher.block_by_admin", read_only=True)
    photo_url = serializers.CharField(source="teacher.photo_url", read_only=True)

    class Meta:
        model = Teacher
        fields = '__all__'
        # exclude = ("id", "teacher")
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
            "block_by_admin",
        ]



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
    block_by_admin = serializers.BooleanField(source="counsellor.block_by_admin", read_only=True)
    photo_url = serializers.CharField(source="counsellor.photo_url", read_only=True)

    class Meta:
        model = Counsellor
        fields = '__all__'
        # exclude = ("id", "counsellor")
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
            "block_by_admin",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # exclude = ("id", "created_at", "updated_at")
        fields = ["email","username","profile_image",]


# class AdminSerializer(serializers.ModelSerializer):
#     email = serializers.CharField(source="counsellor.email", read_only=True)
#     username = serializers.CharField(source="counsellor.username", read_only=True)
#     full_name = serializers.CharField(source="counsellor.full_name", read_only=True)
#     address = serializers.CharField(source="counsellor.address", read_only=True)
#     country = serializers.CharField(source="counsellor.country", read_only=True)
#     phone = serializers.CharField(source="counsellor.phone", read_only=True)
#     zip_code = serializers.CharField(source="counsellor.area_code", read_only=True)
#     profile_img = serializers.CharField(source="counsellor.profile_image", read_only=True)
#     block_by_admin = serializers.BooleanField(source="counsellor.block_by_admin", read_only=True)
#
#     class Meta:
#         model = Counsellor
#         fields = '__all__'
#         # exclude = ("id", "counsellor")
#         extra_fields = [
#             "email",
#             "username",
#             "full_name",
#             "address",
#             "country",
#             "phone",
#             "zip_code",
#             "profile_img",
#             "block_by_admin",
#         ]


# class blockbyadminSerializer(serializers.ModelSerializer):
#     """
#     Serializer for bock_by_admin endpoint.
#     """
#
#     # block_by_admin = serializers.BooleanField(required=True)
#
#     class Meta:
#         model =User
#         fields = ["block_by_admin"]
#
#
#     def validate(self, attrs):
#         id = attrs.get("id",None)
#         # print(*args)
#         block_by_admin = attrs.get("block_by_admin")
#         usr = User.objects.get(id=id)
#
#         if usr.block_by_admin==True:
#             raise serializers.ValidationError("already blocked by admin pls contact with admin")
#         return super().validate(attrs)

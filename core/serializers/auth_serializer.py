from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from core.models.users import User
from student.models.students import Student
from teacher.models.teachers import Teacher
from counsellor.models.counsellors import Counsellor
from django.utils import timezone
from rest_framework import status
from django.contrib.auth.hashers import make_password
from core.helpers import password_validation
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework.exceptions import AuthenticationFailed
from django.utils.encoding import force_str
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from core.models.locations import Location


class RegisterSerializer(serializers.ModelSerializer):
    retype_password = serializers.CharField(required=True, style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = (
            "role",
            "username",
            "email",
            "password",
            "retype_password",
        )
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}},
        }

    def validate(self, attrs):
        usernmae = attrs.get("usernmae")
        email = attrs.get("email")
        password = attrs.get("password")
        retype_password = attrs.get("retype_password")
        # if User.objects.filter(username=usernmae):
        #     raise serializers.ValidationError("username already exists")
        if User.objects.filter(email=email):
            raise serializers.ValidationError("email already exists")
        if password != retype_password:
            raise serializers.ValidationError("passwords must match")
        pwd_err = password_validation(password)
        if pwd_err:
            raise serializers.ValidationError(pwd_err)

        return super().validate(attrs)

    def create(self, attrs):
        usernmae = attrs["username"]
        email = attrs["email"]
        role = attrs["role"]
        password = attrs["password"]

        user = User(
            email=email,
            username=usernmae,
            role=role,
        )
        user.set_password(password)
        user.save()
        if user.role == "student":
            Student.objects.create(student=user)
        elif user.role == "teacher":
            Teacher.objects.create(teacher=user)
        elif user.role == "counsellor":
            Counsellor.objects.create(counsellor=user)
        else:
            pass
        return user


class MyTokenObtainPairSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj["email"])
        token = RefreshToken.for_user(user)
        refresh = str(token)
        access = str(token.access_token)
        data = {"refresh": refresh, "access": access}
        # data["first_name"] = user.first_name
        if user.role == None:
            data["role"] = " "
        else:
            data["role"] = user.role

        return data

    class Meta:
        model = User
        fields = ["email", "password", "tokens"]

    def validate(self, attrs):
        email = attrs.get("email", "")
        password = attrs.get("password", "")
        user = authenticate(email=email, password=password)
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email not Found')
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        if user.block_by_admin == True:
            raise serializers.ValidationError("You are blocked by admin. Please contact to admin")
        if user.is_verified_email == False:
            raise serializers.ValidationError("Your email is not verified, please verify your email.")

        # if not user.is_verified:
        #     raise AuthenticationFailed('Email is not verified')

        # return {"email": user.email, "username": user.username, "tokens": user.tokens}

        return super().validate(attrs)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # exclude = ("id", "created_at", "updated_at")
        fields = "__all__"

# class SocialuserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         # exclude = ("id", "created_at", "updated_at")
#         fields = ("auth_token", "email", "first_name","social_id","socialid_token","username","photourl","provider")
#
# class SocialuserroleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         # exclude = ("id", "created_at", "updated_at")
#         fields = ("role",)

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=20)

    class Meta:
        fields = ["email"]


class SetNewPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    # retype_password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ["new_password", "token", "uidb64"]

    def validate(self, attrs):
        new_password = attrs.get("new_password")
        # retype_password = attrs.get("retype_password")
        # if new_password != retype_password:
        #     raise serializers.ValidationError("passwords must be same")
        errors = password_validation(new_password)
        if errors:
            raise serializers.ValidationError(errors)
        else:
            attrs["new_password"] = make_password(attrs["new_password"])
        token = attrs.get("token")
        uidb64 = attrs.get("uidb64")
        user_id = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=user_id)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError("The reset link is invalid")
        user.password = attrs["new_password"]
        user.save()
        return super().validate(attrs)




# class VerifyemailSerializer(serializers.Serializer):
#     is_verified_email = serializers.BooleanField(default=False)
#     # retype_password = serializers.CharField(min_length=6, max_length=68, write_only=True)
#     token = serializers.CharField(min_length=1, write_only=True)
#     uidb64 = serializers.CharField(min_length=1, write_only=True)
#
#     class Meta:
#         fields = ["is_verified_email", "token", "uidb64"]
#
#     def validate(self, attrs):
#         is_verified_email = attrs.get("is_verified_email")
#         # retype_password = attrs.get("retype_password")
#         # if new_password != retype_password:
#         #     raise serializers.ValidationError("passwords must be same")
#         # errors = password_validation(new_password)
#         # if errors:
#         #     raise serializers.ValidationError(errors)
#         # else:
#         #     attrs["new_password"] = make_password(attrs["new_password"])
#         token = attrs.get("token")
#         uidb64 = attrs.get("uidb64")
#         user_id = force_str(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(id=user_id)
#         if not PasswordResetTokenGenerator().check_token(user, token):
#             raise serializers.ValidationError("The reset link is invalid")
#         user.is_verified_email = attrs["is_verified_email"]
#         user.save()
#         return super().validate(attrs)

class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate(self, attrs):
        password = attrs.get("new_password")
        errors = password_validation(password)
        if errors:
            raise serializers.ValidationError(errors)
        return super().validate(attrs)



# class StateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = States
#         # exclude = ("id", "created_at", "updated_at")
#         fields = "__all__"
#
#
# class CitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cities
#         # exclude = ("id", "created_at", "updated_at")
#         fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    city_array = serializers.SerializerMethodField()

    class Meta:
        model = Location
        # exclude = ("id", "created_at", "updated_at")
        fields = ["state", "city_array"]

    def get_city_array(self, obj):
        cities = self.context["cities"]
        city_state = list(filter(lambda city: city["state"] == obj["state"], cities))
        city_list = []
        for state in city_state:
            city_list.append(state["city"])
        return city_list
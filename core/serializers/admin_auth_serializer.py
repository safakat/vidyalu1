from rest_framework import serializers
from core.models.users import User
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth
from core.helpers import password_validation
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework.exceptions import AuthenticationFailed
from django.utils.encoding import force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator



class AdminRegisterSerializer(serializers.ModelSerializer):
    retype_password = serializers.CharField(required=True, style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = (
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
        # pwd_err = password_validation(password)
        # if pwd_err:
        #     raise serializers.ValidationError(pwd_err)

        return super().validate(attrs)

    def create(self, attrs):
        usernmae = attrs["username"]
        email = attrs["email"]
        # role = attrs["role"]
        password = attrs["password"]

        user = User(
            email=email,
            username=usernmae,
            # role=role,
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_user = False
        user.is_staff = True
        user.save()
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
        data["role"] = "admin"
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
        if not user.is_superuser:
            raise serializers.ValidationError("User is not  admin")

        # if not user.is_verified:
        #     raise AuthenticationFailed('Email is not verified')

        # return {"email": user.email, "username": user.username, "tokens": user.tokens}

        return super().validate(attrs)


# class MyTokenObtainPairSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(max_length=255, min_length=3)
#     password = serializers.CharField(max_length=68, min_length=6, write_only=True)
#     tokens = serializers.SerializerMethodField()
#
#     def get_tokens(self, obj):
#         user = User.objects.get(username=obj["username"])
#         token = RefreshToken.for_user(user)
#         refresh = str(token)
#         access = str(token.access_token)
#         data = {"refresh": refresh, "access": access}
#         # data["first_name"] = user.first_name
#         # data["role"] = user.role
#         return data
#
#     class Meta:
#         model = User
#         fields = ["username", "password", "tokens"]
#
#     def validate(self, attrs):
#         username = attrs.get("username", "")
#         password = attrs.get("password", "")
#         try:
#             u=User.objects.get(username=username)
#         except User.DoesNotExist:
#             raise serializers.ValidationError("invalid username")
#         user = authenticate(email=u.email, password=password)
#
#         if not user:
#             raise serializers.ValidationError("Invalid credentials")
#
#         if not user.is_superuser:
#             raise serializers.ValidationError("User is not  admin")
#
#         # if not user.is_verified:
#         #     raise AuthenticationFailed('Email is not verified')
#
#         # return {"email": user.email, "username": user.username, "tokens": user.tokens}
#
#         return super().validate(attrs)
#

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
        # errors = password_validation(new_password)
        # if errors:
        #     raise serializers.ValidationError(errors)
        # else:
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


# class ChangePasswordSerializer(serializers.Serializer):
#     """
#     Serializer for password change endpoint.
#     """
#
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)
#
#     def validate(self, attrs):
#         password = attrs.get("new_password")
#         errors = password_validation(password)
#         if errors:
#             raise serializers.ValidationError(errors)
#         return super().validate(attrs)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # exclude = ("id", "created_at", "updated_at")
        fields = ["email","username","profile_image",]

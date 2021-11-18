from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from core.models.users import User
from core.helpers import api_response
from core.serializers.admin_auth_serializer import *
from rest_framework.views import APIView
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_str, smart_bytes, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from urllib.parse import urlparse
from django.core.mail import send_mail
from vidyalu import settings
from rest_framework.permissions import IsAuthenticated,IsAdminUser


class AdminRegisterView(generics.GenericAPIView):
    serializer_class = AdminRegisterSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_superuser = 1
            user.is_user = 0
            user.is_staff = 1
            user.save()
            token = RefreshToken.for_user(user)
            user_data = {
                "access_token": str(token.access_token),
                "refresh_token": str(token),
            }
            return api_response(201, "Registration successfully done", serializer.data, status=True)
        else:
            errors_list = [serializer.errors[error][0] for error in serializer.errors]
            return api_response(400, errors_list[0], {}, status=False)


class AdminLoginAPIView(generics.GenericAPIView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return api_response(200, "Login success", serializer.data["tokens"], status=True)
        else:
            errors_list = [serializer.errors[error][0] for error in serializer.errors]
            return api_response(400, errors_list[0], {}, status=False)


class AdminRequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data.get("email", "")

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            to_email = user.email
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            url = settings.SITEURL + "reset-password?/"
            # path = request.build_absolute_uri()
            # url_parse = urlparse(path)
            # base_url = url_parse.scheme + "://" + url_parse.netloc + "/reset-password?"
            absurl = str(url) + "uidb64=" + uidb64 + "&" + "token=" + token
            subject = "Reset your passsword"
            body = "Hi,\n" + user.username + "\n" + "Use link below to reset your password\n" + absurl
            send_mail(subject, body, settings.EMAIL_HOST_USER, [to_email])
            return api_response(200, "We have sent you a link to reset your password", {}, status=True)
        else:
            return api_response(400, "Your mail is not registered with us", {}, status=False)


class AdminSetNewPasswordView(generics.GenericAPIView):
    """
    An endpoint for reset password.
    """

    serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64="0000", token=None):
        try:
            if "uidb64" in request.GET and request.GET["uidb64"] != "":
                uidb64 = request.GET["uidb64"]
            if "token" in request.GET and request.GET["token"] != "":
                token = request.GET["token"]
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return api_response(400, "Invalid Token Please Request New One.", {}, status=False)
            else:
                return api_response(200, "Token is valid", {}, status=True)
        except:
            return api_response(400, "Invalid Token Please Request New One.", {}, status=False)

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return api_response(200, "password reset success", {}, status=True)
        else:
            errors_list = [serializer.errors[error][0] for error in serializer.errors]
            return api_response(400, errors_list[0], {}, status=False)


class AdminView(APIView):
    permission_classes = (IsAdminUser,)
    # parser_class = (FileUploadParser,)

    def get(self,request):
        try:
            user = User.objects.get(id=request.user.id)
            serializer = UserSerializer(user)
            return api_response(200, "Admin profile retrieved successfully.", serializer.data, status=True)
        except User.DoesNotExist:
            return api_response(400, "Admin Not Found", {}, status=False)

# class UpdatePassword(APIView):
#     """
#     An endpoint for changing password.
#     """
#
#     permission_classes = (IsAuthenticated,)
#
#     def get_object(self, queryset=None):
#         return self.request.user
#
#     def put(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         serializer = ChangePasswordSerializer(data=request.data)
#
#         if serializer.is_valid(raise_exception=True):
#             # Check old password
#             old_password = serializer.data.get("old_password")
#             if not self.object.check_password(old_password):
#                 return api_response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
#             # set_password also hashes the password that the user will get
#             self.object.set_password(serializer.data.get("new_password"))
#             self.object.save()
#             return api_response(200, "password updated successfully", {})
#
#         return api_response(400, "password not updated.", {})
#
#
#

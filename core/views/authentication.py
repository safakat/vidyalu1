from datetime import date,timedelta
from rest_framework import generics
from rest_framework.views import APIView
from core.models.users import User
from core.serializers.auth_serializer import *
from core.helpers import api_response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from core.serializers.auth_serializer import MyTokenObtainPairSerializer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import send_mail
from vidyalu import settings
from urllib.parse import urlparse
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout as django_logout, login, authenticate
from core.views.send_emails import send_onboard_eamil
from core.models.locations import Location
from django.utils import timezone







class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    # parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = RefreshToken.for_user(user)
            send_onboard_eamil(request, user.email)
            user_data = {
                "access_token": str(token.access_token),
                "refresh_token": str(token),
            }
            return api_response(201, "An activation link has been send to your email. Please verify.", serializer.data, status=True)
        else:
            errors_list = [serializer.errors[error][0] for error in serializer.errors]
            return api_response(400, errors_list[0], {}, status=False)



class VerifyMyEmailView(APIView):
    def get(self, request, uidb64="0000", token=None):
        try:
            if "uidb64" in request.GET and request.GET["uidb64"] != "":
                uidb64 = request.GET["uidb64"]
            if "token" in request.GET and request.GET["token"] != "":
                token = request.GET["token"]
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            user_created_at = user.created_at
            after_24hr_dt = user_created_at + timedelta(minutes=4)
            now_dt = timezone.now()
            if not (now_dt < after_24hr_dt) and user.is_verified_email == False:
                user.delete()
                return api_response(200, "Your link has been expired. Your record has been removed, please sign up again and verify your email.", {}, status=True)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return api_response(400, "Invalid Token Please Request New One.", {}, status=False)
            else:
                user.is_verified_email = True
                user.save()
                return api_response(200, "Your email has been verified", {}, status=True)
        except:
            return api_response(200, "Your link has been expired. Your record has been removed, please sign up again and verify your email.", {}, status=True)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return api_response(200, "Login success", serializer.data["tokens"], status=True)
        else:
            errors_list = [serializer.errors[error][0] for error in serializer.errors]
            return api_response(400, errors_list[0], {}, status=False)


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data.get("email", "")

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            to_email = user.email
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            url = settings.SITEURL + "reset-password?"
            # path = request.build_absolute_uri()
            # url_parse = urlparse(path)
            # base_url = url_parse.scheme + "://" + url_parse.netloc + "/reset-password?"
            absurl = str(url) + "uidb64=" + uidb64 + "&" + "token=" + token
            subject = "Reset your passsword"
            body = "Hi,\n"+user.username +"\n"+ "Use link below to reset your password\n" + absurl
            send_mail(subject, body, settings.EMAIL_HOST_USER, [to_email])
            return api_response(200, "We have sent you a link to reset your password", {}, status=True)
        else:
            return api_response(400, "Your mail is not registered with us", {}, status=False)




class SetNewPasswordView(generics.GenericAPIView):
    """
    An endpoint for forget password.
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




class UpdatePassword(APIView):
    """
    An endpoint for reset password.
    """

    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return api_response(400, "Wrong old_password.", {}, status=False)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return api_response(200, "password updated successfully", {}, status=True)
        else:
            errors_list = [serializer.errors[error][0] for error in serializer.errors]
            return api_response(400, errors_list[0], {}, status=False)

        # return api_response(400, "password not updated.", {}, status=False)



# # States
# class StatesView(APIView):
#     # permission_classes = (IsAdminUser,)
#
#     def get(self, request):
#         state = States.objects.filter(country_id = 101)
#         # print("state", state.id)
#         # city = Cities.objects.filter(state_id = id)
#         if state:
#             serializer1 = StateSerializer(state, many=True)
#             # serializer2 = CitySerializer(city, many=True)
#             # s=serializer1 + serializer2
#             return api_response(200, "States retrieved successfully.", serializer1.data, status=True)
#         else:
#             return  api_response(404,"No states found",{},status=False)

class LocationView(APIView):
    def get(self, request):
        countries = Location.objects.filter(country="India")
        states = countries.values("state").distinct()
        cities = countries.values("city", "state")
        serializer = LocationSerializer(states, context={"cities": cities}, many=True)
        return api_response(200, "locations retrieved successfully", serializer.data, status=True)




class Logout(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        if getattr(settings, "ACCOUNT_LOGOUT_ON_GET", False):
            response = self.logout(request)
        else:
            response = self.http_method_not_allowed(request, *args, **kwargs)

        return self.finalize_response(request, response, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.logout(request)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        if getattr(settings, "REST_SESSION_LOGIN", True):
            django_logout(request)

        response = api_response(200,"Successfully logged out.",{},status=True)
        return response

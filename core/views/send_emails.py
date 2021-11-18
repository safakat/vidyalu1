from core.models.users import User
from django.utils.encoding import smart_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from urllib.parse import urlparse
from django.core.mail import send_mail
from vidyalu import settings
from core.helpers import api_response


def send_onboard_eamil(request, email):
    """
    Send activation Link to registered email address
    """
    if User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        # url = settings.SITEURL + "/api/verify-email?/"
        # path = request.build_absolute_uri()
        # url_parse = urlparse(path)
        # base_url = url_parse.scheme + "://" + url_parse.netloc
        absurl = settings.SITEURL + "email-verification?" + "uidb64=" + uidb64 + "&token=" + token
        # absurl = str(url) + "uidb64=" + uidb64 + "&" + "token=" + token
        subject = "Vidyalu account verification."
        body =  "Hi,\n" + user.username + "\n" +"Please click below link to verify your email address\n" + absurl
        send_mail(subject, body, settings.EMAIL_HOST_USER, [email])
        return api_response(200, "We have sent you a link to activate your account", {"uidb64": uidb64, "token": token})
    return api_response(404, "User email not found", {"email": email})

# http://localhost:8000/email-verification?uidb64=NDc&token=aqrri7-2bbd35633a192bed30a08c85307ef5df
# https://vidyalu.myvtd.site/email-verification?%2Fuidb64=Mzg&token=aqrogw-17fa0bb69bca5a061902c7e176d65f57


# def send_onboard_eamil(request, email):
#     """
#     Send activation Link to registered email address
#     """
#     if User.objects.filter(email=email).exists():
#         user = User.objects.get(email=email)
#         uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
#         token_generator = PasswordResetTokenGenerator()
#         token = token_generator.make_token(user)
#         path = request.build_absolute_uri()
#         url_parse = urlparse(path)
#         base_url = url_parse.scheme + "://" + url_parse.netloc
#         absurl = base_url + "/email-verification?" + "uidb64=" + uidb64 + "&token=" + token
#         subject = "Vidyalu account verification."
#         body = "Please click below link to verify your email address\n" + absurl
#         send_mail(subject, body, settings.EMAIL_HOST_USER, [email])
#         return api_response(200, "We have sent you a link to activate your account", {"uidb64": uidb64, "token": token})
#     return api_response(404, "User not found", {"email": email})

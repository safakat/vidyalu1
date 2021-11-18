from rest_framework.response import Response
import re


def api_response(code, message, data,status=None):
    data = {
        "status": status,
        "code": code,
        "message": message,
        "data": data,
    }
    return Response(data=data, status=code)

def password_validation(password):
    if not len(password) >= 8:
        return "Your password must contain at least 8 characters."
    if not re.findall("\d", password):
        return "Your password must contain at least 1 digit, 0-9."
    if not re.findall("[A-Z]", password):
        return "Your password must contain at least 1 uppercase letter, A-Z."
    if not re.findall("[a-z]", password):
        return "Your password must contain at least 1 lowercase letter, a-z."
    if not re.findall("[()[\]{}|\\`~!@#$%^&*_\-+=;:'\",<>./?]", password):
        return "Your password must contain at least one special symbol."
    else:
        return None
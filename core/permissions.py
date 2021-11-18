# -*- coding: utf-8 -*-
"""
Permission for each API application
As each API subapplication is meant for
a particular user role. And they are seperated
by the path in URI too. How a visiable abstraction
to human eye.
"""


from rest_framework.permissions import BasePermission

class IsTeacher(BasePermission):
    """
    Allows access only to teacher users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_active and request.user.role == 'teacher')



class IsCounsellor(BasePermission):
    """
    Allows access only to Counsellor users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_active and request.user.role == 'counsellor')



class IsStudent(BasePermission):
    """
    Allows access only to Student users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_active and request.user.role == 'student')

class IsTeacherCounsellor(BasePermission):
    """
    Allows access only to teacher and counsellor users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_active and request.user.role == 'teacher' or 'counsellor')

class IsStudentTeacher(BasePermission):
    """
    Allows access only to teacher and student users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_active and request.user.role == 'teacher' or 'student')


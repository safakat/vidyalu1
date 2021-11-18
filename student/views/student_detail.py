from core.models.users import User
from django.db.models import manager
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.helpers import api_response
from student.models.students import Student
from student.serializers.student_serializer import *
from social_auth.models import SocialAccount
from counsellor.models.counsellors import Counsellor



class StudentView(APIView):
    """
        student profile can be get put and delete the details.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            stu = Student.objects.get(student_id=request.user.id)
            serializer1 = StudentSerializer(stu)
            data1 = serializer1.data
        except Student.DoesNotExist:
            return api_response(400, "Student Not Found", {}, status=False)
        try:
            social_stu = SocialAccount.objects.get(user_id=request.user.id)
            serializer2 = GoogleSocialuserSerializer(social_stu)
            data2 = serializer2.data
        except SocialAccount.DoesNotExist:
            data2 = {}
        serialized_data = data1
        serialized_data.update(data2)
        return api_response(200, "Student profile retrieved successfully.", serialized_data, status=True)



    def put(self, request):
        try:
            stu = Student.objects.get(student_id=request.user.id)
            user = stu.student
            # user = User.objects.get(id=request.user.id)
            serializer1 = StudentUserProfileSerializer(user, data=request.data, partial=True)
            serializer2 = StudentProfileSerializer(stu, data=request.data, partial=True)
            if serializer1.is_valid(raise_exception=True):
                serializer1.save()
            if serializer2.is_valid(raise_exception=True):
                serializer2.save()
            else:
                return api_response(400, "Invalid data", {}, status=False)
            data = serializer1.data
            data.update(serializer2.data)
            return api_response(200, "Profile updated successfully", data, status=True)
        except Student.DoesNotExist:
            return api_response(400, "Student Not Found", {}, status=False)

    def delete(self, request):
        try:
            user = User.objects.get(id=request.user.id)
            user.delete()
            return api_response(204, "Student deleted success", {}, status=True)
        except User.DoesNotExist:
            return api_response(400, "Student Not Found", {}, status=False)



class StudentBasicinformation(APIView):
    """
            student update the profile step-1.
    """
    permission_classes = (IsAuthenticated,)


    def put(self, request):
        try:
            stu = Student.objects.get(student_id=request.user.id)
            user = stu.student
            serializer1 = StudentUserSerializer(user, data=request.data, partial=True)
            serializer2 = StudentBasicinfoSerializer(stu, data=request.data, partial=True)
            if serializer1.is_valid(raise_exception=True):
                serializer1.save()
            if serializer2.is_valid(raise_exception=True):
                serializer2.save(step=1)
            else:
                return api_response(400, "Invalid data", {}, status=False)
            data = serializer1.data
            data.update(serializer2.data)
            return api_response(200, "Profile updated successfully", data, status=True)
        except Student.DoesNotExist:
            return api_response(400, "Student Not Found", {}, status=False)



class StudentcounsellorView(APIView):
    """
            student can view the counsellor details.
    """

    def get(self,request):
        counsellor = Counsellor.objects.filter(step=3)
        if counsellor:
            serializer = StudentCounsellorSerializer(counsellor, many=True)
            return api_response(200, "Counsellor profile retrieved successfully.", serializer.data, status=True)
        else:
            return api_response(404, "No counsellor found", {}, status=False)
from core.models.users import User
from django.db.models import manager
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.helpers import api_response
from teacher.models.teachers import Teacher
from teacher.serializers.teacher_serializer import *
from core.serializers.auth_serializer import UserSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser


class TeacherView(APIView):
    permission_classes = (IsAuthenticated,)
    #
    # def get(self,request):
    #     role = request.GET.get('role', None)
    #     pincode = request.GET.get('role', None)
    #     city = request.GET.get('role', None)
    #     results = User.objects.all()
    #     if role == "teacher":
    #         results = results.filter(is_teacher=True)
    #     if pincode:
    #         results = results
    #
    #     try:
    #         tch = Teacher.objects.get(teacher_id=request.user.id)
    #         # user = tch.teacher
    #         serializer = TeacherSerializer(tch)
    #         return api_response(200, "Teacher profile retrieved successfully.", serializer.data, status=True)
    #     except Teacher.DoesNotExist:
    #         return api_response(400, "Teacher Not Found", {}, status=False)
    #
    def get(self, request):
        try:
            tch = Teacher.objects.get(teacher_id=request.user.id)
            serializer1 = TeacherSerializer(tch)
            data1 = serializer1.data
        except Teacher.DoesNotExist:
            return api_response(400, "Teacher Not Found", {}, status=False)
        try:
            social_tch = SocialAccount.objects.get(user_id=request.user.id)
            serializer2 = GoogleSocialuserSerializer(social_tch)
            data2 = serializer2.data
        except SocialAccount.DoesNotExist:
            data2 = {}
        serialized_data = data1
        serialized_data.update(data2)
        return api_response(200, "Teacher profile retrieved successfully.", serialized_data, status=True)


    def put(self,request):
        try:
            tch = Teacher.objects.get(teacher_id=request.user.id)
            user = tch.teacher
            serializer1 = TeacherUserProfileSerializer(user, data=request.data, partial=True)
            serializer2 = TeacherProfileSerializer(tch, data=request.data, partial=True)
            if serializer1.is_valid(raise_exception=True):
                serializer1.save()
            if serializer2.is_valid(raise_exception=True):
                serializer2.save()
            else:
                return api_response(400, "Invalid data", {}, status=False)
            data = serializer1.data
            data.update(serializer2.data)
            return api_response(200, "Profile updated successfully", data, status=True)
        except Teacher.DoesNotExist:
            return api_response(400, "Teacher Not Found", {}, status=False)


    def delete(self,request):
        try:
            user = User.objects.get(id=request.user.id)
            user.delete()
            return api_response(204, "Teacher deleted success", {}, status=True)
        except User.DoesNotExist:
            return api_response(400, "Teacher Not Found", {}, status=False)






class TeacherBasicinformation(APIView):
    permission_classes = (IsAuthenticated,)

    # def get(self, request):
    #     try:
    #         tch = Teacher.objects.get(teacher_id=request.user.id)
    #         serializer = UserSerializer(tch)
    #         return api_response(200, "Teacher profile retrieved successfully.", serializer.data, status=True)
    #     except Teacher.DoesNotExist:
    #         return api_response(400, "Teacher Not Found", {}, status=False)

    def put(self, request):
        try:
            tch = Teacher.objects.get(teacher_id=request.user.id)
            user = tch.teacher
            serializer1 = TeacherUserSerializer(user, data=request.data, partial=True)
            serializer2 = TeacherBasicinfoSerializer(tch, data=request.data, partial=True)
            if serializer1.is_valid(raise_exception=True):
                serializer1.save()
            if serializer2.is_valid(raise_exception=True):
                serializer2.save(step=1)
            else:
                return api_response(400, "Invalid data", {}, status=False)
            data = serializer1.data
            data.update(serializer2.data)
            return api_response(200, "Profile updated successfully", data, status=True)
        except Teacher.DoesNotExist:
            return api_response(400, "Teacher Not Found", {}, status=False)


class TeacherEducationalqualification(APIView):
    permission_classes = (IsAuthenticated,)
    # parser_class = (FileUploadParser,)
    parser_classes = (MultiPartParser, FormParser)

    # def get(self, request):
    #     try:
    #         tch = Teacher.objects.get(teacher_id=request.user.id)
    #         serializer = TeacherEducationalSerializer(tch)
    #         return api_response(200, "Teacher profile retrieved successfully.", serializer.data, status=True)
    #     except Teacher.DoesNotExist:
    #         return api_response(400, "Teacher Not Found", {}, status=False)

    def put(self, request,*args, **kwargs):
        try:
            tch = Teacher.objects.get(teacher_id=request.user.id)
            # user = tch.teacher
            serializer = TeacherEducationalSerializer(tch, data=request.data,partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(step=2)
                # print(serializer.data["edu_qualification"])
                # serializer.data["edu_qualification"] = eval(serializer.data["edu_qualification"][0])
                return api_response(200, "Profile updated successfully", serializer.data, status=True)
            else:
                return api_response(400, "Invalid data", {}, status=False)
        except Teacher.DoesNotExist:
            return api_response(400, "Teacher Not Found", {}, status=False)


class TeacherTeachinginformation(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)

    #
    # def get(self, request):
    #     try:
    #         tch = Teacher.objects.get(teacher_id=request.user.id)
    #         serializer = TeacherTeachingSerializer(tch)
    #         return api_response(200, "Teacher profile retrieved successfully.", serializer.data, status=True)
    #     except Teacher.DoesNotExist:
    #         return api_response(400, "Teacher Not Found", {}, status=False)

    def put(self, request,):
        try:
            tch = Teacher.objects.get(teacher_id=request.user.id)
            user = tch.teacher
            serializer1 = UserTeacherTeachingSerializer(user, data=request.data, partial=True)
            serializer2 = TeacherTeachingSerializer(tch, data=request.data, partial=True)
            if serializer1.is_valid(raise_exception=True):
                serializer1.save()
            if serializer2.is_valid(raise_exception=True):
                serializer2.save(step=3)
            else:
                return api_response(400, "Invalid data", {}, status=False)
            data = serializer1.data
            data.update(serializer2.data)
            return api_response(200, "Profile updated successfully", data, status=True)
        except Teacher.DoesNotExist:
            return api_response(400, "Teacher Not Found", {}, status=False)


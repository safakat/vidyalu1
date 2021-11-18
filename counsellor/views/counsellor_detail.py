from core.models.users import User
from django.db.models import manager
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.helpers import api_response
from counsellor.models.counsellors import Counsellor
from counsellor.serializers.counsellor_serializer import *
from core.serializers.auth_serializer import UserSerializer


class CounsellorView(APIView):
    permission_classes = (IsAuthenticated,)

    # def get(self,request):
    #     try:
    #         cons = Counsellor.objects.get(counsellor_id=request.user.id)
    #         serializer = CounsellorSerializer(cons)
    #         return api_response(200,"Counsellor profile retrieved successfully.",serializer.data, status=True)
    #     except Counsellor.DoesNotExist:
    #         return api_response(400, "Counsellor Not Found", {}, status=False)

    def get(self, request):
        try:
            cons = Counsellor.objects.get(counsellor_id=request.user.id)
            serializer1 = CounsellorSerializer(cons)
            data1 = serializer1.data
        except Counsellor.DoesNotExist:
            return api_response(400, "Counsellor Not Found", {}, status=False)
        try:
            social_cons = SocialAccount.objects.get(user_id=request.user.id)
            serializer2 = GoogleSocialuserSerializer(social_cons)
            data2 = serializer2.data
        except SocialAccount.DoesNotExist:
            data2 = {}
        serialized_data = data1
        serialized_data.update(data2)
        return api_response(200, "Counsellor profile retrieved successfully.", serialized_data, status=True)


    def put(self,request):
        try:
            cons = Counsellor.objects.get(counsellor_id=request.user.id)
            user = cons.counsellor
            serializer1 = CounsellorUserProfileSerializer(user, data=request.data, partial=True)
            serializer2 = CounsellorProfileSerializer(cons, data=request.data, partial=True)
            if serializer1.is_valid(raise_exception=True):
                serializer1.save()
            if serializer2.is_valid(raise_exception=True):
                serializer2.save()
            else:
                return api_response(400, "Invalid data", {}, status=False)
            data = serializer1.data
            data.update(serializer2.data)
            return api_response(200, "Profile updated successfully", data, status=True)
        except Counsellor.DoesNotExist:
            return api_response(400, "Counsellor Not Found", {}, status=False)


    def delete(self,request):
        try:
            user = User.objects.get(id=request.user.id)
            user.delete()
            return api_response(204, "Counsellor deleted success", {}, status=True)
        except User.DoesNotExist:
            return api_response(400, "Counsellor Not Found", {}, status=False)


class CounsellorBasicinformation(APIView):
    permission_classes = (IsAuthenticated,)

    # def get(self, request):
    #     try:
    #         cons = Counsellor.objects.get(counsellor_id=request.user.id)
    #         serializer = ConsBasicinfoSerializer(cons)
    #         return api_response(200, "Counsellor profile retrieved successfully.", serializer.data, status=True)
    #     except Counsellor.DoesNotExist:
    #         return api_response(400, "Counsellor Not Found", {}, status=False)

    def put(self, request):
        try:
            cons = Counsellor.objects.get(counsellor_id=request.user.id)
            user = cons.counsellor
            serializer1 = ConsUserbasicSerializer(user, data=request.data, partial=True)
            serializer2 = ConsBasicinfoSerializer(cons, data=request.data, partial=True)
            if serializer1.is_valid(raise_exception=True):
                serializer1.save()
            if serializer2.is_valid(raise_exception=True):
                serializer2.save(step=1)
            else:
                return api_response(400, "Invalid data", {}, status=False)
            data=serializer1.data
            data.update(serializer2.data)
            return api_response(200, "Profile updated successfully", data, status=True)

        except Counsellor.DoesNotExist:
            return api_response(400, "Counsellor Not Found", {}, status=False)


class CounsellorApplicationform(APIView):
    permission_classes = (IsAuthenticated,)
    # parser_class = (FileUploadParser,)
    # parser_classes = (MultiPartParser, FormParser)

    # def get(self, request):
    #     try:
    #         cons = Counsellor.objects.get(counsellor_id=request.user.id)
    #         serializer = CounsellorApplicationformSerializer(cons)
    #         return api_response(200, "Counsellor profile retrieved successfully.", serializer.data, status=True)
    #     except Counsellor.DoesNotExist:
    #         return api_response(400, "Counsellor Not Found", {}, status=False)

    def put(self, request):
        try:
            cons = Counsellor.objects.get(counsellor_id=request.user.id)
            user = cons.counsellor
            serializer1 = ConsUserApplicationformSerializer(user, data=request.data, partial=True)
            serializer2 = CounsellorApplicationformSerializer(cons, data=request.data, partial=True)
            if serializer1.is_valid(raise_exception=True):
                serializer1.save()
            if serializer2.is_valid(raise_exception=True):
                serializer2.save(step=2)
            else:
                return api_response(400, "Invalid data", {}, status=False)
            data = serializer1.data
            data.update(serializer2.data)
            return api_response(200, "Profile updated successfully", data, status=True)
        except Counsellor.DoesNotExist:
            return api_response(400, "Counsellor Not Found", {}, status=False)


class CounsellorUploaddoc(APIView):
    permission_classes = (IsAuthenticated,)



    # def get(self, request):
    #     try:
    #         cons = Counsellor.objects.get(counsellor_id=request.user.id)
    #         serializer = CounsellorUploaddocSerializer(cons)
    #         return api_response(200, "Counsellor profile retrieved successfully.", serializer.data, status=True)
    #     except Counsellor.DoesNotExist:
    #         return api_response(400, "Counsellor Not Found", {}, status=False)

    def put(self, request):
        try:
            cons = Counsellor.objects.get(counsellor_id=request.user.id)
            # user = tch.teacher
            serializer = CounsellorUploaddocSerializer(cons, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(step=3)
                return api_response(200, "Counsellor updated successfully", serializer.data, status=True)
            else:
                return api_response(400, "Invalid data", {}, status=False)
        except Counsellor.DoesNotExist:
            return api_response(400, "Counsellor Not Found", {}, status=False)







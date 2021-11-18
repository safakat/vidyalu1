from rest_framework.views import APIView
from core.permissions import IsStudent
from rest_framework.permissions import IsAuthenticated
from core.helpers import api_response
from counsellor.models.session_model import Session
from student.serializers.student_session_serializer import SessionDetailSerializer,OneSessionDetailSerializer
from counsellor.models.counsellors import Counsellor
from counsellor.serializers.counsellor_serializer import CounsellorSerializer

class StudentSessionallView(APIView):
    """
           student  get all the session list.
    """
    permission_classes = (IsStudent,)

    def get(self, request):
        session = Session.objects.filter(publish=True,block_by_admin=False).order_by('-created_at')
        if session:
            serializer = SessionDetailSerializer(session, many=True)
            return api_response(200, "Session retrieved successfully.", serializer.data, status=True)
        else:
            return  api_response(404,"No Session found",{},status=False)



class StudentSessionDetailsView(APIView):
    """
           student get the single session details.
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            session_id = request.data.get("id", None)
            session = Session.objects.get(id=session_id)
            if session:
                serializer = OneSessionDetailSerializer(session,context={"user_id":request.user.id})
                return api_response(200, "Session details retrieved successfully.", [serializer.data], status=True)

        except Session.DoesNotExist:
            return api_response(400, "Session Not Found", {}, status=False)



class CounsellorSessionDetailView(APIView):
    """
              student search the counsellor details and get the session from counsellor id.
    """
    # permission_classes = (IsTeacher,)

    def post(self, request):
        try:
            counsellor_id = request.data.get("id", None)
            session = Session.objects.filter(counsellor_id=counsellor_id,publish=True,block_by_admin=False)
            if session:
                serializer = SessionDetailSerializer(session, many=True)
                return api_response(200, "Session details retrieved successfully.", serializer.data, status=True)
            else:
                return api_response(200, "No Session found", [], status=True)
        except Session.DoesNotExist:
            return api_response(400, "Session Not Found", [], status=False)




# class SearchCounsellorSessionDetailsView(APIView):
#     # permission_classes = (IsStudent,)
#
#     def post(self, request):
#         try:
#             session_id = request.data.get("id", None)
#             session = Session.objects.get(id=session_id)
#             if session:
#                 serializer = OneSessionDetailSerializer(session)
#                 return api_response(200, "Session details retrieved successfully.", [serializer.data], status=True)
#
#         except Session.DoesNotExist:
#             return api_response(400, "Session Not Found", {}, status=False)
#
#
#
# class CounsellorProfileDetailView(APIView):
#     # permission_classes = (IsTeacher,)
#
#     def post(self, request):
#         try:
#             counsellor_id = request.data.get("id", None)
#             cons = Counsellor.objects.get(counsellor_id=counsellor_id)
#             if cons:
#                 serializer = CounsellorSerializer(cons)
#                 return api_response(200, "Counsellor details retrieved successfully.", serializer.data, status=True)
#
#         except Counsellor.DoesNotExist:
#             return api_response(400, "No Counsellor found", {}, status=False)




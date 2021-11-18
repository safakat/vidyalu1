from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from core.helpers import api_response
from counsellor.models.session_model import Session
from vidyalu_admin.serializers.admin_session_serializer import SessionDetailSerializer,AdminSessionBookingSerializer
from student.models.session_booking import SessionBooking
class AdminSessionDetailsView(APIView):
    """
            Admin can view all the session details.
    """
    permission_classes = (IsAdminUser,)

    def get(self, request):
        session = Session.objects.all().order_by('-created_at')
        if session:
            serializer = SessionDetailSerializer(session, many=True)
            return api_response(200, "Session retrieved successfully.", serializer.data, status=True)
        else:
            return  api_response(404,"No Session found",{},status=False)





class AdminBlockSessionView(APIView):
    """
               Admin can block by any session by using session id.
    """
    permission_classes = (IsAdminUser,)

    def put(self,request):
        try:
            session_id = request.data.get("id", None)
            session = Session.objects.get(id=session_id)
            if session.block_by_admin == False:
                session.block_by_admin = True
                session.save()
                return api_response(200, "Blocked by admin  successfully", request.data, status=True)
            elif session.block_by_admin == True:
                session.block_by_admin = False
                session.save()
                return api_response(200, "Unblocked by admin  successfully", {}, status=True)
        except Session.DoesNotExist:
            return api_response(400, "session Not Found", {}, status=False)



class AdminSessionBookingDetailView(APIView):
    """
        Admin get the details of session booking.
    """
    permission_classes = (IsAdminUser,)

    def post(self, request):
        session_id = request.data.get("id", None)
        booking_session = SessionBooking.objects.filter(session_id=session_id,is_booking=True).order_by('-purchase_at')
        # print(booking_course)
        if booking_session:
            serializer = AdminSessionBookingSerializer(booking_session, many=True)
            return api_response(200, "Admin Session booking retrieved successfully.", serializer.data, status=True)
        else:
            return api_response(200, "No Session booking found", [], status=True)






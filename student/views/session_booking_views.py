from rest_framework.views import APIView
from core.permissions import IsStudent
from core.helpers import api_response
from student.serializers.session_booking_serializer import SessionBookingSerializer,SessionBookingGetSerializer
from student.models.session_booking import SessionBooking



class StudentSessionBookingView(APIView):
    """
        student can book the session .
    """
    permission_classes = (IsStudent,)


    def post(self, request):
            user = request.user.id
            serializer = SessionBookingSerializer(data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user_id=user)
                return api_response(200, "Session booking successfully", serializer.data, status=True)
            else:
                return api_response(400, "Session booking failed", {}, status=False)


class StudentSessionBookingDetailView(APIView):
    """
       student get the details of session booking.
    """
    permission_classes = (IsStudent,)

    def get(self, request):
        booking_session = SessionBooking.objects.filter(user_id=request.user.id,is_booking=True).order_by('-purchase_at')
        if booking_session:
            serializer = SessionBookingGetSerializer(booking_session, many=True)
            return api_response(200, "Session booking retrieved successfully.", serializer.data, status=True)
        else:
            return api_response(200, "No Session booking found", [], status=True)



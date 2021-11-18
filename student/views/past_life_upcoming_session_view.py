from django.utils import timezone

from rest_framework.views import APIView


from counsellor.models.session_model import Session

from core.helpers import api_response
from core.permissions import IsStudent

from student.models.session_booking import SessionBooking
from student.serializers.past_live_upcoming_session_serializer import PastLiveUpcomingSessionSerializer


class PastLiveUpcomingSessionView(APIView):
    permission_classes = (IsStudent,)
    def get(self,request):
        user = request.user.id
        booked_session = SessionBooking.objects.filter(user_id = user,is_booking = True)
        sessions_id = booked_session.values_list("session_id")

        current_date = timezone.now().date()
        session = Session.objects.filter(id__in = sessions_id)
        past_session = session.filter(end_date__lt = current_date)
        live_session = session.filter(start_date__lte = current_date,end_date__gte = current_date)
        upcoming_session = session.filter(start_date__gt = current_date)

        booked_past_session = SessionBooking.objects.filter(user_id = user,is_booking = True, session_id__in = past_session.values_list("id"))
        booked_live_session = SessionBooking.objects.filter(user_id = user,is_booking = True, session_id__in = live_session.values_list("id"))
        booked_upcoming_session = SessionBooking.objects.filter(user_id = user,is_booking = True, session_id__in = upcoming_session.values_list("id"))
        serializer1 = PastLiveUpcomingSessionSerializer(instance=booked_past_session,many = True)
        serializer2 = PastLiveUpcomingSessionSerializer(instance=booked_live_session,many = True)
        serializer3 = PastLiveUpcomingSessionSerializer(instance=booked_upcoming_session,many = True)
        return api_response(200, "Session booking retrieved successfully.", {"current_date":current_date,"past_session":serializer1.data,"live_session":serializer2.data,"upcoming_session":serializer3.data}, status=True)

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from counsellor.serializers.session_serializers import SessionSerializer,SessionDetailSerializer,CounsellorGetSessionBookingSerializer
from counsellor.models.session_model import Session
from counsellor.models.counsellors import Counsellor
from core.helpers import api_response
from core.permissions import IsCounsellor
from student.models.session_booking import SessionBooking
from django.utils import timezone

class SessionAPIView(APIView):
    """
        counsellor create the session .
    """
    permission_classes = (IsCounsellor,)

    def post(self, request):

        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(counsellor_id=request.user.id)
            return api_response(200, "Session details saved sucessfully", serializer.data, status=True)
        else:
            return api_response(400, "Unable to save Session", serializer.errors, status=False)
    #
    # permission_classes = (IsCounsellor,)
    #
    # def post(self, request):
    #     print("1")
    #     serializer = SessionSerializer(request.data)
    #     if serializer.is_valid():
    #         serializer.save(counsellor_id=request.user.id)
    #         return api_response(200, "session details saved sucessfully", serializer.data, status=True)
    #     else:
    #         return api_response(404, "Unable to save session", serializer.errors, status=False)

class SessionDetailView(APIView):
    """
           counsellor get the session .
    """
    permission_classes = (IsCounsellor,)

    def get(self, request):
        session = Session.objects.filter(counsellor_id=request.user.id)
        if session:
            current_date = timezone.now().date()
            past_session = Session.objects.filter(counsellor_id=request.user.id,end_date__lt=current_date)
            live_session = Session.objects.filter(counsellor_id=request.user.id,start_date__lte=current_date, end_date__gte=current_date)
            upcoming_session = Session.objects.filter(counsellor_id=request.user.id, start_date__gt=current_date)
            serializer1 = SessionDetailSerializer(instance=past_session, many=True)
            serializer2 = SessionDetailSerializer(instance=live_session, many=True)
            serializer3 = SessionDetailSerializer(instance=upcoming_session, many=True)
            # serializer = SessionDetailSerializer(session, many=True)
            return api_response(200, "Session details retrieved successfully.",
                                {"past_session": serializer1.data, "live_session": serializer2.data,
                                 "upcoming_session": serializer3.data}, status=True)

            # return api_response(200, "Session details retrieved successfully.", serializer.data, status=True)
        else:
            return api_response(200, "No Session found", [], status=True)


# class SessionDetailView(APIView):
#     """
#            counsellor get the session .
#     """
#     permission_classes = (IsCounsellor,)
#
#     def get(self, request):
#         session = Session.objects.filter(counsellor_id=request.user.id)
#         if session:
#             serializer = SessionDetailSerializer(session, many=True)
#             return api_response(200, "Session details retrieved successfully.", serializer.data, status=True)
#         else:
#             return api_response(400, "No Session found", {}, status=True)


class SessionEditView(APIView):
    """
           counsellor can edit  the session .
    """
    permission_classes = (IsCounsellor,)

    def put(self,request):
        try:
            session_id = request.data.get("id", None)
            session = Session.objects.get(id=session_id)
            serializer = SessionSerializer(session, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(counsellor_id=request.user.id)
                return api_response(200, "Session Updated successfully", serializer.data, status=True)
            else:
                return api_response(400, "Invalid data", {}, status=False)
        except Session.DoesNotExist:
            return api_response(400, "Session Not Found", {}, status=False)



class PublishSessionView(APIView):
    """
           counsellor can publish and unpublish the session .
    """
    permission_classes = (IsCounsellor,)

    def put(self,request):
        try:
            session_id = request.data.get("id",None)
            session = Session.objects.get(id=session_id)
            if session.publish == False:
                session.publish = True
                session.save()
                return api_response(200, "Session will be published successfully", request.data, status=True)

            elif session.publish == True:
                session.publish = False
                session.save()
                return api_response(200, "Session will be unpublished successfully", request.data, status=True)

        except Session.DoesNotExist:
            return api_response(400, "Session Not Found", {}, status=False)




class CounsellorSessionBookingDetailView(APIView):
    """
        counsellor get the details of session booking.
    """
    permission_classes = (IsCounsellor,)

    def post(self, request):
        session_id = request.data.get("id", None)
        booking_session = SessionBooking.objects.filter(counsellor_id=request.user.id,session_id=session_id,is_booking=True).order_by('-purchase_at')
        # print(booking_course)
        if booking_session:
            serializer = CounsellorGetSessionBookingSerializer(booking_session, many=True)
            return api_response(200, "Session booking retrieved successfully.", serializer.data, status=True)
        else:
            return api_response(200, "No Session booking found", [], status=True)





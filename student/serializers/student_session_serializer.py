from rest_framework import serializers
from counsellor.models.session_model import Session
from counsellor.serializers.counsellor_serializer import CounsellorSerializer
from counsellor.models.counsellors import Counsellor
from student.models.session_booking import SessionBooking



class SessionDetailSerializer(serializers.ModelSerializer):
    """
           serializer for get all the session list.
    """
    counsellor_details = serializers.SerializerMethodField()

    class Meta:
        model = Session
        exclude = ['date_time']
        extra_fields = ["counsellor_details"]


    def get_counsellor_details(self, obj):
            try:
                cons_id = obj.counsellor.id
                cons = Counsellor.objects.get(counsellor_id=cons_id)
                serializer1 = CounsellorSerializer(cons)
                data1 = serializer1.data
                return data1
            except Counsellor.DoesNotExist:
                return None


class OneSessionDetailSerializer(serializers.ModelSerializer):
    """
           serializer for get  the single session list.
    """
    counsellor_details = serializers.SerializerMethodField()
    is_booking = serializers.SerializerMethodField()

    class Meta:
        model = Session
        exclude = ['date_time']
        extra_fields = ["counsellor_details"]


    def get_counsellor_details(self, obj):
            try:
                cons_id = obj.counsellor.id
                cons = Counsellor.objects.get(counsellor_id=cons_id)
                serializer1 = CounsellorSerializer(cons)
                data1 = serializer1.data
                return data1
            except Counsellor.DoesNotExist:
                return None

    def get_is_booking(self, obj):
        # request = self.context['request']
        try:
            user_id = self.context['user_id']
            session_id = obj.id
            if user_id == obj.counsellor.id:
                return True
            bid = SessionBooking.objects.get(user__id=user_id, session__id=session_id)
            return bid.is_booking
        except:
            return False











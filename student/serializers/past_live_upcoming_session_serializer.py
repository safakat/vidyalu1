from rest_framework import serializers

from core.serializers.auth_serializer import UserSerializer
from counsellor.serializers.session_serializers import SessionDetailSerializer
from student.models.session_booking import SessionBooking

class PastLiveUpcomingSessionSerializer(serializers.ModelSerializer):
    counsellor = UserSerializer()
    session = SessionDetailSerializer()
    class Meta:
        model = SessionBooking
        fields = '__all__'
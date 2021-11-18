from rest_framework import serializers

from video_conference.models.conference_details_model import ConferenceDetails
class GetCLassSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConferenceDetails
        fields = ('course','session','conference_url','conference_topic','conference_time','conference_password')

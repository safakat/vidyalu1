from django.db.models import fields
from rest_framework import serializers

from video_conference.models.conference_details_model import ConferenceDetails

class ConferenceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model =ConferenceDetails
        fields =('user_id','course','session','conference_url','timezone','conference_topic','conference_password','conference_time') 
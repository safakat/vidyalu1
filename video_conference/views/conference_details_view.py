import sys
from time import time
import jwt,requests,json
from django.conf import settings

from rest_framework.views import APIView

from core.helpers import api_response
from core.permissions import IsTeacherCounsellor

from video_conference.serializers.conference_details_serializer import ConferenceDetailsSerializer

class CreateConferenceURL(APIView):

    permission_classes = (IsTeacherCounsellor,)

    def generate_token(self):
        token = jwt.encode(
            # Create a payload of the token containing 
            # API Key & expiration time
            {'iss': settings.ZOOM_API_KEY, 'exp': time() + 5000},
            
            # Secret used to generate token signature
            settings.ZOOM_API_SECRET_KEY,
            
            # Specify the hashing alg
            algorithm='HS256'
        )
        return token

    def conference_details(self,topic,time,password,timezone = None):
        conference_details ={
            "topic": topic,
            "type": 2,
            "start_time": time,
            "duration": "45",
            # "timezone": "Asia/Kolkata",
            "password": password,
            "agenda": "test",
            
            "recurrence": {
                "type": 1,
                "repeat_interval": 1
                },
            
            "settings": {
                "host_video": "true",
                "participant_video": "true",
                "join_before_host": "False",
                "mute_upon_entry": "true",
                "watermark": "true",
                "audio": "voip",
                "auto_recording": "cloud"
                }
            }

        return conference_details

    def create_conference(self,token,conference_details):
        headres = {
            'authorization':'Bearer %s' % token,
            'content-type':'application/json'
        }

        r = requests.post(
            f'https://api.zoom.us/v2/users/me/meetings',
            headers=headres,data = json.dumps(conference_details)
        )

        y = json.loads(r.text)
        join_URL = y["join_url"]
        conference_password = y['password']
        conference_topic = y['topic']
        conference_time =y['start_time']

        return {
            'conference_url':join_URL,
            'conference_password':conference_password,
            'conference_topic':conference_topic,
            'conference_time':conference_time

        }

    def change_time_format(self,time):
        time = time.split('T')
        time = 'T'.join(time)

        time = time[:-1]+"Z"
        
        return time
    def post(self,request):
        data = request.data
        print(data)
        try:
            print(type(data))
            token = self.generate_token()
            time = data['conference_time']
            time = self.change_time_format(time=time)
            topic = data['conference_topic']
            password = data['conference_password']
            conference_info = self.conference_details(topic,time,password)
            conference_details_json = self.create_conference(token,conference_info)
            # data._mutable = True
            request.POST._mutable = True
            data['conference_url'] = conference_details_json['conference_url']
            data['conference_time'] = time
            # data._mutable = False
            request.POST._mutable = False
            print(data)
            serializer = ConferenceDetailsSerializer(data = data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
                # print(conference_details_json)
                return api_response(200,"Successfull", [data],status=True)
            else:
                return api_response(400,"Unable to create meeting url",{}, status=False)
        except:
            return api_response(200,str(sys.exc_info()), {'message':str(sys.exc_info())},status=True)

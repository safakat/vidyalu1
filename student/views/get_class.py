from rest_framework.views import APIView
from core.permissions import IsStudentTeacher
from core.helpers import api_response


from video_conference.models.conference_details_model import ConferenceDetails

from student.serializers.class_serializer import GetCLassSerializer

import sys

class LatestClass(APIView):
    permission_classes = (IsStudentTeacher,)

    def post(self,request):
        # user_id = request.user.id
        course_id = request.data["course_id"]
        conference_time = request.data["conference_time"]
        try:
            class_list = ConferenceDetails.objects.filter(course_id = course_id ,conference_time = conference_time)
            if class_list.count() == 0:
                return api_response(200, "No class found",[], status=True)
            else:
                next_class = class_list[0]

        except:
            return api_response(400, "No class found",[{"count":str(class_list.count()),"error":str(sys.exc_info())}], status=False)

        serializer = GetCLassSerializer(next_class)
        return api_response(200, "Class list retrived successfully",[serializer.data], status=True)


from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from core.helpers import api_response
from student.models.course_booking import CourseBooking
from teacher.serializers.student_list_serializer import StudentbookinglistSerializer
from student.serializers.teacher_list_serializer import TeacherbookinglistSerializer



class TeacherlistView(APIView):
    """
        stydent get the details of course booking teacher.
    """

    def post(self, request):
        student_id = request.data.get("id", None)
        teacher_list = CourseBooking.objects.filter(user_id=student_id,is_booking=True)
        # print(booking_course)
        if teacher_list:
            serializer = TeacherbookinglistSerializer(teacher_list, many=True)
            return api_response(200, " Student can view teacher details successfully.", serializer.data, status=True)
        else:
            return api_response(200, "No  teacher details found", [], status=True)

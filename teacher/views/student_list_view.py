

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from core.helpers import api_response
from student.models.course_booking import CourseBooking
from teacher.serializers.student_list_serializer import StudentbookinglistSerializer



class StudentlistView(APIView):
    """
        teacher get the details of course booking student.
    """

    def post(self, request):
        teacher_id = request.data.get("id", None)
        student_list = CourseBooking.objects.filter(teacher_id=teacher_id,is_booking=True)
        # print(booking_course)
        if student_list:
            serializer = StudentbookinglistSerializer(student_list, many=True)
            return api_response(200, " teacher can view student details  successfully.", serializer.data, status=True)
        else:
            return api_response(200, "No student details found", [], status=True)

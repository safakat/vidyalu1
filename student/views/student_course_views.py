from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from core.permissions import IsStudent
from core.helpers import api_response
from teacher.models.courses_model import Course
from teacher.models.teachers import Teacher
from student.serializers.student_course_serializer import CourseDetailSerializer,OneCourseDetailSerializer
from teacher.serializers.teacher_serializer import TeacherSerializer


class StudentCourseallView(APIView):
    """
               student can view all the course list.
    """
    permission_classes = (IsStudent,)

    def get(self, request):
        course = Course.objects.filter(publish=True,block_by_admin=False).order_by('-created_at')
        if course:
            serializer = CourseDetailSerializer(course, many=True)
            return api_response(200, "Course retrieved successfully.", serializer.data, status=True)
        else:
            return  api_response(404,"No Course found",{},status=False)




class StudentCourseDetailsView(APIView):
    """
            student can view single course details.
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            course_id = request.data.get("id", None)
            course = Course.objects.get(id=course_id)
            if course:
                serializer = OneCourseDetailSerializer(course, context={"user_id":request.user.id})
                return api_response(200, "Course details retrieved successfully.", [serializer.data], status=True)

        except Course.DoesNotExist:
            return api_response(400, "Course Not Found", {}, status=False)



class TeacherCourseDetailView(APIView):
    # permission_classes = (IsTeacher,)
    """
            student can seach all teacher and get course by teacher id.
    """

    def post(self, request):
        try:
            teacher_id = request.data.get("id", None)
            course = Course.objects.filter(teacher_id=teacher_id,publish=True,block_by_admin=False)
            if course:
                serializer = CourseDetailSerializer(course, many=True)
                return api_response(200, "Course details retrieved successfully.", serializer.data, status=True)
            else:
                return api_response(200, "No Course found", [], status=True)
        except Course.DoesNotExist:
            return api_response(400, "Course Not Found", [], status=False)




# class SearchTeacherCourseDetailsView(APIView):
#     # permission_classes = (IsStudent,)
#
#     def post(self, request):
#         try:
#             course_id = request.data.get("id", None)
#             course = Course.objects.get(id=course_id)
#             if course:
#                 serializer = OneCourseDetailSerializer(course)
#                 return api_response(200, "Course details retrieved successfully.", [serializer.data], status=True)
#
#         except Course.DoesNotExist:
#             return api_response(400, "Course Not Found", {}, status=False)
#
#
# class TeacherProfileDetailView(APIView):
#     # permission_classes = (IsTeacher,)
#
#     def post(self, request):
#         try:
#             teacher_id = request.data.get("id", None)
#             tch = Teacher.objects.get(teacher_id=teacher_id)
#             if tch:
#                 serializer = TeacherSerializer(tch)
#                 return api_response(200, "Teacher details retrieved successfully.", serializer.data, status=True)
#
#         except Teacher.DoesNotExist:
#             return api_response(400, "No Teacher found", {}, status=False)




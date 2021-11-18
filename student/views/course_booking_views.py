from rest_framework.views import APIView
from core.permissions import IsStudent
from core.helpers import api_response
from student.serializers.course_booking_serializer import CourseBookingSerializer,CourseBookingGetSerializer
from student.models.course_booking import CourseBooking



class StudentCourseBookingView(APIView):
    """
        student can book the course.
    """
    permission_classes = (IsStudent,)

    def post(self, request):
            user = request.user.id
            serializer = CourseBookingSerializer(data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user_id=user)
                return api_response(200, "Course booking successfully", serializer.data, status=True)
            else:
                return api_response(400, "Course booking failed", {}, status=False)


class StudentCourseBookingDetailView(APIView):
    """
        student get the details of course booking.
    """
    permission_classes = (IsStudent,)

    def get(self, request):
        booking_course = CourseBooking.objects.filter(user_id=request.user.id,is_booking=True).order_by('-purchase_at')
        # print(booking_course)
        if booking_course:
            serializer = CourseBookingGetSerializer(booking_course, many=True)
            return api_response(200, "Course booking retrieved successfully.", serializer.data, status=True)
        else:
            return api_response(200, "No Course booking found", [], status=True)

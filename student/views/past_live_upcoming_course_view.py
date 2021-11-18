from django.utils import timezone

from rest_framework.views import APIView

from teacher.models.courses_model import Course

from core.helpers import api_response
from core.permissions import IsStudent

from student.models.course_booking import CourseBooking
from student.serializers.past_live_upcoming_course_serializer import PastLiveUpcomingCourseSerializer


class PastLiveUpcomingCourseView(APIView):
    permission_classes = (IsStudent,)
    def get(self,request):
        user = request.user.id
        booked_course = CourseBooking.objects.filter(user_id = user,is_booking = True)
        courses_id = booked_course.values_list("course_id")

        current_date = timezone.now().date()
        course = Course.objects.filter(id__in = courses_id)
        past_course = course.filter(end_date__lt = current_date)
        live_course = course.filter(start_date__lte = current_date,end_date__gte = current_date)
        upcoming_course = course.filter(start_date__gt = current_date)

        booked_past_course = CourseBooking.objects.filter(user_id = user,is_booking = True, course_id__in = past_course.values_list("id"))
        booked_live_course = CourseBooking.objects.filter(user_id = user,is_booking = True, course_id__in = live_course.values_list("id"))
        booked_upcoming_course = CourseBooking.objects.filter(user_id = user,is_booking = True, course_id__in = upcoming_course.values_list("id"))
        serializer1 = PastLiveUpcomingCourseSerializer(instance=booked_past_course,many = True)
        serializer2 = PastLiveUpcomingCourseSerializer(instance=booked_live_course,many = True)
        serializer3 = PastLiveUpcomingCourseSerializer(instance=booked_upcoming_course,many = True)
        return api_response(200, "Course booking retrieved successfully.", {"past_course":serializer1.data,"live_course":serializer2.data,"upcoming_course":serializer3.data}, status=True)


    # def post(self):
    #     pass
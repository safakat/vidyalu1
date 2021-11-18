
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from teacher.serializers.course_serializers import CourseSerializer,CourseDetailSerializer,TeacherGetCourseBookingSerializer
from teacher.models.courses_model import Course
from teacher.models.teachers import Teacher
from core.helpers import api_response
from core.permissions import IsTeacher
from student.models.course_booking import CourseBooking
from django.db.models.signals import post_save
from django.utils import timezone


# def create_profile(sender, instance, *args, **kwargs):
#     print("call the function")
#     if instance.dates_times:
#         cls = CourseSchedule.objects.filter(course_id=instance.id)
#         cls.delete()
#         cls_info = instance.dates_times
#         print(cls_info)
#         for pos, cls in enumerate(cls_info):
#             pos = pos + 1
#             # print("1"),
#             cls_information = CourseSchedule.objects.create(
#                 course_id=instance.id,
#                 class_name="day" +str(pos),
#                 date=cls['class_date'],
#                 time=cls['class_time']
#             )


# post_save.connect(create_profile, sender=Course)

class CourseAPIView(APIView):
    """
        teacher can create the course.
    """

    permission_classes = (IsTeacher,)
    def post(self,request):
        print("request.data",request.data)
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(teacher_id=request.user.id)
            return api_response(200, "course details saved sucessfully", serializer.data, status=True)
        else:
            return api_response(400, "Unable to save course", serializer.errors, status=False)


class CourseDetailView(APIView):
    """
        teacher get the course details.
    """
    permission_classes = (IsTeacher,)

    def get(self, request):
        course = Course.objects.filter(teacher_id=request.user.id)
        if course:
            current_date = timezone.now().date()
            # past_course = course.filter(end_date__lt=current_date)
            # live_course = course.filter(start_date__lte=current_date, end_date__gte=current_date)
            # upcoming_course = course.filter(start_date__gt=current_date)

            past_course = Course.objects.filter(teacher_id=request.user.id,end_date__lt=current_date)
            live_course = Course.objects.filter(teacher_id=request.user.id,start_date__lte=current_date, end_date__gte=current_date)
            upcoming_course = Course.objects.filter(teacher_id=request.user.id,start_date__gt=current_date)
            serializer1 = CourseDetailSerializer(instance=past_course, many=True)
            serializer2 = CourseDetailSerializer(instance=live_course, many=True)
            serializer3 = CourseDetailSerializer(instance=upcoming_course, many=True)

            # serializer = CourseDetailSerializer(course, many=True)
            return api_response(200, "Course details retrieved successfully.",{"past_course": serializer1.data, "live_course": serializer2.data,
                                 "upcoming_course": serializer3.data}, status=True)

            # return api_response(200, "Course details retrieved successfully.", serializer.data, status=True)
        else:
            return api_response(400, "No Course found", {}, status=True)



class CourseEditView(APIView):
    """
           teacher can edit  course details.
    """
    permission_classes = (IsTeacher,)

    def put(self, request):
        print("request.data",request.data)
        try:
            course_id = request.data.get("id", None)
            course = Course.objects.get(id=course_id)
            serializer = CourseSerializer(course, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(teacher_id=request.user.id)
                return api_response(200, "Course Updated successfully", serializer.data, status=True)
            else:
                return api_response(400, "Invalid data", {}, status=False)
        except Course.DoesNotExist:
            return api_response(400, "Course Not Found", {},status=False)



class PublishCourseView(APIView):
    """
              teacher can publish and unpublish the course.
    """
    permission_classes = (IsTeacher,)

    def put(self,request):
        try:
            course_id = request.data.get("id",None)
            course = Course.objects.get(id=course_id)
            if course.publish == False:
                course.publish = True
                course.save()
                return api_response(200, "Course will be published successfully", request.data, status=True)
            elif course.publish == True:
                course.publish = False
                course.save()
                return api_response(200, "Course will be unpublished successfully", request.data, status=True)
        except Course.DoesNotExist:
            return api_response(400, "Course Not Found", {},status=False)


class TeacherCourseBookingDetailView(APIView):
    """
        teacher get the details of course booking.
    """
    permission_classes = (IsTeacher,)

    def post(self, request):
        course_id = request.data.get("id", None)
        booking_course = CourseBooking.objects.filter(course__id=course_id,is_booking=True,teacher_id=request.user.id).order_by('-purchase_at')
        # print(booking_course)
        if booking_course:
            serializer = TeacherGetCourseBookingSerializer(booking_course, many=True)
            return api_response(200, "Course booking retrieved successfully.", serializer.data, status=True)
        else:
            return api_response(200, "No Course booking found", [], status=True)


# class TeachereBookingallCourseView(APIView):
#     """
#         teacher get the details of course booking.
#     """
#     permission_classes = (IsTeacher,)
#
#     def get(self, request):
#         # course_id = request.data.get("id", None)
#         course_id = Course.objects.filter(teacher_id=request.user.id)
#         booking_course = CourseBooking.objects.filter(course_id=course_id,is_booking=True,teacher_id=request.user.id).order_by('-purchase_at')
#         # print(booking_course)
#         if booking_course:
#             serializer = TeacherGetCourseBookingSerializer(booking_course, many=True)
#             return api_response(200, "Course booking retrieved successfully.", serializer.data, status=True)
#         else:
#             return api_response(200, "No Course booking found", [], status=True)

# class TeacherAllCourseBookingDetailView(APIView):
#     """
#         teacher get the all the details of course booking.
#     """
#     permission_classes = (IsTeacher,)
#
#     def get(self, request):
#         booking_course = CourseBooking.objects.all().order_by('-purchase_at')
#         # print(booking_course)
#         if booking_course:
#             serializer = TeacherGetCourseBookingSerializer(booking_course, many=True)
#             return api_response(200, "Course booking retrieved successfully.", serializer.data, status=True)
#         else:
#             return api_response(200, "No Course booking found", [], status=True)

# class CourseDetailView(APIView):
#     def get(self, request,course_id):
#         course = Course.objects.get(id=course_id)
#         if course:
#             serializer = CourseSerializer(course)
#             return api_response(200, "Course details retrieved successfully.", serializer.data, status=True)
#         else:
#             return api_response(404, "No Course found", {}, status=False)
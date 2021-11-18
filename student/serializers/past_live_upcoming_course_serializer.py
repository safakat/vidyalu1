from rest_framework import serializers

from core.serializers.auth_serializer import UserSerializer
from teacher.serializers.course_serializers import CourseDetailSerializer

from student.models.course_booking import CourseBooking

class PastLiveUpcomingCourseSerializer(serializers.ModelSerializer):
    teacher = UserSerializer()
    course = CourseDetailSerializer()
    class Meta:
        model = CourseBooking
        fields = '__all__'
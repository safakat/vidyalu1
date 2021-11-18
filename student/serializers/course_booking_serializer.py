from rest_framework import serializers
from core.serializers.auth_serializer import UserSerializer
from student.models.course_booking import CourseBooking
from teacher.serializers.course_serializers import CourseDetailSerializer
from teacher.models.courses_model import Course
from teacher.serializers.teacher_serializer import TeacherSerializer
from teacher.models.teachers import Teacher

class CourseBookingSerializer(serializers.ModelSerializer):
    """
              serializer for student can book the course.
    """
    class Meta:
        model = CourseBooking
        # fields = ('sender','receiver','message')
        exclude = ("user",)






class CourseBookingGetSerializer(serializers.ModelSerializer):
    course = CourseDetailSerializer()
    teacher = UserSerializer()
    class Meta:
        model = CourseBooking
        fields = '__all__'


# class CourseBookingGetSerializer(serializers.ModelSerializer):
#     course = CourseDetailSerializer()
#     # teacher = UserSerializer()
#     teacher = serializers.SerializerMethodField()
#
#     class Meta:
#         model = CourseBooking
#         fields = '__all__'
#
#     def get_teacher(self, obj):
#         try:
#             tch_id=obj.teacher.id
#             tch = Teacher.objects.get(teacher_id=tch_id)
#             serializer1 = TeacherSerializer(tch)
#             data1 = serializer1.data
#             return data1
#         except Teacher.DoesNotExist:
#             return None


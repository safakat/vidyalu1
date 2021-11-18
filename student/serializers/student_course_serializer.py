from rest_framework import serializers
from teacher.models.courses_model import Course
from teacher.serializers.teacher_serializer import TeacherSerializer
from teacher.models.teachers import Teacher
from core.models.users import User
from student.models.course_booking import CourseBooking


class CourseDetailSerializer(serializers.ModelSerializer):
    """
        serializer for get all the course list.
    """
    teacher_details = serializers.SerializerMethodField()

    class Meta:
        model = Course
        exclude = ['date_time']
        extra_fields = ["teacher_details"]

    def get_teacher_details(self, obj):
        try:
            tch_id=obj.teacher.id
            tch = Teacher.objects.get(teacher_id=tch_id)
            serializer1 = TeacherSerializer(tch)
            data1 = serializer1.data
            return data1
        except Teacher.DoesNotExist:
            return None



class OneCourseDetailSerializer(serializers.ModelSerializer):
    """
           serializer for get  the single course list.
    """
    # contents = serializers.FileField(read_only=True)
    # video = serializers.FileField(read_only=True)

    teacher_details = serializers.SerializerMethodField()
    is_booking = serializers.SerializerMethodField()

    class Meta:
        model = Course
        exclude = ['date_time']
        extra_fields = ["teacher_details"]

    def get_teacher_details(self, obj):
        try:
            tch_id = obj.teacher.id
            tch = Teacher.objects.get(teacher_id=tch_id)
            serializer1 = TeacherSerializer(tch)
            data1 = serializer1.data
            return data1
        except Teacher.DoesNotExist:
            return None

    def get_is_booking(self, obj):
        try:
            user_id=self.context['user_id']
            course_id=obj.id
            if user_id==obj.teacher.id:
                return True
            bid = CourseBooking.objects.get(user__id=user_id, course__id=course_id)
            return bid.is_booking
        except:
            return  False









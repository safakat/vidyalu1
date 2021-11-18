from rest_framework import serializers
from teacher.models.courses_model import Course
from teacher.serializers.teacher_serializer import TeacherSerializer
from teacher.models.teachers import Teacher
from student.models.course_booking import CourseBooking
from teacher.models.teachers import Teacher
from teacher.serializers.teacher_serializer import TeacherSerializer
from core.models.users import User




class TeacherbookinglistSerializer(serializers.ModelSerializer):
    # course = CourseDetailSerializer()
    # student = StudentSerializer()
    teacher = serializers.SerializerMethodField()
    class Meta:
        model = CourseBooking
        fields = '__all__'

    def get_teacher(self, obj):
        try:
            tch_id = obj.teacher.id
            tch = Teacher.objects.get(teacher_id=tch_id)
            serializer1 = TeacherSerializer(tch)
            data1 = serializer1.data
            return data1
        except Teacher.DoesNotExist:
            return None


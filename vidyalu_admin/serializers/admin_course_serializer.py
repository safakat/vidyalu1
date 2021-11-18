from rest_framework import serializers
from teacher.models.courses_model import Course
from teacher.serializers.teacher_serializer import TeacherSerializer
from teacher.models.teachers import Teacher
from student.models.course_booking import CourseBooking
from student.models.students import Student
from student.serializers.student_serializer import StudentSerializer
from core.models.users import User


class CourseDetailSerializer(serializers.ModelSerializer):
    """
        serializer for all course details for admin .
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


class AdminCourseBookingSerializer(serializers.ModelSerializer):
    # course = CourseDetailSerializer()
    # student = StudentSerializer()
    student = serializers.SerializerMethodField()
    class Meta:
        model = CourseBooking
        fields = '__all__'

    def get_student(self, obj):
        try:
            stu_id = obj.user.id
            stu = Student.objects.get(student_id=stu_id)
            serializer1 = StudentSerializer(stu)
            data1 = serializer1.data
            return data1
        except Student.DoesNotExist:
            return None







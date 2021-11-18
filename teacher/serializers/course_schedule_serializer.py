from rest_framework import serializers

from teacher.models.courses_model import Course



class CourseScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id','teacher_id','title','dates_times')
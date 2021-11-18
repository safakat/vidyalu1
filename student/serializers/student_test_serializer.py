from rest_framework import serializers
from student.models.student_test_model import StudentTest
from teacher.models.teacher_test_model import Test

class StudentTestGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentTest
        fields = "__all__"




class StudentTestGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = "__all__"


# class StudentTestPostSerializer(serializers.ModelSerializer):
#     # start_date = serializers.DateField(required=False)
#     # duration = serializers.DurationField(required=False)
#     class Meta:
#         model = StudentTest
#         exclude = ["student"]
#         # fields = ('title','course','no_of_question','start_date','duration','end_date','total_marks')
#

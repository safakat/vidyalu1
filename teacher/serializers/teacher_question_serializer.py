from rest_framework import serializers

from teacher.models.teacher_question_model import Question

class TeacherQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ["teacher"]



class QuestionGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'





# class TeacherQuestionFilePostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         fields = ('question_text','option_one','option_two','option_three','option_four','correct_answer')
#

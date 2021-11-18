from django.db import models

from teacher.models.teacher_test_model import Test
from teacher.models.courses_model import Course
from core.models.users import User


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    test = models.ForeignKey(Test,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=1000,null=True,blank=True)
    option = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # score = models.IntegerField(null=True,blank=True)


    class Meta:
        db_table = "teacher_questions"
    
    def __str__(self):
        return self.question_text
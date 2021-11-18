from django.db import models
from core.models.users import User
from teacher.models.courses_model import Course
from teacher.models.teacher_test_model import Test
from teacher.models.teacher_question_model import Question


class StudentTest(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.JSONField(null=True, blank=True)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # deadline = models.DateTimeField(default=now,editable=True,null=False,blank=False)

    class Meta:
        db_table = 'student_test'

    # @property
    # def score(self):
    #     if self.question:
    #         qtn=self.question
    #         return len(list(filter(lambda ans:ans["is_correct"]==True,qtn)))

from django.db import models
from django.utils.timezone import now

from core.models.users import User
from teacher.models.courses_model import Course

TEST_TYPE_CHOICE = (('Surprise Test','Surprise Test'),('test_type_a','test_type_a'),('test_type_b','test_type_b'))

class Test(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500,default = "test subject", null=False,blank=False)
    teacher = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    no_of_question = models.CharField(max_length=200,null=False,blank=False)
    duration = models.CharField(max_length=200,null=False,blank=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    total_marks = models.IntegerField(blank=True,null=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # deadline = models.DateTimeField(default=now,editable=True,null=False,blank=False)


    class Meta:
        db_table = 'teacher_tests'
    
    def __str__(self):
        return self.title
from django.db import models
from core.models.users import User
# from teacher.models.teachers import Course


class Student(models.Model):
    STUDENT_TYPE_CHOICES = (
        ("guest", "guest"),
        ("member", "member"),
    )
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    salutation = models.BooleanField(default=False)
    qualification = models.CharField(max_length=191, null=True, blank=True)
    certification = models.CharField(max_length=191, null=True, blank=True)
    intrest = models.BooleanField(default=False)
    stu_type = models.CharField(max_length=199, choices=STUDENT_TYPE_CHOICES, blank=True, null=True)
    step = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "students"
        verbose_name = "Students"
        verbose_name_plural = "Student"



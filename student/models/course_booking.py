from django.db import models
from core.models.users import User
from teacher.models.courses_model import Course


class CourseBooking(models.Model):
    transaction_id = models.CharField(max_length=191,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='student_user',null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE,related_name='teacher_user',null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='course_obj',null=True)
    card_number = models.CharField(max_length=191,null=True,blank=True)
    cvv_number = models.PositiveIntegerField(null=True,blank=True)
    expiry_date = models.CharField(max_length=191,null=True,blank=True)
    name_on_card = models.CharField(max_length=191, null=True, blank=True)
    is_booking = models.BooleanField(default=False)
    purchase_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "course_booking"
        verbose_name = "Course_booking"
        verbose_name_plural = "Course_booking"



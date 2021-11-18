from django.db import models
from core.models.users import User


class Teacher(models.Model):
    TEACHER_TYPE_CHOICES = (
        ("guest", "guest"),
        ("member", "member"),
    )
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    edu_qualification = models.JSONField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    certificate = models.FileField(upload_to="documents/", null=True, blank=True)
    tch_information = models.JSONField(null=True, blank=True)
    competency_area = models.JSONField(null=True, blank=True)
    awards = models.CharField(max_length=191, null=True, blank=True)
    would_like_to_teach = models.CharField(max_length=191, null=True, blank=True)
    tch_resume = models.FileField(upload_to="documents/",null=True, blank=True)
    is_adharcard = models.BooleanField(default=False)
    is_pancard = models.BooleanField(default=False)
    is_passport = models.BooleanField(default=False)
    id_proof = models.FileField(upload_to="documents/", null=True, blank=True)
    fac_type = models.CharField(max_length=199, choices=TEACHER_TYPE_CHOICES, blank=True, null=True)
    step =models.PositiveIntegerField(default=0)
    search = models.CharField(max_length=199, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "teachers"
        verbose_name = "Teachers"
        verbose_name_plural = "Teacher"


    # teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    # edu_qualification = models.CharField(max_length=191, null=True, blank=True)
    # edu_startyear = models.PositiveIntegerField(null=True, blank=True)
    # edu_endyear = models.PositiveIntegerField(null=True, blank=True)
    # description = models.TextField(null=True, blank=True)
    # certificate = models.FileField(upload_to="documents/",null=True, blank=True)
    # # teaching_experience = models.CharField(max_length=191,null=True, blank=True)
    # # # tch_qualification = models.CharField(max_length=191, null=True, blank=True)
    # # # tch_startyear = models.PositiveIntegerField(null=True, blank=True)
    # # # tch_endyear = models.PositiveIntegerField(null=True, blank=True)
    # # competency_area = models.CharField(max_length=191, null=True, blank=True)
    # # awards = models.CharField(max_length=191, null=True, blank=True)
    # # would_like_to_teach = models.CharField(max_length=191, null=True, blank=True)
    # # tch_resume = models.FileField(upload_to="documents/",null=True, blank=True)
    # # is_adharcard = models.BooleanField(default=False)
    # # is_pancard = models.BooleanField(default=False)
    # # is_passport = models.BooleanField(default=False)
    # # id_proof_image = models.FileField(upload_to="documents/", null=True, blank=True)
    # # tch_type = models.CharField(max_length=199, choices=TEACHER_TYPE_CHOICES, blank=True, null=True)
    # # created_at = models.DateTimeField(auto_now_add=True)
    # # updated_at = models.DateTimeField(auto_now=True)
    #

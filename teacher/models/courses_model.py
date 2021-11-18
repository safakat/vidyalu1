from django.db import models
from core.models.users import User
from teacher.models.teachers import Teacher

COURSE_CATEGORY_CHOICES = (('information technology','Information Technology'),('graphic design','Graphic Design'),)
COURSE_SUITABLE_FOR = (('it students','It Students'),('mechanical students','Mechanical Students'),)


class Course(models.Model):
    date_time = models.DateTimeField(auto_now=True)
    teacher = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=199,null=False,blank=False,default="COURSE TITLE")
    year_of_experience = models.FloatField(null=True, blank=True)
    language = models.CharField(max_length=150, null=True, blank=True)
    price = models.PositiveIntegerField(default=0, null=True, blank=True)
    contents = models.FileField(upload_to="documents/", null=True, blank=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    total_days = models.IntegerField(null=True,blank=True)
    dates_times = models.JSONField(null=True,blank=True)
    total_hours = models.IntegerField(null=True, blank=True)
    weekly_schedule = models.CharField(max_length=150, null=True, blank=True)
    video = models.FileField(upload_to='video/', null=True, blank=True)
    salient = models.TextField(null=True,blank=True)
    block_by_admin = models.BooleanField(default=False)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "course"

    def __str__(self):
        return self.title



# class CourseSchedule(models.Model):
#     course  = models.ForeignKey(Course, on_delete=models.CASCADE)
#     class_name = models.CharField(max_length=199, null=True, blank=True)
#     date = models.DateTimeField(null=True, blank=True)
#     time = models.DateTimeField(null=True, blank=True)
#
#     class Meta:
#         db_table = "courseschedule"


# class Chapter(models.Model):
#     type_week_no = models.FloatField(null=True, blank=True)
#     course_title = models.CharField(max_length=150, null=True, blank=True)
#     course_price = models.PositiveIntegerField(default=0, null=True, blank=True)
#     description = models.CharField(max_length=5000, null=True, blank=True)
#     documents = models.FileField(upload_to="documents/", null=True, blank=True)
#
#
#     class Meta:
#         db_table = "chapter"


# def user_directory_path(instance, filename):

#     # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.id, filename)

# class Course(models.Model):
# date_time = models.DateTimeField(auto_now=True)
# teacher= models.ForeignKey(Teacher,on_delete=models.CASCADE,unique=False)
# course_name = models.CharField(max_length=500,null=False,blank=False,default="COURSE NAME")
# course_description = models.CharField(max_length=5000,null=True,blank=True)
# course_category = models.CharField(choices=COURSE_CATEGORY_CHOICES,max_length=200,null=True,blank=True)
# course_suitable_for = models.CharField(choices=COURSE_SUITABLE_FOR,max_length=200,null=True,blank=True)
# course_offering = models.CharField(max_length=250,null=True,blank=True)
# course_curriculum = models.CharField(max_length=150,null=True,blank=True)
# course_requirements = models.CharField(max_length=150,null=True,blank=True)
# course_benifits = models.CharField(max_length=150,null=True,blank=True)
# course_language = models.CharField(max_length=150,null = True,blank=True)
# course_total_time = models.FloatField(null=True,blank=True)
# course_image = models.ImageField(upload_to = 'image/', null= True, blank = True)
# course_video = models.FileField(upload_to='video/',null=True,blank=True)
# # course_slot = models.
# course_tags = models.CharField(max_length=200,null=True,blank=True)
# course_price = models.PositiveIntegerField(default=0,null=True,blank=True)
# admission_criteria = models.CharField(max_length=200,null=True,blank=True)
# average_rating = models.FloatField(null=True,blank=True)
# count_student_took_course = models.IntegerField(null=True,blank=True)
# eligibility = models.CharField(max_length=200,null=True,blank=True)
# block_by_admin = models.BooleanField(default=False)
# created_at = models.DateTimeField(auto_now_add=True)
# updated_at = models.DateTimeField(auto_now=True)

# class Meta:
#     db_table = "course"
#
# def __str__(self):
#     return self.course_name

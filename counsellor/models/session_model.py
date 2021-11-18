from django.db import models
from core.models.users import User

from counsellor.models.counsellors import Counsellor

COURSE_CATEGORY_CHOICES = (('information technology', 'Information Technology'), ('graphic design', 'Graphic Design'),)
COURSE_SUITABLE_FOR = (('it students', 'It Students'), ('mechanical students', 'Mechanical Students'),)

# def user_directory_path(instance, filename):

#     # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.id, filename)

class Session(models.Model):
    date_time = models.DateTimeField(auto_now=True)
    counsellor = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=199,null=False,blank=False,default="SESSION TITLE")
    year_of_experience = models.FloatField(null=True, blank=True)
    language = models.CharField(max_length=150, null=True, blank=True)
    price = models.PositiveIntegerField(default=0, null=True, blank=True)
    contents = models.FileField(upload_to="documents/", null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    total_days = models.IntegerField(null=True, blank=True)
    dates_times = models.JSONField(null=True, blank=True)
    total_hours = models.IntegerField(null=True, blank=True)
    weekly_schedule = models.CharField(max_length=150, null=True, blank=True)
    video = models.FileField(upload_to='video/', null=True, blank=True)
    salient = models.TextField(null=True, blank=True)
    block_by_admin = models.BooleanField(default=False)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = "session"

    def __str__(self):
        return self.title

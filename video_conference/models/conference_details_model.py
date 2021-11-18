from django.db import models

from core.models.users import User
from teacher.models.courses_model import Course
from counsellor.models.session_model import Session

import pytz

class ConferenceDetails(models.Model):

    timezone_choice = tuple(zip(pytz.all_timezones,pytz.all_timezones))

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    session = models.ForeignKey(Session,on_delete=models.CASCADE,null=True,blank=True)
    conference_url = models.CharField(max_length=250,null=False, blank=False)
    timezone = models.CharField(max_length=250, default = "Asia/Kolkata",choices=timezone_choice,null=True,blank=True)
    conference_time = models.DateTimeField(null=False,blank=False)
    conference_topic = models.CharField(max_length=250,null=False,blank=False)
    conference_password = models.CharField(max_length=8,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True,null=False,blank=False)

    def __str__(self):
        return self.conference_topic
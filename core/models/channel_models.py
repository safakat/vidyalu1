from django.db import models
from core.models.users import User

# Create your models here.

class Channel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel_name = models.CharField(max_length=250,null=False,blank=False)
    group_name = models.CharField(max_length=250,null=False,blank=False)

    def __str__(self):
        return f'{self.user} - {self.channel_name}'

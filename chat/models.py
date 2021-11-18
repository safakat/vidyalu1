from django.db import models


from chat.managers import ThreadManager

from django.conf import settings
from core.models.users import User

# Create your models here.

class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Thread(TrackingModel):
    THREAD_TYPE = (
        ('personal','Personal'),
        ('group','Group')
    )

    name = models.CharField(max_length=50,null=True,blank=True)
    thread_type = models.CharField(max_length=15,choices=THREAD_TYPE,default='group')
    users = models.ManyToManyField(User)

    objects = ThreadManager()

    def __str__(self) -> str:
        if self.thread_type == 'personal' and self.users.count() == 2:
            return f'{self.users.first()} and {self.users.last()}'
        return f'{self.name}'
    
class Message(TrackingModel):
    thread = models.ForeignKey(Thread,on_delete=models.CASCADE)
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)
    is_seen = models.BooleanField(default=False,null=False,blank=False)

    def __str__(self) -> str:
        return f'From <Thread - {self.thread}'

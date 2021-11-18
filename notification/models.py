from django.db import models

from core.models.users import User

from core.models.channel_models import Channel

from channels.layers import get_channel_layer

from asgiref.sync import async_to_sync

# Create your models here.

class Notofication(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    notification = models.CharField(max_length=250,null=False, blank=False)
    is_seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'[{self.id}] from {self.sender} to {self.receiver} -- {self.notification} -- {self.is_seen}'

    def save(self,*args, **kwargs):
        channel_layer = get_channel_layer()
        channel = Channel.objects.get(user_id = self.receiver)
        async_to_sync(channel_layer.group_send)(
            channel.group_name,{
                'type':'websocket.message',
            'text':"hello"
            }
        )
        super(Notofication, self).save(*args, **kwargs)

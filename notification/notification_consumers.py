import json
from channels.generic.websocket import AsyncConsumer

from channels.db import database_sync_to_async

from core.models.channel_models import Channel
from core.models.user_status_models import UserStatus

class NotificationConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        self.me = self.scope['user']
        print("username:",self.me)
        self.room_name = f'{self.me}-notification'

        # Join room group
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        print(self.channel_name)

        await self.store_channels(self.me, self.channel_name,self.room_name)

        await self.update_user_status(self.me,True)

        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_disconnect(self,event):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

        await self.update_user_status(self.me,False)

        await self.delete_channel(self.me)

    # Receive message from WebSocket
    async def websocket_receive(self, event):
        msg = json.dumps({
            'text':event.get('text'),
            'username':self.scope['user'].username
        })

        await self.channel_layer.group_send(
            self.room_name,
            {
            'type':'websocket.message',
            'text':msg
        })

    # Receive message from room group
    async def websocket_message(self, event):
        print(f'[{self.channel_name}] - Message sent -{event["text"]}')
        await self.send({
            'type':'websocket.send',
            'text':event.get('text')
        })

    @database_sync_to_async
    def store_channels(self,me,channel_name,group_name):
        Channel.objects.create(
            user = me,
            channel_name = channel_name,
            group_name = group_name
        )

    @database_sync_to_async
    def delete_channel(self,me):
        Channel.objects.get(user_id = me).delete()

    @database_sync_to_async
    def update_user_status(self,me,status):
        data = UserStatus.objects.filter(user = me)
        if not data:
            UserStatus.objects.create(user = me, active_status = status)
        else:
            data.update(active_status = status)

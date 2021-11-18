from django.urls import path
from chat.views import LiveChat, LiveChatAPI
urlpatterns = [
    # path('live_chat/<str:username>/', LiveChat.as_view()),
    path('live_chat_api/<str:username>/', LiveChatAPI.as_view(),name='live_chat_api'),

]
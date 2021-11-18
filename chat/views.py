from django.shortcuts import render
from django.views import View

# Create your views here.

from urllib.parse import parse_qs
from django import views
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import get_user_model
from django.shortcuts import Http404
from chat.models import Thread, Message
from django.core import serializers
# Create your views here.
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from jwt import decode as jwt_decode
from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from chat.helpers import api_response
from chat.serializers import MessageSeraializer

class LiveChatAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print('self.request.user : ',self.user)
        return Thread.objects.by_user(self.user)
    
    def get_object(self):
        other_username = self.kwargs.get("username")
        self.other_user = get_user_model().objects.get(id = other_username)
        obj = Thread.objects.get_or_create_personal_thread(self.user,self.other_user)
        Message.objects.filter(thread = obj, sender = self.other_user.id).update(is_seen = True)
        print(obj)
        if obj == None:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        # print(self.request.user.id)
        # print('self.request.user : ',self.request.id)
        print(self.user)
        context = {}
        context['me'] = self.user.username
        context['thread'] = self.get_object()
        context['user'] = self.other_user.username
        context['messages'] = self.get_object().message_set.all()
        # context['message1'] = serializers.serialize("jsonl",Message.objects.filter(thread = self.get_object()),fields=('thread','sender','text','created_at'))
        context['message1'] = Message.objects.filter(thread = self.get_object())
        # print(context)
        return context

    def get(self,request,**kwargs):
        self.user = None
        if request.user.is_authenticated:
            self.user = request.user
        else:
            try:
                token = parse_qs(request.scope["query_string"].decode("utf8"))["token"][0]
                
                try:
                # This will automatically validate the token and raise an error if token is invalid
                    UntypedToken(token)
                except (InvalidToken, TokenError) as e:
                # Token is invalid
                    print(e)
                    return None
                else:
                #  Then token is valid, decode it
                    decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                    print(decoded_data)
                # Will return a dictionary like -
                # {
                #     "token_type": "access",
                #     "exp": 1568770772,
                #     "jti": "5c15e80d65b04c20ad34d77b6703251b",
                #     "user_id": 6
                # }

                # Get the user using ID
                    self.user = get_user_model().objects.get(id=decoded_data["user_id"])
            except KeyError:
                pass
        if self.user:
            context = self.get_context_data(**kwargs)
            print(context)
            # data = serializers.serialize("json",context)
            # return data
            # return render(request, self.template_name,context = context)
            serializer = MessageSeraializer(context['message1'],many = True)
            return api_response(200,"message fetched",serializer.data,status=True)
        else:
            return redirect('/admin/login/?next='+request.path)


class LiveChat(View):

    template_name = 'chat/chat.html'

    def get_queryset(self):
        print('self.request.user : ',self.user)
        return Thread.objects.by_user(self.user)
    
    def get_object(self):
        other_username = self.kwargs.get("username")
        self.other_user = get_user_model().objects.get(id = other_username)
        obj = Thread.objects.get_or_create_personal_thread(self.user,self.other_user)
        print(obj)
        if obj == None:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        # print(self.request.user.id)
        # print('self.request.user : ',self.request.id)
        print(self.user)
        context = {}
        context['me'] = self.user
        context['thread'] = self.get_object()
        context['user'] = self.other_user
        context['messages'] = self.get_object().message_set.all()
        # print(context)
        return context

    def get(self,request,**kwargs):
        self.user = None
        if request.user.is_authenticated:
            self.user = request.user
        else:
            try:
                token = parse_qs(request.scope["query_string"].decode("utf8"))["token"][0]
                
                try:
                # This will automatically validate the token and raise an error if token is invalid
                    UntypedToken(token)
                except (InvalidToken, TokenError) as e:
                # Token is invalid
                    print(e)
                    return None
                else:
                #  Then token is valid, decode it
                    decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                    print(decoded_data)
                # Will return a dictionary like -
                # {
                #     "token_type": "access",
                #     "exp": 1568770772,
                #     "jti": "5c15e80d65b04c20ad34d77b6703251b",
                #     "user_id": 6
                # }

                # Get the user using ID
                    self.user = get_user_model().objects.get(id=decoded_data["user_id"])
            except KeyError:
                pass
        if self.user:
            context = self.get_context_data(**kwargs)
            print(context)
            # data = serializers.serialize("json",context)
            # return data
            return render(request, self.template_name,context = context)
        else:
            return redirect('/admin/login/?next='+request.path)

    def post(self, request, **kwargs):
        self.object = self.get_object()
        thread = self.get_object()
        data = request.POST
        user = request.user
        text = data.get("message")
        Message.objects.create(sender = user, thread = thread, text = text)
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context=context)

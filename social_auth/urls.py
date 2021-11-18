from django.urls import path
from social_auth.views import GoogleSocialAuthView,ChangeroleStataus

urlpatterns = [
    path("google", GoogleSocialAuthView.as_view()),
    path("role/update", ChangeroleStataus.as_view()),
]

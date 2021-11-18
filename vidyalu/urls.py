from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("api/", include("student.urls")),
    path("api/", include("teacher.urls")),
    path("api/", include("counsellor.urls")),
    path("api/", include("vidyalu_admin.urls")),
    path("api/", include("social_auth.urls")),
    path('',include('chat.urls')),
    # path('api/', include('video_conference.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Vidyalu Admin"
admin.site.site_title = "Vidyalu- A learning Platform"
admin.site.index_title = "Welcome to Vidyalu- A learning Admin Portal"


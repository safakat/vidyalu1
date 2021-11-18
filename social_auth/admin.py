from django.contrib import admin

from social_auth.models import SocialAccount
# Register your models here.

class SocialUserModelAdmin(admin.ModelAdmin):
    model = SocialAccount
    list_display = ('user', 'provider', 'auth_token','id_token', 'uid')

    def has_add_permission(self, request):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(SocialAccount,SocialUserModelAdmin)

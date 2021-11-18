from django.contrib import admin
from core.models.users import User
# Register your models here.

class UserModelAdmin(admin.ModelAdmin):
    model = User
    list_display = ('email', 'full_name','username', 'phone', 'country','role','is_active')

    def has_add_permission(self, request):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(User,UserModelAdmin)
from django.contrib.auth.models import User, Group
admin.site.unregister(Group)




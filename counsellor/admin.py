from django.contrib import admin
from counsellor.models.counsellors import Counsellor

# Register your models here.
class CounsellorModelAdmin(admin.ModelAdmin):
    model = Counsellor
    list_display = ('counsellor', 'name', 'role', 'country', 'phone','active')

    def name(self, obj):
        return obj.counsellor.username

    def role(self, obj):
        return obj.counsellor.role

    def country(self, obj):
        return obj.counsellor.country

    def phone(self, obj):
        return obj.counsellor.phone

    def active(self, obj):
        return obj.counsellor.is_active == 1

    active.boolean = True


    def has_add_permission(self, request):
        return False

    #def has_delete_permission(self, request, obj=None):
        #return False

    def has_change_permission(self, request, obj=None):
        return False
admin.site.register(Counsellor,CounsellorModelAdmin)
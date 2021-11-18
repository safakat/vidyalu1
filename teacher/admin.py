from django.contrib import admin
from teacher.models.teachers import Teacher
from core.models.users import User

# Register your models here.
class TeacherModelAdmin(admin.ModelAdmin):
    model = Teacher
    list_display = ('teacher','name','role','country','phone','active')

    def name(self, obj):
        return obj.teacher.username

    def role(self, obj):
        return obj.teacher.role

    def country(self, obj):
        return obj.teacher.country

    def phone(self, obj):
        return obj.teacher.phone

    def active(self, obj):
        return obj.teacher.is_active == 1

    active.boolean = True



    def has_add_permission(self, request):
        return False

    #def has_delete_permission(self, request, obj=None):
        #return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Teacher,TeacherModelAdmin)

from django.contrib import admin
from student.models.students import Student
from core.models.users import User

# Register your models here.
class StudentModelAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('student','name','role', 'country','phone','active')

    def name(self, obj):
        return obj.student.username

    def role(self, obj):
        return obj.student.role

    def country(self, obj):
        return obj.student.country

    def phone(self, obj):
        return obj.student.phone

    def active(self, obj):
        return obj.student.is_active == 1

    active.boolean = True





    def has_add_permission(self, request):
        return False

    #def has_delete_permission(self, request, obj=None):
        #return False

    def has_change_permission(self, request, obj=None):
        return False
admin.site.register(Student,StudentModelAdmin)


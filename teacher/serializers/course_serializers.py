from rest_framework import serializers
from teacher.models.courses_model import Course
from student.models.course_booking import CourseBooking
from student.models.students import Student
from student.serializers.student_serializer import StudentSerializer


class CourseSerializer(serializers.ModelSerializer):
    """
                 serializer for teacher create course.
    """
    contents = serializers.FileField(required=False)
    video = serializers.FileField(required=False)
    class Meta:
        model = Course
        exclude = ["teacher"]


    def get_month(self,mt):
        month = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07","Aug": "08","Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        mon = month[mt]
        # print("month value1 : ", mon)
        return mon

    def save_enddate(self, data):
        date_list = data.split(" ")
        mt = date_list[1]
        mo = self.get_month(mt)
        dt = date_list[2]
        Yr = date_list[3]
        new_list = []
        new_list.append(Yr)
        new_list.append(mo)
        new_list.append(dt)

        data = "-".join(new_list)
        print(data)

        return data

    def to_internal_value(self, data):
        data._mutable = True
        data["end_date"] = self.save_enddate(data["end_date"])
        date_list = data["start_date"].split(" ")
        mt= date_list[1]
        mo = self.get_month(mt)
        dt = date_list[2]
        Yr = date_list[3]
        new_list = []
        new_list.append(Yr)
        new_list.append(mo)
        new_list.append(dt)

        data['start_date'] = "-".join(new_list)
        print(data['start_date'])

        return super().to_internal_value(data)




class CourseDetailSerializer(serializers.ModelSerializer):
    """
            serializer for get course details.
    """
    name = serializers.CharField(source="teacher.username", read_only=True)
    class Meta:
        model = Course
        fields = "__all__"
        # exclude = ["teacher"]



class TeacherGetCourseBookingSerializer(serializers.ModelSerializer):
    # course = CourseDetailSerializer()
    # student = StudentSerializer()
    student = serializers.SerializerMethodField()
    class Meta:
        model = CourseBooking
        fields = '__all__'

    def get_student(self, obj):
        try:
            stu_id = obj.user.id
            stu = Student.objects.get(student_id=stu_id)
            serializer1 = StudentSerializer(stu)
            data1 = serializer1.data
            return data1
        except Student.DoesNotExist:
            return None







from rest_framework import serializers
from counsellor.models.session_model import Session
from counsellor.serializers.counsellor_serializer import CounsellorSerializer
from counsellor.models.counsellors import Counsellor
from student.models.students import Student
from student.serializers.student_serializer import StudentSerializer
from student.models.session_booking import SessionBooking


class SessionDetailSerializer(serializers.ModelSerializer):
    """
          serializer for all session details for admin .
      """
    counsellor_details = serializers.SerializerMethodField()

    class Meta:
        model = Session
        exclude = ['date_time']
        extra_fields = ["counsellor_details"]


    def get_counsellor_details(self, obj):
            try:
                cons_id = obj.counsellor.id
                cons = Counsellor.objects.get(counsellor_id=cons_id)
                serializer1 = CounsellorSerializer(cons)
                data1 = serializer1.data
                return data1
            except Counsellor.DoesNotExist:
                return None


class AdminSessionBookingSerializer(serializers.ModelSerializer):
    # course = SessionDetailSerializer()
    # student = StudentSerializer()
    student = serializers.SerializerMethodField()
    class Meta:
        model = SessionBooking
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










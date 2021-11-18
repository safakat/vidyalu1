from rest_framework import serializers

from student.models.session_booking import SessionBooking
from counsellor.serializers.session_serializers import SessionDetailSerializer

from core.serializers.auth_serializer import UserSerializer


class SessionBookingSerializer(serializers.ModelSerializer):
    """
              serializer for student can book the session.
    """
    class Meta:
        model = SessionBooking
        # fields = ('sender','receiver','message')
        exclude = ("user",)


    # def get_month(self,mt):
    #     month = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07","Aug": "08","Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    #     mon = month[mt]
    #     # print("month value1 : ", mon)
    #     return mon
    #
    #
    # def to_internal_value(self, data):
    #     data._mutable = True
    #     date_list = data["expiry_date"].split(" ")
    #     mt= date_list[1]
    #     mo = self.get_month(mt)
    #     dt = date_list[2]
    #     Yr = date_list[3]
    #     new_list = []
    #     new_list.append(Yr)
    #     new_list.append(mo)
    #     new_list.append(dt)
    #
    #     data['expiry_date'] = "-".join(new_list)
    #     print(data['start_date'])
    #
    #     return super().to_internal_value(data)



class SessionBookingGetSerializer(serializers.ModelSerializer):
    session = SessionDetailSerializer()
    counsellor = UserSerializer()

    class Meta:
        model = SessionBooking
        fields = '__all__'

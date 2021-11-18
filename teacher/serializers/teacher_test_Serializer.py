from rest_framework import serializers

from teacher.models.teacher_test_model import Test

class TestGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"

class TestPostSerializer(serializers.ModelSerializer):
    # start_date = serializers.DateField(required=False)
    # duration = serializers.DurationField(required=False)
    class Meta:
        model = Test
        fields = ('title','course','no_of_question','start_date','duration','end_date','total_marks')



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

    # def save_duration(self,data):
    #     date_list = data.split(" ")
    #     tm = date_list[4]
    #     # mo = self.get_month(mt)
    #     # dt = date_list[2]
    #     # Yr = date_list[3]
    #     new_list = []
    #     new_list.append(tm)
    #
    #     data = " ".join(new_list)
    #     print(data)
    #
    #     return data

    def to_internal_value(self, data):
        # data._mutable = True
        data["end_date"] = self.save_enddate(data["end_date"])
        # data["duration"] = self.save_duration(data["duration"])
        date_list = data["start_date"].split(" ")
        print("date_list",date_list)
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

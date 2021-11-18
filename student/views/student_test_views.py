from rest_framework.views import APIView
from core.permissions import IsTeacher,IsStudent
from core.helpers import api_response
from student.serializers.student_test_serializer import StudentTestGetSerializer
from teacher.models.teacher_test_model import Test
from teacher.models.teachers import Teacher



class StudentGetTestdetailView(APIView):
    permission_classes = (IsStudent,)

    def post(self,request):
        user_id = request.user.id
        course_id = request.data.get("id", None)
        # teacher_id = Teacher.objects.get(teacher_id = user_id).id
        tests = Test.objects.filter(course_id=course_id,active=True)
        if tests:
            serialized_test = StudentTestGetSerializer(tests, many = True)
            return api_response(200,"Test retrived successfully", serialized_test.data, status=True)
        else:
            return api_response(200, "No Test found", [], status=True)





# class StudentTestView(APIView):
#     permission_classes = (IsStudent,)
#
#     def post(self,request):
#         user_id = request.user.id
#         # request.POST._mutable = True
#         serialized_test = StudentTestPostSerializer(data = request.data)
#         if serialized_test.is_valid(raise_exception=True):
#             serialized_test.save(student_id=request.user.id)
#             return api_response(200,"Student Test created  successfully",serialized_test.data, status=True)
#         return api_response(400,"Student Test failed",{}, status=False)

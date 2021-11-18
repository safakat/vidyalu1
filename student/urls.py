from django.urls import path
from student.views.student_detail import StudentView,StudentBasicinformation,StudentcounsellorView
from student.views.student_course_views import StudentCourseallView,StudentCourseDetailsView,TeacherCourseDetailView
from student.views.student_session_views import StudentSessionallView,StudentSessionDetailsView,CounsellorSessionDetailView
from student.views.course_booking_views import StudentCourseBookingView,StudentCourseBookingDetailView
from student.views.session_booking_views import StudentSessionBookingView,StudentSessionBookingDetailView
from student.views.past_live_upcoming_course_view import PastLiveUpcomingCourseView
from student.views.past_life_upcoming_session_view import PastLiveUpcomingSessionView
from student.views.course_schedule_view import StudentCourseScheduleView
from student.views.get_class import LatestClass
from student.views.teacher_list_view import TeacherlistView
from student.views.student_question_views import StudentQuestionView
from student.views.student_question_views import StudentTestView
from student.views.student_test_views import StudentGetTestdetailView


urlpatterns = [
    path("student", StudentView.as_view(), name="student_profile"),
    path("student/basicinfo", StudentBasicinformation.as_view(), name="student_basicinformation"),
    path("student/counsellor", StudentcounsellorView.as_view(), name="counsellor_details"),
    path("student/courseall", StudentCourseallView.as_view(), name="course_all_details"),
    path("student/sessionall", StudentSessionallView.as_view(), name="session_all_details"),
    path("student/course/details", StudentCourseDetailsView.as_view(), name="course_details"),
    path("student/session/details", StudentSessionDetailsView.as_view(), name="session_details"),
    path("search/teacher/course", TeacherCourseDetailView.as_view(), name="teacher_course"),
    path("search/counsellor/session", CounsellorSessionDetailView.as_view(), name="counsellor_session"),
    path("student/course/booking", StudentCourseBookingView.as_view(), name="course_booking"),
    path("student/course/booking/details", StudentCourseBookingDetailView.as_view(), name="course_booking_detail"),
    path("student/session/booking", StudentSessionBookingView.as_view(), name="session_booking"),
    path("student/session/booking/details", StudentSessionBookingDetailView.as_view(), name="session_booking_detail"),
    path("student/past_live_upcoming_course",PastLiveUpcomingCourseView.as_view(), name="past_live_upcoming_course"),
    path("student/past_live_upcoming_session",PastLiveUpcomingSessionView.as_view(),name="past_live_upcoming_session"),
    path("student/get_class_list", StudentCourseScheduleView.as_view(), name="course_schedule_view"),
    path("student/get_class",LatestClass.as_view(),name="get_class"),
    path("student/get_teacher_list", TeacherlistView.as_view(), name="teacher_list_view"),
    path("student/get_question/list", StudentQuestionView.as_view(), name='get_test_question'),
    path("student/test_view", StudentTestView.as_view(), name='student_test'),
    path('student/testdetails/list', StudentGetTestdetailView.as_view(), name='student_testdetails'),

    # path("search/teacher/Profile", TeacherProfileDetailView.as_view(), name="teacher_profile"),
    # path("search/counsellor/Profile", CounsellorProfileDetailView.as_view(), name="counsellor_profile"),
    # path("search/teacher/course/details", SearchTeacherCourseDetailsView.as_view(), name="teacher_course"),
    # path("search/counsellor/session/details", SearchCounsellorSessionDetailsView.as_view(), name="counsellor_session"),

]

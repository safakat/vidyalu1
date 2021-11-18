from django.urls import path
from teacher.views.teacher_detail import TeacherView,TeacherBasicinformation,TeacherEducationalqualification,TeacherTeachinginformation
from teacher.views.course_details_view import CourseAPIView,CourseDetailView,CourseEditView,PublishCourseView,TeacherCourseBookingDetailView
from teacher.views.course_schedule_view import CourseScheduleView
from video_conference.views.conference_details_view import CreateConferenceURL
from teacher.views.student_list_view import StudentlistView
from teacher.views.teacher_test_details import TeacherCreatTestView,TeacherGetTestView,TeacherPutTestView,ActiveTestView
from teacher.views.teacher_question_details import TestQuestionAPI,TestGetQuestionAPI,TestChangeQuestionAPI,TestDeleteQuestionAPI

urlpatterns = [
    path("teacher", TeacherView.as_view(), name="teacher_profile"),
    path("teacher/basicinfo", TeacherBasicinformation.as_view(), name="teacher_basicinformation"),
    path("teacher/eduqualfi", TeacherEducationalqualification.as_view(), name="teacher_eduqulification"),
    path("teacher/teachinginfo", TeacherTeachinginformation.as_view(), name="teacher_teachingformation"),
    path("teacher/course", CourseAPIView.as_view(), name="teacher_course"),
    path("teacher/courseall", CourseDetailView.as_view(), name="course_all"),
    path("teacher/course/edit", CourseEditView.as_view(), name="course_edit"),
    path("teacher/course/publish", PublishCourseView.as_view(), name="publish_course"),
    path("teacher/course/booking/details", TeacherCourseBookingDetailView.as_view(), name="course_booking_details"),
    path("teacher/get_class_list",CourseScheduleView.as_view(),name = "course_schedule_view"),
    path('teacher/create_meeting_url',CreateConferenceURL.as_view(),name='create_meeting_url'),
    path("teacher/get_student_list", StudentlistView.as_view(), name="student_list_view"),
    path('teacher/test', TeacherCreatTestView.as_view()),
    path('teacher/testdetails', TeacherGetTestView.as_view()),
    path('teacher/change/testdetails', TeacherPutTestView.as_view()),
    path("teacher/test/active", ActiveTestView.as_view(), name="active_test"),
    path('teacher/test_question', TestQuestionAPI.as_view()),
    path('teacher/get/test_question', TestGetQuestionAPI.as_view()),
    path('teacher/change/test_question', TestChangeQuestionAPI.as_view()),
    path('teacher/delete/test_question', TestDeleteQuestionAPI.as_view()),

    # path("teacher/all/coursebooking/details", TeacherAllCourseBookingDetailView.as_view(), name="course_booking_details_all"),
    # path("teacher/course/<int:course_id>", CourseDetailView.as_view(), name="block_user_by_id"),
]

from django.urls import path
from counsellor.views.counsellor_detail import CounsellorView,CounsellorBasicinformation,CounsellorApplicationform,CounsellorUploaddoc
from counsellor.views.session_detail import SessionAPIView,SessionDetailView,SessionEditView,PublishSessionView,CounsellorSessionBookingDetailView
urlpatterns = [
    path("counsellor", CounsellorView.as_view(), name="counsellor_profile"),
    path("counsellor/basicinfo", CounsellorBasicinformation.as_view(), name="teacher_basicinformation"),
    path("counsellor/appform", CounsellorApplicationform.as_view(), name="counsellor_applicationform"),
    path("counsellor/uploaddoc", CounsellorUploaddoc.as_view(), name="counsellor_uploaddoc"),
    path("counsellor/session", SessionAPIView.as_view(), name="counsellor_session"),
    path("counsellor/sessionall", SessionDetailView.as_view(), name="session_all"),
    path("counsellor/session/edit", SessionEditView.as_view(), name="session_edit"),
    path("counsellor/session/publish", PublishSessionView.as_view(), name="publish_session"),
    path("counsellor/session/booking/details", CounsellorSessionBookingDetailView.as_view(), name="session_booking_details"),
    # path("counsellor/all/sessionbooking/details", TeacherAllCourseBookingDetailView.as_view(),name="course_booking_details_all"),
]

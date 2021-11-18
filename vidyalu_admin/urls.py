from django.urls import path
from vidyalu_admin.views.admin_views import AdminstudentView,AdminteacherView,AdmincounsellorView,BlockStudentView,BlockTeacherView,BlockCounsellorView,AdminView
from vidyalu_admin.views.admin_course_views import AdminCourseDetailsView,AdminBlockCourseView,AdminCourseBookingDetailView
from vidyalu_admin.views.admin_session_views import AdminSessionDetailsView,AdminBlockSessionView,AdminSessionBookingDetailView


urlpatterns = [
    path("admin/view", AdminView.as_view(), name="admin_profile"),
    path("admin/student", AdminstudentView.as_view(), name="student_details"),
    path("admin/teacher", AdminteacherView.as_view(), name="teacher_details"),
    path("admin/counsellor", AdmincounsellorView.as_view(), name="counsellor_details"),
    # path("admin/block/user", BlockUserView.as_view(), name="block_user_by_id"),
    path("admin/block/student/<int:user_id>", BlockStudentView.as_view(), name="block_user_by_id"),
    path("admin/block/teacher/<int:user_id>", BlockTeacherView.as_view(), name="block_user_by_id"),
    path("admin/block/counsellor/<int:user_id>", BlockCounsellorView.as_view(), name="block_user_by_id"),
    path("admin/teacher/courseall", AdminCourseDetailsView.as_view(), name="course_all"),
    path("admin/counsellor/sessionall", AdminSessionDetailsView.as_view(), name="session_all"),
    path("admin/block/course", AdminBlockCourseView.as_view(), name="block_course"),
    path("admin/block/session", AdminBlockSessionView.as_view(), name="block_session"),
    path("admin/coursebooking/details", AdminCourseBookingDetailView.as_view(), name="course_booking_details"),
    path("admin/sessionbooking/details", AdminSessionBookingDetailView.as_view(), name="session_booking_details"),

]

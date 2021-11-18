from django.urls import path
from core.views.authentication import *
# from core.views.authentication import MyTokenObtainPairView
from rest_framework_simplejwt import views as jwt_views
from core.views.admin_auth import *
# from core.views.role_update import RoleUpdateView
from core.views.search import SearchView

urlpatterns = [
    path("api/register", RegisterAPI.as_view(), name="register_user"),
    path("api/login", LoginAPIView.as_view(), name="token_pair"),
    # path("api/user/role/update", RoleUpdateView.as_view(), name="roleupdate"),
    path("api/logout", Logout.as_view(), name="user_logout"),
    # path("token", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("api/password/reset", RequestPasswordResetEmail.as_view(), name="password_reset"),
    path("api/password/reset/confirmPasswordReset", SetNewPasswordView.as_view(), name="password_reset_done"),
    path("api/password/change", UpdatePassword.as_view(), name="password_change"),
    path("email-verification", VerifyMyEmailView.as_view(), name="email_verify"),
    # path("api/states", StatesView.as_view(), name="all_states"),
    path("api/location", LocationView.as_view(), name="all_st"),
    path("api/search/list", SearchView.as_view(), name="search_list"),




    # admin urls
    path("api/admin/register", AdminRegisterView.as_view()),
    path("api/admin/login", AdminLoginAPIView.as_view(), name="admin_token"),
    path("api/admin/password/reset", AdminRequestPasswordResetEmail.as_view(), name="password_reset"),
    path("api/admin/password/reset/confirmPasswordReset", AdminSetNewPasswordView.as_view(), name="password_reset_done"),
    path("api/admin/view", AdminView.as_view(), name="admin_profile"),

    # path("admin/password/change", UpdatePassword.as_view(), name="password_change"),


]

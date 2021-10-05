from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login_page', Login_User, name="login_page"),
    path('logout_user', Logout_User, name="logout_user"),
    path('user_profile_page', User_profile, name="proofile_page"),
    path('Employee_registration', Employee_Registration, name="Employee_reg"),
    path('Employee_list_page', Employees_list_view.as_view(), name="Employee_list_page"),

    path('update_status/<int:status>/<int:id>',update_status,name='update_status'),

    path('change_password', auth_views.PasswordChangeView.as_view(), name='change_password'),
    path('password_change_done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(),
    name='password_reset_done'),
    path('password_reset_confirm/<slug:uidb64>/<slug:token>/', auth_views.PasswordResetConfirmView.as_view(),
    name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(),
    name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

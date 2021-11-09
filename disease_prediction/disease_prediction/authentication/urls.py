from django.urls import path, reverse_lazy

from django.contrib.auth import views as auth_views

from disease_prediction.authentication.views.login import CustomLoginView
from disease_prediction.authentication.views.registration import RegistrationView, StateJsonView

from .views.oauth import trackfly_oauth_callback
urlpatterns = [
    path('trackfly/callback/', trackfly_oauth_callback, name='trackfly-callback'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('forgot-password/',
         auth_views.PasswordResetView.as_view(
             template_name='authentication/forgot_password.html',
             html_email_template_name='emails/password_reset_email.html',
             email_template_name='emails/password_reset_email.html',
             subject_template_name='emails/password_reset_subject.txt',
             success_url=reverse_lazy('authentication:forgot_password_done')
         ),
         name='forgot_password'),

    path('forgot-password/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='authentication/forgot_password_done.html',
    ), name='forgot_password_done'),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('authentication:password_reset_complete'),
            template_name='authentication/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='authentication/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),

    path('state/', StateJsonView.as_view(), name='state'),
]

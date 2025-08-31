from django.urls import include, re_path, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path('', include('django_classified.urls', namespace='django_classified')),
    re_path('social/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),

    # Auth base
    path('login/', auth_views.LoginView.as_view(template_name='django_classified/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # Password reset (flow completo)
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='django_classified/password_reset_form.html',
        email_template_name='django_classified/password_reset_email.txt',
        subject_template_name='django_classified/password_reset_subject.txt',
        success_url='/password-reset/done/'
    ), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='django_classified/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='django_classified/password_reset_confirm.html',
        success_url='/reset/done/'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='django_classified/password_reset_complete.html'
    ), name='password_reset_complete'),

    # Pagina usata da social auth (se serve)
    path('email-sent/', TemplateView.as_view(template_name='django_classified/email_sent.html'), name='email_sent'),

    # Registrazione utenti (django-registration-redux, backend simple)
    path('accounts/', include('registration.backends.simple.urls')),

    # Modulo "baratto"
    path('trade/', include('trade.urls', namespace='trade')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

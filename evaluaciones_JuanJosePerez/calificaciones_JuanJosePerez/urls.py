from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.listar_calificaciones, name='listar_calificaciones'),
    path('crear/', views.crear_calificacion, name='crear_calificacion'),
    path('editar/<int:pk>/', views.editar_calificacion, name='editar_calificacion'),
    path('eliminar/<int:pk>/', views.eliminar_calificacion, name='eliminar_calificacion'),
    path('promedio-general/', views.promedio_general_view, name='promedio_general'),
    
    # Auth
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/register/', views.register, name='register'),
    
    # Recovery
    path('accounts/password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('accounts/password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('accounts/recover-username/', views.recover_username, name='recover_username'),
]

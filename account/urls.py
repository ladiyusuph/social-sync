from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy


app_name="account"

urlpatterns = [
    # path('login/', views.user_login, name = 'login'),
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    # path('logout/', auth_views.LogoutView.as_view(), name ='logout'),
    path('logout/', views.user_logout, name ='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done'),
                                                                   template_name="account/password_change_form.html"),
         name="password-change"),
     path('password-change/done/', 
          auth_views.PasswordChangeDoneView.as_view(
              template_name='account/password_change_done.html' ), 
          name='password_change_done'),
        
    #reset paswword urls
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='account/password_reset_form.html',
        email_template_name='account/password_reset_email.html',
        success_url=reverse_lazy('account:password_reset_done')),
         name = "password-reset"),
    
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='account/password_reset_done.html'
    ), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             success_url=reverse_lazy('account:password_reset_complete'),
             template_name='account/password_reset_confirm.html'), 
         name='password_reset_confirm'),
    
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='account/password_reset_complete.html'
    ), name='password_reset_complete'),
    
    path('', views.dashboard, name = "dashboard"),
    
    path('register/', views.register, name="register"),
    
    path('edit/', views.edit, name="edit"),
    
    path('users/', views.user_list, name='user_list'),
    
    # path('users/follow/', views.user_follow, name='user_follow'),
    
    path('users/follow/<int:user_id>/', views.follow_user, name='follow_user'),
    
    path('users/unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
    
    path('users/<username>/', views.user_detail, name='user_detail'),

]
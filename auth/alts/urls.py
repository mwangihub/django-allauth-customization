from django.urls import path
from . import views

app_name = "user_urls"

urlpatterns = [ 
    path('authentication/user_login/', views.UserLoginView.as_view(template_name='registration/login.html'), name="user_login"),
    path('authentication/logout/', views.UserLogoutView.as_view(), name="logout"),
    path('authentication/sign-up/', views.SignUpViewMain.as_view(), name="sign-up"), 
    path('authentication/register/', views.SignUpView.as_view(), name="register"),
    path('authentication/register/employee', views.EmployeeSignUpView.as_view(), name="register-employee"),
    path('authentication/register/cutomer', views.CustomerSignUpView.as_view(), name="register-cutomer"),
    path('authentication/reset_password_confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='reset_password_confirm'),
    path('authentication/reset-password/', views.ResetPasswordRequestView.as_view(), name="reset-password"),
    path('authentication/activate/<uidb64>/<token>/', views.confirm_account, name='activate'),
]
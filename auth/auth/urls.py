from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('user/', include('alts.urls')),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('choose-user-type/', views.ChooseUserTypeView.as_view(), name='choose-user'),
    path('staff-register/', views.StaffRegisterProcessView.as_view(), name='staff_register'),
]

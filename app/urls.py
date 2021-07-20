from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.LoginPage,name='loginpage'),
    path('index/',views.IndexPage,name="indexpage"),
    path('login/',views.Login,name="login"),
    path('logout/',views.logout,name="logout"),
    path("admin-add-hr/",views.AdminAddHR,name="adminaddhr"),
    path("add-hr/",views.Register_HR_EMP,name="addhr"),
]
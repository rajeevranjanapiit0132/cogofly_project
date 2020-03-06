from django.urls import path 

from . import views

app_name = "accounts"

urlpatterns = [

    path("login/", views.UserAuthView.as_view(), name="login"),
    path("register/", views.CreateUserView.as_view(), name="register"),
    
]
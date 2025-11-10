from django.urls import path
from . import views

urlpatterns = [
    path('userlogin', views.UserLogin, name="UserLogin"),
    # path('sendlogincode', views.SendLoginUserCode, name="SendLoginUserCode"),
]
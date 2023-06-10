from django.urls import path
from . import views

urlpatterns = [
   path("home",views.home),
   path("login",views.signin),
   path("logout",views.signout),
   path("register",views.register)
]
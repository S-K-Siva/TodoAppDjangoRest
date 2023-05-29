from django.urls import path
from . import views 
my_app = "frontend"
urlpatterns = [
    path('',views.homepage,name="home"),
]
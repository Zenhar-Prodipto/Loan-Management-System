from django.urls import path
from . import views

app_name = "deposite"

urlpatterns = [
    # dashboard
    path("", views.home, name="home"),
]
from django.urls import path
from . import views

app_name = "loan"

urlpatterns = [
    # dashboard
    path("", views.home, name="home"),
]
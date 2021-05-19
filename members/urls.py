from django.urls import path
from . import views

app_name = "members"

urlpatterns = [
    # dashboard
    path("", views.home, name="members-home"),
]
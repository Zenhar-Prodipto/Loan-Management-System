from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "dashboard"

urlpatterns = [
    # dashboard
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="dashboard/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="dashboard/logout.html"),
        name="logout",
    ),
    path("profile-update", views.profileUpdateView, name="admin-profile-update"),
]
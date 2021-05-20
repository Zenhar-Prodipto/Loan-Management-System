from django.urls import path
from . import views
from .views import (
    CreateMembersView,
    MemberHomeView,
    ReadMemberView,
    UpdateMemberView,
    DeleteMemberView,
    MemberSearchView,
)

app_name = "members"

urlpatterns = [
    # dashboard
    path("", MemberHomeView.as_view(), name="members-home"),
    path("/create", CreateMembersView.as_view(), name="members-create"),
    path(
        "/<str:member_name>/<int:member_no>",
        ReadMemberView.as_view(),
        name="members-details",
    ),
    path(
        "/update/<str:member_name>/<int:member_no>",
        UpdateMemberView.as_view(),
        name="members-update",
    ),
    path(
        "/<str:member_name>/<int:member_no>/delete",
        DeleteMemberView.as_view(),
        name="members-delete",
    ),
    path(
        "/search",
        MemberSearchView.as_view(),
        name="members-search",
    ),
]
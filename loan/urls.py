from django.urls import path
from . import views
from .views import (
    LoanHomeView,
    CreateLoanView,
    LoanDetailsView,
    ListLoanView,
    LoanCollectionCreateView,
    LoanCollectionDetailsView,
    LoanCollectionUpdateView,
)
import loan

app_name = "loan"

urlpatterns = [
    path("", LoanHomeView.as_view(), name="loan-home"),
    path("/create", CreateLoanView.as_view(), name="loan-create"),
    path(
        "/<int:loan_id>",
        LoanDetailsView.as_view(),
        name="loan-details",
    ),
    path("/list", ListLoanView.as_view(), name="loan-list"),
    path(
        "/loan-collection/create",
        LoanCollectionCreateView.as_view(),
        name="loan-collection-create",
    ),
    path(
        "collection/<int:loan_collection_id>",
        LoanCollectionDetailsView.as_view(),
        name="collection-details",
    ),
    path(
        "collection/<int:loan_collection_id>/update",
        LoanCollectionUpdateView.as_view(),
        name="collection-update",
    ),
]
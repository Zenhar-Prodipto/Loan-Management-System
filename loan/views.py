import loan
from typing import Collection
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from members.models import Memberprofile, Memberarea
from dashboard.models import Adminprofile
from .models import Loan, Loancollentionsheet
from djmoney.money import Money

from .forms import LoanForm, LoanCollectionForm, LoanCollectionUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)


# Create your views here.
class LoanHomeView(LoginRequiredMixin, ListView):
    model = Loancollentionsheet
    template_name = "loan/loan-home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["collections"] = Loancollentionsheet.objects.all()
        return context


class CreateLoanView(LoginRequiredMixin, CreateView):
    model = Loan
    template_name = "loan/loan-create.html"
    form_class = LoanForm
    success_url = "/loan"

    def form_valid(self, form):
        # form.instance.loan_approved_by = self.request.user
        return super().form_valid(form)


class LoanDetailsView(LoginRequiredMixin, DetailView):
    model = Loan
    template_name = "loan/loan-details.html"

    def get_object(self, *args, **kwargs):
        id_from_url = self.kwargs.get("loan_id")
        loan = Loan.objects.get(loan_id=id_from_url)
        return loan

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loan = self.get_object()
        context["loan"] = Loan.objects.get(loan_id=loan.loan_id)
        return context


class ListLoanView(LoginRequiredMixin, ListView):
    model = Loan
    template_name = "loan/loan-list.html"
    queryset = Loan.objects.all()
    context_object_name = "loans"


class LoanCollectionCreateView(LoginRequiredMixin, CreateView):
    model = Loancollentionsheet
    template_name = "loan/loan-collection-create.html"
    form_class = LoanCollectionForm
    success_url = "/loan"

    def form_valid(self, form):
        # form.instance.loan_approved_by = self.request.user
        return super().form_valid(form)


class LoanCollectionDetailsView(LoginRequiredMixin, DetailView):
    model = Loancollentionsheet
    template_name = "loan/loan-collection-details.html"

    def get_object(self, *args, **kwargs):
        id_from_url = self.kwargs.get("loan_collection_id")
        collection = Loancollentionsheet.objects.get(loan_collection_id=id_from_url)
        return collection

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        collection = self.get_object()
        context["collection"] = Loancollentionsheet.objects.get(
            loan_collection_id=collection.loan_collection_id
        )
        return context


class LoanCollectionUpdateView(LoginRequiredMixin, UpdateView):
    model = Loancollentionsheet
    template_name = "loan/loan-collection-update.html"

    # success_url = "/loan"

    def get_object(self, *args, **kwargs):
        id_from_url = self.kwargs.get("loan_collection_id")
        collection = Loancollentionsheet.objects.get(loan_collection_id=id_from_url)
        return collection

    def post(self, request, loan_collection_id, *args, **kwargs):
        collection = self.get_object()
        new_update = Loancollentionsheet.objects.get(
            loan_collection_id=collection.loan_collection_id
        )
        collection_form = LoanCollectionUpdateForm(request.POST, instance=new_update)
        if collection_form.is_valid():
            data = collection_form.cleaned_data
            deposite_amount = data["loan_deposite_amount"]
            withdrawal_amount = data["loan_deposite_withdrawal"]
            collection_amount = data["loan_collection_installment_amount"]

            collection = self.get_object()
            new_update = Loancollentionsheet.objects.get(
                loan_collection_id=collection.loan_collection_id
            )
            if deposite_amount > Money(0, "BDT"):
                new_update.add_loan_deposite()

            if withdrawal_amount > Money(0, "BDT"):
                new_update.loan_withdrawal_func()

            if collection_amount:
                if new_update.check_loan_collection_possibility():
                    new_update.add_loan_collection_installment_amount()
            collection_form.save()
            return render(request, "loan/loan-home.html")

    def get(self, request, loan_collection_id, *args, **kwargs):
        collection = self.get_object()
        new_update = Loancollentionsheet.objects.get(
            loan_collection_id=collection.loan_collection_id
        )
        collection_form = LoanCollectionUpdateForm(request.POST, instance=new_update)
        context = {"collection_form": collection_form}
        return render(request, "loan/loan-collection-update.html", context)

    # def form_valid(self, form):
    #     # (
    #     #     deposite_amount,
    #     #     withdrawal_amount,
    #     #     collection_amount,
    #     # ) = self.post()  # list unpacking

    #     data = form.cleaned_data
    #     deposite_amount = data["loan_deposite_amount"]
    #     withdrawal_amount = data["loan_deposite_withdrawal"]
    #     collection_amount = data["loan_collection_installment_amount"]

    #     collection = self.get_object()
    #     new_update = Loancollentionsheet.objects.get(
    #         loan_collection_id=collection.loan_collection_id
    #     )
    #     if deposite_amount > Money(0, "BDT"):
    #         new_update.add_loan_deposite()

    #     if withdrawal_amount > Money(0, "BDT"):
    #         new_update.loan_withdrawal_func()

    #     if collection_amount:
    #         if new_update.check_loan_collection_possibility():
    #             new_update.add_loan_collection_installment_amount()
    #     new_update.save()

    #     return super().form_valid(form)
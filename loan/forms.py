from django import forms
from django.db import models
from django.db.models import fields

from members.models import Memberprofile, Memberarea
from .models import Loan, Loancollentionsheet


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        exclude = ["loan_area"]


class LoanCollectionForm(forms.ModelForm):
    class Meta:
        model = Loancollentionsheet
        exclude = [
            "member",
            "loan_total_collection",
            "loan_deposite_balance",
            "loan_payable_installment_amount",
        ]


class LoanCollectionUpdateForm(forms.ModelForm):
    class Meta:
        model = Loancollentionsheet
        exclude = [
            "loan_id",
            "member",
            "loan_total_collection",
            "loan_deposite_balance",
            "loan_payable_installment_amount",
            "loan_number_of_installments",
        ]

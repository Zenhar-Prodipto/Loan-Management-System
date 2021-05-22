from django.db import models
from django.utils import timezone
from datetime import datetime, date
from djmoney.models.fields import MoneyField

# models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from members.models import Memberprofile, Memberarea
from dashboard.models import Adminprofile


class Loan(models.Model):

    LOAN_TYPE_CHOICES = (
        ("MONTHLY", "Monthly"),
        ("DAILY", "Daily"),
    )

    loan_id = models.IntegerField(primary_key=True, default=0, editable=False)
    member_no = models.ForeignKey(Memberprofile, on_delete=CASCADE)
    loan_area = models.ForeignKey(Memberarea, on_delete=CASCADE)
    loan_approved_by = models.ForeignKey(Adminprofile, on_delete=CASCADE)
    loan_passed_date = models.DateTimeField(default=timezone.now)
    loan_amount = MoneyField(max_digits=19, decimal_places=4, default_currency="TAKA")

    loan_period = models.DateTimeField(default=timezone.now)
    Loan_type = models.CharField(
        max_length=9, choices=LOAN_TYPE_CHOICES, default="MONTHLY"
    )

    def save(self, *args, **kwargs):
        if not Loan.objects.count():
            self.loan_id = 3000
        else:
            self.loan_id = Loan.objects.last().loan_id + 1

        self.loan_area = self.member_no.member_area

        super(Loan, self).save(*args, **kwargs)


class Loancollentionsheet(models.Model):
    loan_collection_id = models.IntegerField(
        primary_key=True, default=0, editable=False
    )
    loan_id = models.ForeignKey(
        Loan, on_delete=CASCADE, related_name="loan_collection_loan_id"
    )

    member = models.CharField(max_length=500)
    # member_id = models.IntegerField(default=0, max_length=10000)
    loan_deposite_amount = MoneyField(
        max_digits=19, decimal_places=4, default_currency="TAKA"
    )
    loan_deposite_withdrawal = MoneyField(
        max_digits=19, decimal_places=4, default_currency="TAKA"
    )
    loan_deposite_balance = MoneyField(
        max_digits=19, decimal_places=4, default_currency="TAKA"
    )

    loan_collection_installment_amount = MoneyField(
        max_digits=19, decimal_places=4, default_currency="TAKA"
    )
    loan_total_collection = MoneyField(
        max_digits=19, decimal_places=4, default_currency="TAKA"
    )

    loan_payable_installment_amount = MoneyField(
        max_digits=19, decimal_places=4, default_currency="TAKA"
    )

    loan_number_of_installments = models.IntegerField(max_length=100)

    def withdraw_loan_deposite(self):

        if self.loan_deposite_balance < self.loan_deposite_withdrawal:
            return "Not possible"
        new_balance = self.loan_deposite_balance - self.loan_deposite_withdrawal
        self.loan_deposite_balance = new_balance
        return {
            "new_balance": self.loan_deposite_balance,
            "withdrawal_amount": self.loan_deposite_withdrawal,
        }

    def add_loan_deposite(self):
        new_balance = self.loan_deposite_balance + self.loan_deposite_amount
        self.loan_deposite_balance = new_balance
        return self.loan_deposite_balance

    def loan_withdrawal_func(self):

        if self.loan_deposite_withdrawal > self.loan_deposite_amount:
            raise ValueError

        new_balance = self.loan_deposite_amount - self.loan_deposite_withdrawal
        self.loan_deposite_withdrawal = new_balance
        return self.loan_deposite_withdrawal

    def add_loan_collection_installment_amount(self):
        self.loan_number_of_installments += 1
        self.loan_payable_installment_amount = (
            self.loan_payable_installment_amount
            - self.loan_collection_installment_amount
        )
        self.loan_total_collection += self.loan_collection_installment_amount

    def check_loan_collection_possibility(self):
        if (
            self.loan_collection_installment_amount
            > self.loan_payable_installment_amount
        ):
            return False

    def save(self, *args, **kwargs):
        if not Loancollentionsheet.objects.count():
            self.loan_collection_id = 4000
        else:
            self.loan_collection_id = (
                Loancollentionsheet.objects.last().loan_collection_id + 1
            )

        self.member = self.loan_id.member_no.member_name

        self.loan_total_collection = self.loan_collection_installment_amount
        self.loan_deposite_balance = self.loan_deposite_amount
        self.loan_payable_installment_amount = (
            self.loan_id.loan_amount - self.loan_collection_installment_amount
        )
        super(Loancollentionsheet, self).save(*args, **kwargs)
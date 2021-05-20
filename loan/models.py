from django.db import models
from django.utils import timezone
from datetime import datetime, date
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from members.models import Memberprofile, Memberarea
from dashboard.models import Adminprofile


class Loan(models.Model):

    MONTH_CHOICES = (
        ("MONTHLY", "Monthly"),
        ("DAILY", "Daily"),
    )

    loan_id = models.IntegerField(primary_key=True, default=0, editable=False)
    member_no = models.ForeignKey(Memberprofile, on_delete=CASCADE)
    loan_area = models.ForeignKey(Memberarea, on_delete=CASCADE)
    approved_by = models.ForeignKey(Adminprofile, on_delete=CASCADE)
    loan_passed = models.DateTimeField(default=timezone.now)
    loan_amount = models.IntegerField(max_length=200)
    loan_period = models.DateTimeField(default=timezone.now)
    Loan_type = models.CharField(max_length=9, choices=MONTH_CHOICES, default="MONTHLY")

    def save(self, *args, **kwargs):
        if not Loan.objects.count():
            self.loan_id = 3000
        else:
            self.loan_id = Loan.objects.last().loan_id + 1
        super(Loan, self).save(*args, **kwargs)

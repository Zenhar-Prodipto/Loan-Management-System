from django.contrib import admin
from .models import Loan

# Register your models here.
class LoanAdmin(admin.ModelAdmin):
    readonly_fields = ("loan_id",)


admin.site.register(Loan, LoanAdmin)

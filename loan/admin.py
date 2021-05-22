from django.contrib import admin
from .models import Loan, Loancollentionsheet

# Register your models here.
class LoanAdmin(admin.ModelAdmin):
    readonly_fields = ("loan_id",)


# class LoanCollectionAdmin(admin.ModelAdmin):
#     readonly_fields = ("loan_collection_id",)


admin.site.register(Loan, LoanAdmin)
admin.site.register(Loancollentionsheet)

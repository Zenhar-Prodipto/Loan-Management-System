from django.contrib import admin
from .models import Memberarea, Memberprofile

# Register your models here.
class MemberareaAdmin(admin.ModelAdmin):
    readonly_fields = ("area_id",)


class MemberprofileAdmin(admin.ModelAdmin):
    readonly_fields = ("member_no",)


admin.site.register(Memberarea, MemberareaAdmin)
admin.site.register(Memberprofile, MemberprofileAdmin)

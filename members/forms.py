from django import forms

from .models import Memberprofile, Memberarea


class MemberProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Memberprofile
        fields = "__all__"

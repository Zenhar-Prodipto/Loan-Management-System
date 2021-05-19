from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import AdminProfile
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, AdminProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}")
            return redirect("dashboard:home")

    else:
        form = UserRegistrationForm()
    return render(request, "dashboard/signup.html", {"form": form})


@login_required
def home(request):

    context = {"profile_info": AdminProfile.objects.all()}
    return render(request, "dashboard/home.html", context)


class Home(ListView):
    template_name = "dashboard/home.html"
    model = AdminProfile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loggedInProfile = AdminProfile.objects.get(user=self.request.user)

        context["loggedInProfile"] = loggedInProfile

        return context


def profileUpdateView(request):
    if request.method == "POST":

        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = AdminProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.adminprofile
        )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"successfully updated")
            return redirect("dashboard:admin-profile-update")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = AdminProfileUpdateForm(instance=request.user.adminprofile)
    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "dashboard/update-profile.html", context)

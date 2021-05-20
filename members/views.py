from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from .models import Memberprofile, Memberarea
from dashboard.models import Adminprofile
from .forms import MemberProfileUpdateForm
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


class MemberHomeView(LoginRequiredMixin, ListView):
    model = Memberprofile
    # template_name = "members/members-home.html"
    template_name = "members/a.html"
    context_object_name = "memberProfiles"


class CreateMembersView(LoginRequiredMixin, CreateView):
    model = Memberprofile
    fields = "__all__"
    success_url = "/members"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReadMemberView(LoginRequiredMixin, DetailView):
    model = Memberprofile

    def get_object(self, *args, **kwargs):
        m_id_url = self.kwargs.get("member_no")
        member_no = Memberprofile.objects.get(member_no=m_id_url)
        return member_no

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        member_no = self.get_object()
        context["member"] = Memberprofile.objects.get(member_no=member_no.member_no)
        return context


class UpdateMemberView(UpdateView, LoginRequiredMixin):
    model = Memberprofile
    fields = "__all__"
    success_url = "/members"
    template_name = "members/memberprofile_update.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_object(self, *args, **kwargs):
        m_id_url = self.kwargs.get("member_no")
        member_no = Memberprofile.objects.get(member_no=m_id_url)
        return member_no

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        member_no = self.get_object()
        context["member"] = Memberprofile.objects.get(member_no=member_no.member_no)
        return context


class DeleteMemberView(DeleteView, LoginRequiredMixin):
    model = Memberprofile

    success_url = "/members"

    def get_object(self, queryset=None):
        return Memberprofile.objects.get(member_no=self.kwargs.get("member_no"))

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class MemberSearchView(ListView, LoginRequiredMixin):
    model = Memberprofile

    def post(self, request):
        searched = request.POST.get("member_no_from_searchbar")
        searched_id = int(searched)

        try:
            result = Memberprofile.objects.get(member_no=searched_id)
        except Memberprofile.DoesNotExist:
            result = None

        if result:
            context = {
                "member": get_object_or_404(Memberprofile, member_no=searched_id)
            }

            return render(request, "members/members_search.html", context)
        else:
            context = {"no_result": True}
            return render(request, "members/members_search.html", context)
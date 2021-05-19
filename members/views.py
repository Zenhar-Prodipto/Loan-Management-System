from django.shortcuts import render

# Create your views here.
def home(request):

    context = {"a": "test"}
    return render(request, "members/members.html", context)
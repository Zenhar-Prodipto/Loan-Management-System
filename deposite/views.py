# Create your views here.
from django.shortcuts import render

# Create your views here.
def home(request):

    context = {"a": "test"}
    return render(request, "deposite/deposite.html", context)
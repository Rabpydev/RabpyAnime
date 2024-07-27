from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from App_users.forms import ExtendedProfileForm, RegisterForm, UserProfileForm

# Create your views here.

def register(request: HttpRequest):
    #POST
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
    else:
        form = RegisterForm()

    #GET
    context = {"form": form}
    return render(request, "user/register.html", context)

@login_required
def dashboard(request: HttpRequest):
    return render(request, "user/dashboard.html")

@login_required
def profile(request: HttpRequest):
    form = UserProfileForm()
    extended_form = ExtendedProfileForm()
    context = {
        "form": form,
        "extented": extended_form
    }
    return render(request, "user/profile.html", context)
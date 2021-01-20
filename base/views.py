"""basic views."""

from django.shortcuts import render
from django.template.loader import select_template


def home(request):
    """Home page."""
    login_template = select_template(["login.html", "no_login.html"])
    return render(request, "home.html", {"login_template": login_template})

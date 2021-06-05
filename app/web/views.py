from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from .forms import ContactForm


@require_http_methods(["GET"])
def index_view(request):
    form = ContactForm()
    return render(request, "web/index.html", {"form": form})


@require_http_methods(["POST"])
def contact_view(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Contact request submitted")

    return render(request, "web/htmx/contact_form.html", {"form": form})

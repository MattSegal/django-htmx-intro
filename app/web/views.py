from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from .forms import ContactForm


@require_http_methods(["GET", "POST"])
def index_view(request):
    if request.method == "POST":
        # It's a form submission.
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact request submitted")
    else:
        # It's a regular page visit.
        form = ContactForm()

    return render(request, "web/index.html", {"form": form})

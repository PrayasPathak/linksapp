from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Link
from .forms import CreateLinkForm


# Create your views here.
def home(request):
    links = Link.objects.all()
    context = {"links": links}
    return render(request, "links/index.html", context)


def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.increase_click()
    return redirect(link.url)


def add_link(request):
    form = CreateLinkForm()
    if request.method == "POST":
        form = CreateLinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("home"))
    context = {"form": form}
    return render(request, "links/create_link.html", context)

from django.shortcuts import render, get_object_or_404, redirect
from .models import Link


# Create your views here.
def home(request):
    links = Link.objects.all()
    context = {"links": links}
    return render(request, "links/index.html", context)


def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.increase_click()
    return redirect(link.url)


# {% url 'create-link' %}

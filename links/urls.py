from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:link_slug>/", views.root_link, name="root-link"),
]

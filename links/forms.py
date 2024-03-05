from django.forms import ModelForm
from .models import Link


class CreateLinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ["name", "url", "slug", "clicks"]

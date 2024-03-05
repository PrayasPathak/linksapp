from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} | {self.clicks}"

    def increase_click(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

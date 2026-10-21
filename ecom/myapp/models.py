from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    slug = models.SlugField(unique=True, blank=True)
    stock = models.IntegerField()
    active = models.BooleanField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

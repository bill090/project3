from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=300)
    primaryCategory = models.BooleanField(default=False)
    slug = models.SlugField(max_length=300, default=slugify(title))

    def __str__(self):
        return self.title

class Product(models.Model):
    mainimage = models.ImageField(upload_to='products/', blank=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    featured = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text')
    price = models.FloatField()

    def __str__(self):
        return self.name
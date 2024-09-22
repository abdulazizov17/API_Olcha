from django.db import models

# Create your models here.

from django.db import models
from django.utils.text import slugify


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=200, null=True, blank=True, unique=True)
    image = models.ImageField(upload_to='category/%Y/%m/%d/', null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Group(BaseModel):
    name = models.CharField(max_length=200, null=True, blank=True, unique=True)
    image = models.ImageField(upload_to='category/%Y/%m/%d/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='groups')
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Group, self).save(*args, **kwargs)

class Product(BaseModel):
    name = models.CharField(max_length=200, null=True, blank=True, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='products')
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

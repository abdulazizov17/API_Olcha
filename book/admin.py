from django.contrib import admin

from book.models import Book,Category,Group,Product

# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
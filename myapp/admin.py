from django.contrib import admin
from .models import Author,Category,Blogpost, Item
# Register your models here.


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Blogpost)
# admin.site.register(Item)

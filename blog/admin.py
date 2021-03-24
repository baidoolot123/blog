from django.contrib import admin
from .models import Post 
from .models import Author, Books

# Register your models here.
admin.site.register(Post) 
admin.site.register(Author)
admin.site.register(Books)

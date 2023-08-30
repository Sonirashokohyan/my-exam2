from django.contrib import admin
from .models import BlogPost

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
  list_display = ("title", "content", "pub_date",)
  
admin.site.register(BlogPost, BlogPostAdmin)
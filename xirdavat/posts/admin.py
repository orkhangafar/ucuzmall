
from django.contrib import admin
from posts.models import Post, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter = ['created']

admin.site.register(Post,PostAdmin)
admin.site.register(Category)

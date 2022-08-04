from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe
# Register your models here.

from .models import Category, Post

admin.site.site_header = "SVDental Admin"
admin.site.site_title = "SVDental Admin site"
admin.site.index_title = "SVDental Admin"

admin.site.unregister(Group)

class PostInstanceInline(admin.TabularInline):
    model = Post
    fields=('title', 'status', 'active', )
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_on", "active")
    inlines = [PostInstanceInline]


class PostAdmin(admin.ModelAdmin):
    list_display = ('admin_photo', "title", "slug",
                    "created_on", "status", "category", "active")
    list_filter = ("created_on", "active", "status")
    search_fields = ["title", "slug"]
    readonly_fields = ('admin_photo', 'link_test',)


# register admin site 
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

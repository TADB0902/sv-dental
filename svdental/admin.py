from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe
# Register your models here.

from .models import Category, Post, Appointment

admin.site.site_header = "SVDental Admin"
admin.site.site_title = "SVDental Admin site"
admin.site.index_title = "SVDental Admin"

admin.site.unregister(Group)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_on", "active")


class PostAdmin(admin.ModelAdmin):
    list_display = ('admin_photo', "title", "slug", "created_on", "status", "category", "active")
    list_filter = ("created_on", "active", "status")
    search_fields = ["title", "slug"]
    readonly_fields = ('admin_photo', 'link_test',)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("customerName", "email", "phoneNumber", "created_on", "active")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Appointment, AppointmentAdmin)

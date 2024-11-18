from django.contrib import admin
from .models import Course
from django.utils.html import format_html

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'platform_name', 'price', 'image_preview')  # Add image preview
    search_fields = ('title', 'platform_name')
    list_filter = ('platform_name',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="50" height="50">')
        return "No Image"
    image_preview.short_description = 'Image Preview'

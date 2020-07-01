from django.contrib import admin
from .models import Course


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'created_at', 'updated_at', 'user', 'status']
    list_filter = ['created_at']
    search_fields = ['title']


admin.site.register(Course, CourseAdmin)

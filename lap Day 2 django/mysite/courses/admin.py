from django.contrib import admin

# Register your models here.

from .models import Course, Student

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # columns in list view
    search_fields = ('name', 'description')  # enable searching courses

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'course')
    search_fields = ('name', 'email', 'course__name')  # search across related course name
    list_filter = ('course',)  # optional: filter by course on right side

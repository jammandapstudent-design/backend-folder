from django.contrib import admin
from .models import Student

# This tells the Admin Panel: "Please show the Student table"
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # This controls which columns you see in the list
    list_display = ('student_number', 'last_name', 'first_name', 'course', 'year_level')
    # This adds a search bar for last name and student number
    search_fields = ('last_name', 'student_number')
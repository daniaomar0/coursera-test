from django.contrib import admin
import nested_admin  
from .models import Course, Section, Lecture


class LectureInlineAdmin(nested_admin.NestedTabularInline):
    model = Lecture
    extra = 1  

class SectionInLineAdmin(nested_admin.NestedTabularInline):
    model = Section
    extra = 1  
    inlines = [LectureInlineAdmin]  


class CourseAdmin(nested_admin.NestedModelAdmin):
    inlines = [SectionInLineAdmin]  


admin.site.register(Course, CourseAdmin)



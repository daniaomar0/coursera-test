from django.db import models
from django.conf import settings
from django.db.models import Q
import uuid


class CoursesQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = (
            Q(title__icontains=query) | 
            Q(field__icontains=query) |
            Q(instructor__icontains=query)
        )
        return self.filter(lookups) 


class CourseManager(models.Manager):
    def get_queryset(self):
        return CoursesQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


FIELDS = [
    ('build_apps', 'Build applications'),
    ('data_analysis', 'Data Analysis'),
    ('automate_tasks', 'Automate tasks'),
    ('secure_systems', 'Secure systems'),
    ('develop_websites', 'Develop websites'),
    ('learn_programming', 'Learn programming languages'),
    ('manage_projects', 'Manage IT projects'),
    ('transition_careers', 'Transition to an IT career'),
    ('other', 'Other'),
]


class Course(models.Model):
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    prerequisites = models.TextField(blank=True)
    field = models.CharField(max_length=255, choices=FIELDS)
    associates = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="course_associates", blank=True, null=True)
    image = models.ImageField(upload_to='courses_images' ,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True) #to check where the instructor wants to hide this course or not
    objects = CourseManager()

    def __str__(self):
        return self.title



class Section(models.Model):
    course = models.ForeignKey(Course, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
   


class Lecture(models.Model):
    section = models.ForeignKey(Section, related_name='lectures', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=50, choices=[('article', 'Article'), ('video', 'Video')])
    content = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)





class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')
        
    def __str__(self):
        def __str__(self):
            return f"{self.user.first_name} - {self.course.title}"
    
    
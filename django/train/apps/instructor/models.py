from django.conf import settings
from django.db import models

class InstructorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='instructor_profile')
    is_instructor = models.BooleanField(default=False)
    first_time_login = models.BooleanField(default=True)

EXP_CHOICES=[
            ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('experienced', 'Experienced'),
        ]

EDU_CHOICES=[
    ('phd', 'Ph.D.'),
    ('masters', 'Master’s'),
    ('bachelors', 'Bachelor’s'),
    ('associate', 'Associate’s'),
    ('diploma', 'Diploma'),
]

SPECIALIZATION_CHOICES = [
    ('computer_science', 'Computer Science'),
    ('mathematics', 'Mathematics'),
    ('physics', 'Physics'),
    ('chemistry', 'Chemistry'),
    ('engineering', 'Engineering'),
    # Add other specializations here
]

class InstructorModel(models.Model):
    education_level = models.CharField(max_length=100,choices=EDU_CHOICES)
    specialization = models.CharField(max_length=100,choices=SPECIALIZATION_CHOICES)
    experience = models.CharField(max_length=100,choices=EXP_CHOICES)
    
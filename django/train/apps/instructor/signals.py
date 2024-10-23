from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import InstructorProfile

@receiver(post_save, sender=User)
def create_instructor_profile(sender, instance, created, **kwargs):
    if created and instance.profile.is_instructor:  # Create only for instructors
        InstructorProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_instructor_profile(sender, instance, **kwargs):
    if hasattr(instance, 'instructor_profile'):
        instance.instructor_profile.save()
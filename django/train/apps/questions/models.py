from django.db import models

class Step1(models.Model):
    bg_choices = [
        ('none', 'No prior knowledge'),
        ('basic', 'Basic understanding of computers'),
        ('intermediate', 'Intermediate knowledge (e.g., programming basics)'),
        ('advanced', 'Advanced knowledge (e.g., software development, networking)'),
    ]
    
    speciality = [
        ('it', 'Information Technology'),
        ('engineering', 'Engineering'),
        ('science', 'Science (e.g., Physics, Chemistry)'),
        ('mathematics', 'Mathematics'),
        ('business', 'Business/Management'),
        ('arts', 'Arts/Humanities'),
        ('education', 'Education'),
        ('healthcare', 'Healthcare/Medicine'),
        ('law', 'Law'),
        ('social_sciences', 'Social Sciences'),
        ('high_school', 'High School Student'),
        ('other', 'Other'),
    ]
    
    learn_target = [
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

    background_knowledge = models.CharField(max_length=100, choices=bg_choices)
    speciality_target = models.CharField(max_length=100, choices=speciality)
    learn_target = models.CharField(max_length=100, choices=learn_target)

class Step2(models.Model):
    current_level = models.CharField(max_length=100, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    age = models.IntegerField()
    tell_us_about_yourself = models.CharField(max_length=200)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InstructorForm,InstructorSignUpForm,loginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import InstructorProfile
from apps.courses.models import Course



def get_initials(user):
    first_initial = user.first_name[0].upper() if user.first_name else ''
    last_initial = user.last_name[0].upper() if user.last_name else ''
    return f"{first_initial}{last_initial}"




def instructorHome(request):
    user = request.user
    initials = ''
    email = ''

    if user.is_authenticated:
        initials = get_initials(user)
        email = user.email 

    return render(request, 'instructor/instructor_home.html', {'initials': initials, 'email': email, 'user': user})


@login_required
def instructorForm(request):
    profile = request.user.instructor_profile
    if not profile.is_instructor or not profile.first_time_login:
        return redirect('instructor_home')

    if request.method == 'POST':
        form = InstructorForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            #mark that the instructor has completed the first-time form
            profile.first_time_login = False
            profile.save()
            return redirect('instructor_home')  
    else:
        form = InstructorForm(instance=profile)
    
    return render(request, 'instructor/instructor_form.html', {'form': form})



def instructor_signup_view(request):
    if request.method == 'POST':
        form = InstructorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('instructor_home')  
    else:
        form = InstructorSignUpForm()
    
    return render(request, 'registration/instructor_signup.html', {'form': form})

def instructor_login_view(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('instructor_home')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = loginForm()
        
    return render(request, 'registration/instructor_login.html', {'form': form})


@login_required(login_url='/instructor/inst_login/')
def teach_button_view(request):
    try:
        instructor_profile = request.user.instructor_profile
    except InstructorProfile.DoesNotExist:
        instructor_profile = InstructorProfile.objects.create(user=request.user, is_instructor=True)

    if instructor_profile.first_time_login:
        return redirect('instructor_form')
    else:
        return redirect('instructor_home')
    
    

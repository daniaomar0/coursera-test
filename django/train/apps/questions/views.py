from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import Step1Form, Step2Form
from django.contrib.auth.decorators import login_required
from apps.userProfile.models import Profile



@login_required
def recommendations(request):
    # Ensure the profile exists
    profile, created = Profile.objects.get_or_create(user=request.user)

    # Redirect if the user is not a first-time login
    if not profile.first_time_login:
        return redirect('home')

    if request.method == 'POST':
        # When the "next" button is clicked, process the first step form
        if 'next' in request.POST:
            step1_form = Step1Form(request.POST)
            step2_form = Step2Form()  # Initialize Step 2 form for next view

            if step1_form.is_valid():
                # Save data from Step 1 in session
                request.session['step1'] = step1_form.cleaned_data
        else:
            # Process Step 2 form on subsequent submit
            step1_form = Step1Form()
            step2_form = Step2Form(request.POST)

            if step2_form.is_valid():
                # Mark first-time login as False and save the profile
                profile.first_time_login = False
                profile.save()
                return redirect('home')
    else:
        # Initialize both forms when the user accesses the page
        step1_form = Step1Form()
        step2_form = Step2Form()

    return render(request, 'questions/recommendations.html', {
        'step1_form': step1_form,
        'step2_form': step2_form,
        'username': request.user.first_name
    })

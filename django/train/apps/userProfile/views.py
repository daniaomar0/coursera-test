from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,update_session_auth_hash
from django.contrib import messages
from .forms import UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from apps.courses.models import Course

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password_reset_done')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profile/password_reset.html', {
        'form': form
    })
    
    
@login_required
def settings(request):
    # Ensure the user has a profile
    if not hasattr(request.user, 'user_profile'):
        Profile.objects.create(user=request.user)
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.user_profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('settings')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.user_profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile/settings.html', context)



def search(request):
    query = request.GET.get('q')
    search_results = Course.objects.filter(title__icontains=query) if query else Course.objects.none()
    
    context = {
        'query': query,
        'search_results': search_results,
    }
    return render(request, 'base/search.html', context)


def get_initials(user):
    first_initial = user.first_name[0].upper() if user.first_name else ''
    last_initial = user.last_name[0].upper() if user.last_name else ''
    return f"{first_initial}{last_initial}"

def home(request):
    user = request.user
    initials = ''
    email = ''

    if user.is_authenticated:
        initials = get_initials(user)
        email = user.email  # Only get the email if the user is authenticated

    return render(request, 'base/index.html', {'initials': initials, 'email': email, 'user': user})



def account(request):
    return render(request, 'profile/account.html')


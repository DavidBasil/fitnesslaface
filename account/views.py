from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from blog.models import Post


@login_required
def dashboard(request):
    """Displays user's dashboard"""
    posts = Post.objects.filter(author=request.user)
    return render(request, 'account/dashboard.html', {'section': 'dashboard',
                  'posts': posts})


def register(request):
    """Registers a new user"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # create new user profile
            profile = Profile.objects.create(user=new_user) 
            return render(request, 
                          'account/register_done.html',
                          {'new_user': new_user})
    else: 
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit(request):
    """Allows to edit user/profile info"""
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated.')
        else:
            messages.error(request, 'Error updating your profile.')
    else: 
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form,
                                                'profile_form': profile_form})











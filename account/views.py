from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import (LoginForm, UserRegistrationForm,
                    UserEditForm, ProfileEditForm)
from django.contrib.auth.models import auth
from .models import Profile, Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect
from actions.models import Action
from actions.utils import create_action
from images.models import Image


def user_login(request):
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, 
                                username=cd["username"], 
                                password=cd["password"])
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return HttpResponse("Authenticated successfully")
                    return redirect("account:dashboard")
                else:
                    print("Disabled account")
            else:
                print("Invalid login")
    else:
        form = LoginForm()
    context = {'form':form}
    return render(request, "account/login.html", context=context)


@login_required
def dashboard(request):
    following_users = request.user.following.all()
    following_user_ids = following_users.values_list('id', flat=True)
    
    # Fetch actions by following users
    following_actions = Action.objects.filter(user__in=following_user_ids)
    
    # Fetch images by following users
    following_images = Image.objects.filter(user__in=following_user_ids)
    
    # Combine actions and images to display in the feed
    feed_items = list(following_actions) + list(following_images)
    
    # Sort feed items by date created
    feed_items.sort(key=lambda x: x.created, reverse=True)
    
    return render(request, 
                  'account/dashboard.html',
                  {'section':'dashboard',
                   'actions': feed_items})
    
    
@login_required(login_url='account:login')
def user_logout(request):
    auth.logout(request)
    
    # messages.success(request, 'You have been logged out')
    # return redirect("account:dashboard")
    return render(request, 'registration/logged_out.html')

def register(request):
    user_form = UserRegistrationForm()
    
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data["password"])
            new_user.save()
            
            Profile.objects.create(user=new_user)
            create_action(new_user, 'has created an account')
            # Redirect to the new template on successful creation
            return render(request, 
                          'account/register_done.html', 
                          {'new_user': new_user})
    
    context = {'user_form': user_form}
    
    return render(request, 
                  'account/register.html', 
                  context=context)
    
    
@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated Successfully')
            return redirect('account:dashboard')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
            instance=request.user.profile)
    
    context = {'user_form': user_form,
               'profile_form': profile_form}
    
    return render(request,
          'account/edit.html',
                  context=context)
    
    
@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request,
                  'account/user/list.html',
                  {'section': 'people',
                   'users': users})
    
    
@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    is_following = Contact.objects.filter(user_from=request.user, user_to=user).exists()
    
    return render(request, 'account/user/detail.html', {'section': 'people', 'user': user, 'is_following': is_following})
    
    
 



def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if not request.user.rel_from_set.filter(user_to=user_to_follow).exists():
        Contact.objects.create(user_from=request.user, user_to=user_to_follow)
        create_action(request.user, 'is following', user_to_follow)
    return redirect('account:user_detail', username=user_to_follow.username)



def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    request.user.rel_from_set.filter(user_to=user_to_unfollow).delete()
    
    return redirect('account:user_detail', username=user_to_unfollow.username)



# @require_POST
# @login_required
# def user_follow(request):
#     user_id = request.POST.get('id')
#     action = request.POST.get('action')
    
#     if user_id and action:
#         try:
#             user = User.objects.get(id=user_id)
#             if action == 'follow':
#                 Contact.objects.get_or_create(
#                     user_from=request.user,
#                     user_to=user)
#             else:
#                 Contact.objects.filter(
#                     user_from=request.user,
#                     user_to=user).delete()
#             return JsonResponse({'status':'ok'})
#         except User.DoesNotExist:
#             return JsonResponse({'status':'error'})
    

    
    
    
    
    
    
    
    
    
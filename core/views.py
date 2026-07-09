from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post, Comment, Profile
from django.contrib.auth.models import User

@login_required
@login_required
def home_feed(name_request):
    # Temporary test change: Fetch absolutely ALL posts from everyone
    posts = Post.objects.all().order_by('-created_at')
    return render(name_request, 'feed.html', {'posts': posts})

@login_required
def toggle_like(name_request, post_id):
    if name_request.method == "POST":
        post = get_object_or_404(Post, id=post_id)
        if name_request.user in post.likes.all():
            post.likes.remove(name_request.user)
            liked = False
        else:
            post.likes.add(name_request.user)
            liked = True
        return JsonResponse({'liked': liked, 'likes_count': post.total_likes()})

@login_required
def toggle_follow(name_request, profile_id):
    if name_request.method == "POST":
        target_profile = get_object_or_404(Profile, id=profile_id)
        user_profile = name_request.user.profile
        
        if target_profile in user_profile.following.all():
            user_profile.following.remove(target_profile)
            following = False
        else:
            user_profile.following.add(target_profile)
            following = True
        return JsonResponse({'following': following, 'followers_count': target_profile.followers.count()})
    
@login_required
def profiles_list(name_request):
    # Fetch all profiles except the logged-in user
    all_profiles = Profile.objects.exclude(user=name_request.user)
    return render(name_request, 'profiles.html', {'profiles': all_profiles})

@login_required
def user_profile_view(name_request, username):
    # Find the target user by username
    target_user = get_object_or_404(User, username=username)
    target_profile = target_user.profile
    # Fetch only the posts written by this specific user
    user_posts = Post.objects.filter(author=target_user).order_by('-created_at')
    
    return render(name_request, 'user_profile.html', {
        'target_user': target_user,
        'target_profile': target_profile,
        'posts': user_posts
    })
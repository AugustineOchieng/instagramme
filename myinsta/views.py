from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Comments
from .forms import NewCommentForm, NewPostForm, NewProfileForm
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

# def home(request):
#   images = Image.objects.all()
#   profiles = Profile.objects.all()
#   comments = Comments.objects.all()
#   return render(request, 'instahome.html', {"images": images, "profiles":profiles, "comments":comments})
@login_required(login_url='/accounts/login/')
def feeds(request):
    images = Image.objects.all()
    profiles = Profile.objects.all()
    comments = Comments.objects.all()
    current_user = request.user
    # image = Image.get_images()
    user_pic = Profile.objects.filter(user_id = current_user.id)
    title = "posts"
    
    return render(request, 'instahome.html', {"title":title,"images": images, "user_pic":user_pic, "profiles":profiles,"current_user":current_user, "comments":comments})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = current_user
            post.poster_id = current_user.id
            post.save()
        return redirect('instahomepage')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

def comments(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.profile = current_user
            comment.save()
        return redirect('allImages')
    else:
        form = NewCommentForm()
    return redirect(request, 'comments.html',{"form": form})

def image(request,image_id):
    try:
        images = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,'image.html',{'images':images})

def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.userId = request.user.id
            profile.save()
        return redirect('NewProfile')

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})

def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        user = Profile.objects.get(user=request.user)
        form = NewProfileForm(request.POST, request.FILES, instance=user)
        profile = Profile.objects.filter(user_id =current_user.id)
        if form.is_valid():
            form.save()
        return redirect('instahomepage')
    else:
        form = NewProfileForm()
    return render(request,'edit_profile.html',{'form':form})

def profile(request):
    current_user = request.user
    images = Image.objects.filter(profile = current_user)

    try:
        profiles = Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile.html',{ 'profiles':profiles,'images':images,'current_user':current_user})


def search_results(request):

     if 'profile' in request.GET and request.GET ["profile"]:
         search_term = request.GET.get("profile")
         searched_profiles = Profile.search_by_username(search_term)
         message = f"{search_term}"

         return render(request, 'search.html', {"message":message, "profiles":searched_profiles})
     else:
         message = "You haven't seached for any users yet!"
         return render(request, 'search.html',{"message": message})

# def find_profile(request,profile_id):
#     profile_id
#     try :
#         profile = Profile.objects.get(user_id = profile_id)
#         image = Image.objects.filter(profile_id = profile_id)

#     except ObjectDoesNotExist:
        
#         raise Http404()

#     return render(request, 'find_profile.html', {'profile':profile, "image":image, "poster_id":profile_id})

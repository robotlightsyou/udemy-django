from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            print('looking for profile pic')
            # print(request.FILES.getlist())
            print(request.FILES.dict())

            # if 'profile_pic' in request.FILES:
            #     profile.profile_pic = request.FILES['profile_pic'] 
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

           
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    
    else:
        user_form = UserForm
        profile_form = UserProfileInfoForm
    context_dict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    return render(request, 'basicapp/register.html', context_dict)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("someone tried to login and failed")
            print(username)
            return HttpResponse("Invalid login details")
    else:
        return render(request, 'basicapp/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# def login(request):
#     return render(request, 'basicapp/login.html')


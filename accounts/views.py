from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request,'accounts/signup_page.html', {'error':'Username is Taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password = request.POST['password1'], first_name= request.POST['first_name'], last_name=request.POST['last_name'])
                auth.login(request,user)
                return redirect('add_profile')
        else:
            return render(request,'accounts/signup_page.html',{'error':'Password must match'})
    else:
        return render(request, 'accounts/signup_page.html')


def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login_page.html',{'error':'UserName or Password is incorrect'})
    else:
        return render(request, 'accounts/login_page.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('login')

@login_required
def add_profile(request):
    user = request.user
    if request.method == "POST":
        form = UserProfileForm(request.POST,request.FILES)
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.user= user
            userprofile.save()
            return redirect('home')
    else:
        form=UserProfileForm()
        return render(request, 'accounts/add_profile_form.html', {'form':form})

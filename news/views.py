from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse






def index(request):
    content = {
        'title':'Home',
        'sliderData': Slider.objects.all(),
        'Photographdata':Photographpf.objects.all().order_by('-pk')#sabai nadekhaune kasari ho ?
    }
    return render(request,'pages/home/home-view.html',content)
def slider(request,id):
    data = {
        'sliderdata': Slider.objects.get(pk=id)
    }
    return render(request,'pages/slider/slider-view.html',data)



def photograph(request,id):
    content={
        'photodata': Photographpf.objects.get(pk=id)
    }
    return render(request,'pages/Photographpf/photograph-view.html',content)
def cosmology(request):
    cosmo={
        'lambda': Product.objects.all,
        'lamb': Product.title

    }
    return render(request,'pages/cosmology/cosmology.html',cosmo)

def biomedical(request):
    return render(request,'pages/biomedical/biomedical.html')
def technology(request):
    return render(request,'pages/technology/technology.html')












def about(request):
    return render(request,'pages/about/about-view.html')


def contact(request):
    return render(request,'pages/contact/contact-view.html')


def product_details(request,slug):
    content={
        'productDetailsData':Product.objects.filter(slug=slug)
    }
    return render(request,'pages/product/product-details-view.html',content)


def user_register(request):
    if request.method=='POST':
        data=UserCreationForm(request.POST)
        if data.is_valid():
            data.save()
            messages.success(request,'User was successfully registered') #you are successfully registered (registered name dekhauna k garne ho ?)
            return redirect('register')
        else:
            messages.success(request,'PLEASE CHECK THE DATA YOU ENTERED')
            redirect('register')

    else:
        content={
            'userRegister': UserCreationForm

        }
        return render(request,'pages/login/register-view.html',content)


def user_login(request):
    if request.method=='POST':
        data=AuthenticationForm(data=request.POST)
        if data.is_valid():
            user=data.get_user()
            login(request,user)
            return redirect('users')
        else:
            return redirect('login')
    else:

        content={
            'loginForm':AuthenticationForm

        }

    return render(request,'pages/login/login-view.html',content)
@login_required(login_url='login')
def users(request):
    return render(request, 'pages/users/users-view.html')
def user_logout(request):
    if request.method=='POST':
        logout(request)
        return redirect('login')
    else:
        return HttpResponse ('Invalid access ')

    # return render(request, 'pages/users/-view.html')









def physicsnews(request):
    return render(request,'pages/physicsnews/physicsnews.html')

def download(request):
    return render(request,'download/download.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'pages/login/signup.html', {'form': form})
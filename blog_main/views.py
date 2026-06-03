
from multiprocessing import context
from pyexpat import features
from telnetlib import AUTHENTICATION
from unicodedata import category
from django.shortcuts import render, redirect
# from blog.blog_main.forms import RegistrationForm
from blogs.models import Blog
from blogs.models import Category
from blogs.models import About
from blogs.models import SocalLink
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth



def home(request):
    # categories = Category.objects.all()
    featured_posts= Blog.objects.filter(is_featured=True, status="Published").order_by('updated_at')
    posts= Blog.objects.filter(is_featured= False, status="Published")
    about = About.objects.first()
    social = SocalLink.objects.all()


    context= {
        # 'categories':categories,
        'featured_posts':featured_posts,
        'posts': posts,
        'about': about,
        'social': social,
    }
    return render(request, 'home.html',context)

def about(request):
    about = About.objects.first()
    print("About Info:", about)

    context = {
        'about': about,
    }

    return render(request, 'about.html', context)




def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()

    context={
        'form': form
    }
    return render(request, 'register.html',context)



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
    form = AuthenticationForm()
    context={
        'form': form
    }
    return render(request, 'login.html',context)


def logout(request):
    auth.logout(request)
    return redirect('home')
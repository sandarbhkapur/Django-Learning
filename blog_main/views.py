
from multiprocessing import context
from pyexpat import features
from unicodedata import category
from django.shortcuts import render
from blogs.models import Blog
from blogs.models import Category
from blogs.models import About
from blogs.models import SocalLink



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



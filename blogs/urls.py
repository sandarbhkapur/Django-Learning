
# from django.urls import path

# from . import views

# app_name = 'blogs'

# urlpatterns = [

#     path('<int:category_id>/',views.posts_by_category, name='post_by_category')

# ]

from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('<int:category_id>/', views.posts_by_category, name='posts_by_category'),
]
from django.urls import path
from .import views


app_name = 'images'

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'),
    # path('like/', views.image_like, name='like'),
    path('like/<int:pk>/', views.like_image, name='like_image'),
    # path('unlike/<int:pk>/', views.unlike_image, name='unlike_image'),
    path('', views.image_list, name='list'),
]   
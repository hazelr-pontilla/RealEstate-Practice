from django.urls import path
from . import views
# from listing import views can be use this

urlpatterns = [
    path('', views.listings, name='all-listings'),
    path('<pk>/', views.retrieve, name='retrieve'),
    path('create', views.create, name='create'),
    
]

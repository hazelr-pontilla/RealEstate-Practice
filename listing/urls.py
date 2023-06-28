from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

# from listing import views can be use this

urlpatterns = [
    path('', views.listings, name='all-listings'),
    path('<pk>/', views.retrieve, name='retrieve'),
    path('create', views.create, name='create'),
    path('update/<pk>/', views.update, name='update'),
    path('delete/<pk>/', views.delete, name='delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

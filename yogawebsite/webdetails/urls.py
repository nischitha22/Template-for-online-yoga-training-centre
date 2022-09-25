


from unicodedata import name
from django.urls import path
from. import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('home2/', views.home2, name='home2'),
    path('classes/', views.classes, name='classes'),
    path('about/', views.about, name='about'),
]

urlpatterns += staticfiles_urlpatterns()
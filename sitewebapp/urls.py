from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('work/', views.work, name='work'),
    path('work-single', views.work_single, name='work_single'),
    path('Newsletter-Post', views.NewsletterPost, name='NewsletterPost'),
]

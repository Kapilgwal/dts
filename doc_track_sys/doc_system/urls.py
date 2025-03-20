from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',views.home, name='home'),
    path('profile/',views.profile, name='profile'),
    path('my_doc/',views.my_doc, name='my_doc'),
    path('documents/',views.document, name='documents'),
]

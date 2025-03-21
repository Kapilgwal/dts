from django.urls import path
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home, name='home'),
    path('profile/',views.profile, name='profile'),
    path('my_doc/',views.my_doc, name='my_doc'),
    path('documents/',views.document, name='documents'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

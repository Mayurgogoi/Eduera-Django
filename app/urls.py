from os import name
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path("", views.home, name="Home"),
    path("aboutus/", views.aboutUs, name="About"),
    path("contact/", views.contact, name="Contact"),
    path("courses/", views.courses, name="Courses"),
]
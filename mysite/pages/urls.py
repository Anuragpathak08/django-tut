from django.urls import path
from .views import *


urlpatterns = [
    path('', view=home, name = 'home'),
    path('about/', view=about, name = 'about'),
    path('contact/', view=contact, name = 'contact'),
    path('hobbies/', view=hobbies, name = 'hobbies'),
]
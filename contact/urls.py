from django.urls import path
from . import views

urlpatterns = [
    # Core paths
    path('', views.contact, name='contact'),
]

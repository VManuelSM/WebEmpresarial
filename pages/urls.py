from django.urls import path
from . import views

urlpatterns = [
    # Blog paths
    path('<int:page_id>/<slug:page_title>/', views.page, name='page')
]

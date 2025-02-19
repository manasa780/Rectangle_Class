# rectangles/urls.py

from django.urls import path
from .views import rectangle_view

urlpatterns = [
    path('rectangle/<int:length>/<int:width>/', rectangle_view, name='rectangle_view'),
]
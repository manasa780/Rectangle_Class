from django.shortcuts import render

# Create your views here.
# rectangles/views.py

from django.http import JsonResponse
from .models import Rectangle

def rectangle_view(request, length: int, width: int):
    rectangle = Rectangle(length, width)
    response_data = list(rectangle)  # Convert the iterator to a list
    return JsonResponse(response_data, safe=False)
from django import http
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from . import highlighter
from django.conf import settings

import os

# Create your views here.
def upload_image(request):
    if request.method == "POST":
        image = request.FILES["photo"]
        Image.objects.create(image = image)
        return HttpResponseRedirect("result")    
    
    return render(request, 'highlighter/upload.html')

def show_res(request):
    path = os.path.join(settings.MEDIA_ROOT, "test_image.jpeg")
    li = highlighter.highlighter_func(path)
    images = Image.objects.all()
    if len(images) >0:
        Image.objects.all().delete()
    return render(request, "highlighter/result.html", {"images": images , "li" : li})
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name = 'upload'),
    path("result/", views.show_res, name = 'result'),
]

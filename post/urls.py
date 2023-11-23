from django.urls import path
from .views import main, detail

urlpatterns = [
    path('', main,),
    path('detail/<int:pk>', detail),
]
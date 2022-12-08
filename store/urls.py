from django.urls import *

from . import views


urlpatterns = [
    path('product/', views.allProduct),

    path('', views.index, name="index"),
] 




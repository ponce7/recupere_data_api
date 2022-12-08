from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.http import JsonResponse
import requests


@api_view(['GET'])
def allProduct(request):
    products = Product.objects.all()
    serialization = ProductSerializer(products,many=True)
    return JsonResponse(serialization.data, safe=False)



def index(request):
    response = requests.get('http://127.0.0.1:8000/api/product/').json()
    return render(request, 'index.html', {'response': response})
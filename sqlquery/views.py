from django.shortcuts import render
from .models import Product
import json
from django.http import JsonResponse
from django.core.serializers import serialize
from django.db import connection

# Create your views here.
def home(request):
    qs = Product.objects.all()
    serialized_data = serialize("json", qs)

    print(connection.queries)
    
    serialized_data = json.loads(serialized_data)
    return JsonResponse(serialized_data, safe=False, status=200)
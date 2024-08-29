from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from django.core.serializers import serialize
import json



def add_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try: 
          seller_id = request.POST.get('seller_id')
          seller = seller.objects.get(id=seller_id)
          if seller.is_confirm:
              name_product = data['name']
              price = data['price']
              description = data['description']
              seller = data['seller']
              new_product = product.objects.create(name=name_product, price=price, description=description, seller=seller)
              return jsonresponse({'message': 'product added successfully'}, status=200)
          else:

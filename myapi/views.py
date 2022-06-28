# from rest_framework import viewsets
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .serializers import MenuSerializer
from .models import Menu

# class HeroViewSet (viewsets.ModelViewSet):
#     queryset = Hero.objects.all().order_by('name')
#     serializer_class = HeroSerializer

# Create your views here.

@csrf_exempt
def menuApi(request, id=0):
    if request.method=='GET':
        Menus = Menu.objects.all()
        Menus_serializer = MenuSerializer(Menus, many=True)
        return JsonResponse(Menus_serializer.data, safe=False)
    elif request.method=='POST':
        Menus_data = JSONParser().parse(request)
        Menus_serializer = MenuSerializer(data=Menus_data)
        if Menus_serializer.is_valid():
            Menus_serializer.save()
            return JsonResponse("data added succesfully", safe=False)
        return JsonResponse("unable to add the data", safe=False)
    elif request.method=='PUT':
        Menus_data = JSONParser().parse(request)
        Menus = Menu.objects.get(Menus_id=Menus_data["Menus_id"])
        Menus_serializer = MenuSerializer(Menus, data = Menus_data)
        if Menus_serializer.is_valid():
            Menus_serializer.save()
            return JsonResponse("data was updated succesfully", safe=False)
        return JsonResponse("data was unable to be updated")
    elif request.method=="DELETE":
        Menus = Menu.objects.get(Menus_id=id)
        Menus.delete()
        return JsonResponse("data deleted succesfully", safe = False)
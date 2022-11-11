from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Pet.models import Pet,Account
from Pet.serializers import PetSerializer

# Create your views here.
@csrf_exempt
def petAPI(request):
    if request.method == 'GET':
        petall = Pet.objects.all()
        pet_serializer = PetSerializer(petall,many=True)
        return JsonResponse(pet_serializer.data,safe =False)
    elif request.method == 'POST':
        #create Pet
        petDataCreate = JSONParser().parse(request)
        petDataCreateSerializer = PetSerializer(data = petDataCreate)
        # check request not null
        if petDataCreateSerializer.is_valid():
            petDataCreateSerializer.save()
            return JsonResponse("Created Pet",safe=False)
        return JsonResponse("can't Create",safe=False)
@csrf_exempt
def accountAPI(request):
    pass
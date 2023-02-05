from django.shortcuts import render
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer, UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model

User = get_user_model()


@api_view(["GET"])
def api_root(request, format= None):
	return Response({
		"dog-list": reverse("dog-list", request= request, format= format),
		"breed-list": reverse("breed-list", request= request, format= format),
	})
	

class Register(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class DogList(generics.ListCreateAPIView):
	queryset = Dog.objects.all()
	serializer_class = DogSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly]
	
	
class DogDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Dog.objects.all()
	serializer_class = DogSerializer
	lookup_field = "id"
	
	
class BreedList(generics.ListCreateAPIView):
	queryset = Breed.objects.all()
	serializer_class = BreedSerializer
	
	
class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Breed.objects.all()
	serializer_class = BreedSerializer
	lookup_field = "id"

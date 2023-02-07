from rest_framework import serializers
from .models import Dog, Breed
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class DogSerializer(serializers.ModelSerializer):
	# breed = serializers.HyperlinkedRelatedField(queryset= Breed.objects.all(), view_name= "breed-detail", lookup_field= "id")
	class Meta:
		model = Dog
		fields = "__all__"


class BreedSerializer(serializers.ModelSerializer):	
	class Meta:
		model = Breed
		fields = "__all__"
		
						
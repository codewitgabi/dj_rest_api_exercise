from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views


urlpatterns = [
	# path("", views.api_root, name= "api_root"),
	path("dog-list", views.DogList.as_view(), name= "dog-list"),
	path("dog-detail/<int:id>", views.DogDetail.as_view(), name= "dog-detail"),
	path("breed-list", views.BreedList.as_view(), name= "breed-list"),
	path("breed-detail/<int:id>", views.BreedDetail.as_view(), name= "breed-detail"),
	path("register/", views.Register.as_view(), name="register"),
]

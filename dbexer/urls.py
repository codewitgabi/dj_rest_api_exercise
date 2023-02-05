from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
	openapi.Info(
		title= "Dog API",
		default_version= "1.0.1",
		description= "An API for different dogs and breed. Use this for testing your knowledge on web apis. It is totally free to use. Create as much data as you want but invalid data will be cleared weekly",
	),
	public= True,
	
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/", (
    	include([
    		path("doc/", schema_view.with_ui("swagger", cache_timeout= 0), name= "swagger"),
    	])
    )),	
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path
from . import views

urlpatterns = [
	path('', views.gallery, name="gallery"),
	path('addp', views.addPhoto, name="add_photo"),
	path('addc', views.addCategory, name="add_category"),
]
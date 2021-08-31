from django import forms
from .models import Category 


categories = Category.objects.all()
IMAGE_CATEGORIES = [category for category in categories]

class addPhotos(forms.Form):
	image = forms.ImageField()
	category = forms.ChoiceField(label="Select Category")

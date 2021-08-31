from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Category, Photo
from .forms import addPhotos


def gallery(request):
	category = request.GET.get('category')
	print(category)

	if category == None:
		photos = Photo.objects.all()
	else:
		photos = Photo.objects.filter(category__name=category)


	categories = Category.objects.all()
	context = {'categories': categories, 'photos': photos}
	return render(request, "gallery/index.html", context)


def addPhoto(request):
	categories = Category.objects.all()

	if request.method == 'POST':
		data = request.POST
		image = request.FILES.get('image')

		if data['category'] != 'none':
			category = Category.objects.get(id=data['category'])
		elif data['category_new'] != '':
			category, create = Category.objects.get_or_create(name=data['category_new'])
		else:
			category = None

		photo = Photo.objects.create(
			category=category,
			image=image
		)

		messages.success(request, 'Image has been uploaded Successfully')
		return redirect('gallery')

	return render(request, "gallery/addPhoto.html", {'categories': categories})
	
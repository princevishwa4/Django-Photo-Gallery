from django.shortcuts import render


def gallery(request):
	return render(request, "gallery/index.html")

def addPhoto(request):
	pass
	# return render(request, "gallery/index.html")

def addCategory(request):
	pass
	# return render(request, "gallery/index.html")		
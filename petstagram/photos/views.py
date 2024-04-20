from django.shortcuts import render

# Create your views here.


def add_photo(request):
    context = {}
    return render(request, 'photos/add_photo.html', context)


def details_photo(request, pk):
    context = {}
    return render(request, 'photos/details_photo.html', context)


def edit_photo(request, pk):
    context = {}
    return render(request, 'photos/edit_photo.html', context)
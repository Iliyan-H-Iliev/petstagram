from django.shortcuts import render

from petstagram.pets.models import Pet


# Create your views here.


def add_pet(request):
    context = {}
    return render(request, 'pets/add_pet.html', context)


def details_pet(request, username, pet_slug):
    context = {
        "pet": Pet.objects.get(slug=pet_slug)
    }
    return render(request, 'pets/details_pet.html', context)


def edit_pet(request, username, pet_slug):
    context = {}
    return render(request, 'pets/edit_pet.html', context)


def delete_pet(request, username, pet_slug):
    context = {}
    return render(request, 'pets/delete_pet.html', context)
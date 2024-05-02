from django.shortcuts import render, redirect

from petstagram.common.models import PhotoLike
from petstagram.photos.models import PetPhoto


# Create your views here.


def index(request):
    context = {
        'pet_photos': PetPhoto.objects.all(),
    }
    return render(request, 'common/index.html', context)


def like_pet_photo(request, pk):
    pet_photo_like = PhotoLike.objects.filter(pet_photo_id=pk).filter()

    if pet_photo_like:
        pet_photo_like.delete()
    else:
        PhotoLike.objects.create(pet_photo_id=pk)

    return redirect(request.META.get('HTTP_REFERER') + f"#photo-{pk}")
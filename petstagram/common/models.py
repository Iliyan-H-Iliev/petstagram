from django.db import models
from django.db.models import DO_NOTHING

from petstagram.photos.models import PetPhoto


# Create your models here.


class PhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.TextField(max_length=MAX_TEXT_LENGTH, null=False, blank=False)

    pet_photo = models.ForeignKey(PetPhoto, on_delete=DO_NOTHING, related_name="comments")

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class PhotoLike(models.Model):
    pet_photo = models.ForeignKey(PetPhoto, on_delete=DO_NOTHING, related_name="likes")

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
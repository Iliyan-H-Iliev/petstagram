from django.core.validators import MinLengthValidator, BaseValidator
from django.db import models

from petstagram.pets.models import Pet

# Create your models here.
PHOTO_SIZE_LIMIT = 5 * 1024 * 1024


class MaxSizeValidator(BaseValidator):

    def clean(self, x):
        return x.size > PHOTO_SIZE_LIMIT

    def compare(self, file_size, max_size):
        return file_size > max_size


# def image_size_less_than_5mb(image):
#     if image.size > PHOTO_SIZE_LIMIT:
#         raise ValueError("Image file is too large ( > 5mb )")


class PetPhoto(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to="pet_photos",
        null=False,
        blank=False,
        validators=[MaxSizeValidator(limit_value=PHOTO_SIZE_LIMIT)],
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=[MinLengthValidator(MIN_DESCRIPTION_LENGTH)],
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    pets = models.ManyToManyField(Pet, related_name="photos")

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

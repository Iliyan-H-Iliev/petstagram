from django.contrib import admin

from petstagram.photos.models import PetPhoto


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "photo", "location", "short_description", "created_at", "tagged_pets",)

    def tagged_pets(self, obj):
        return ", ".join([pet.name for pet in obj.pets.all()])


    def short_description(self, obj):
        return obj.description[:20] if obj.description else ""

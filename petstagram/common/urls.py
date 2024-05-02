from django.urls import path

from petstagram.accounts import views
from petstagram.common.views import index, like_pet_photo

urlpatterns = (
    path("", index, name="index"),
    path("pet_photo_like/<int:pk>/", like_pet_photo, name="pet photo likes"),
)
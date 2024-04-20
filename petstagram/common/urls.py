from django.urls import path

from petstagram.accounts import views
from petstagram.common.views import index

urlpatterns = (
    path("", index, name="index"),
)
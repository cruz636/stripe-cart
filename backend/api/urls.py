from django.urls import path

from .views import DetailItemView, ItemView


urlpatterns = [
    path("items/<int:pk>/", DetailItemView.as_view()),
    path("items/", ItemView.as_view()),
]

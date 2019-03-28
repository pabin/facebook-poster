from django.urls import path

from .views import (
    StatusUpdateView,
)

urlpatterns = [
    path('facebook/', StatusUpdateView.as_view(), name='facebook_poster'),
]

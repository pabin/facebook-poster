from django.urls import path

from .views import (
    StatusUpdateView,
)

urlpatterns = [
    path('', StatusUpdateView.as_view(), name='home'),
]

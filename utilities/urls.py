from django.urls import path

from .views import (
    CreateUtilitiesView,
    EditUtilitiesView,
    DetailUtilitiesView,
    ListUtilitiesView
)

app_name = "utilities"
urlpatterns = [
    path('', ListUtilitiesView.as_view(), name='list'),
    path('create/', CreateUtilitiesView.as_view(), name='create'),
    path('<int:pk>/', DetailUtilitiesView.as_view(), name='detail'),
    path('<int:pk>/edit/', EditUtilitiesView.as_view(), name='edit'),
]

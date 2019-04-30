from django.urls import path, include

from .views import SignUpView, DetailUserView, EditUserView

app_name = "users"
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<str:username>/', DetailUserView.as_view(), name='detail'),
    path('<str:username>/edit/', EditUserView.as_view(), name='edit'),
]

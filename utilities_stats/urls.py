from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.defaults import ( 
    page_not_found,
    server_error,
    permission_denied
)

from rest_framework import routers

from api.views import UserViewSet, UtilitiesViewSet
from utilities.views import HomeView

from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'utilities', UtilitiesViewSet)

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('utilities/', include('utilities.urls')),
    path('', HomeView.as_view(), name='home'),
    path(
        'about/',
        TemplateView.as_view(template_name='about.html'),
        name='about'
    ),
    path('api/', include(router.urls)),
    path(
        'api/auth/',
        include('rest_framework.urls', namespace='rest_framework'),
    ),


)


def custom_page_not_found(request):
    return page_not_found(request, None)


def custom_permission_denied(request):
    return permission_denied(request, None)


if settings.DEBUG:
    urlpatterns += i18n_patterns(
        path("404/", custom_page_not_found),
        path("403/", custom_permission_denied),
        path("500/", server_error),
    )

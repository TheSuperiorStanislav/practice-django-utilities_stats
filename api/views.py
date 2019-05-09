from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    BasePermission,
    IsAdminUser,
)
from rest_framework.response import Response

from .serializers import UserSerializer, UtilitiesSerializer
from users.models import UtilitiesUser
from utilities.models import Utilities


def get_owner_url(request, owner):
    return "%s://%s/api/users/%s/" % (
        request.scheme,
        request.get_host(),
        owner.pk
        )


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class UserViewSet(viewsets.ModelViewSet):
    queryset = UtilitiesUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UtilitiesViewSet(viewsets.ModelViewSet):
    queryset = Utilities.objects.filter()
    serializer_class = UtilitiesSerializer
    permission_classes = [IsAuthenticated & IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Utilities.objects.filter(owner=user)

    # Create a model instance.
    def create(self, request, *args, **kwargs):
        data = request.data
        data['owner'] = get_owner_url(request, request.user)
        serializer = self.serializer_class(
            data=data,
            context={'request': request}
            )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    # Update a model instance.
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data
        data['owner'] = get_owner_url(request, request.user)
        serializer = self.get_serializer(
            instance,
            data=data,
            partial=partial,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

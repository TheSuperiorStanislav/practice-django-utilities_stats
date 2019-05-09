from rest_framework import serializers

from users.models import UtilitiesUser
from utilities.models import Utilities


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UtilitiesUser
        # Is it legal?
        fields = ('pk', 'username', 'password', 'email')


class UtilitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Utilities
        fields = '__all__'

from rest_framework import serializers

from users.models import UtilitiesUser
from utilities.models import Utilities
from utilities.utils import is_data_valid, is_date_valid


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UtilitiesUser
        # Is it legal?
        fields = ('pk', 'username', 'password', 'email')


class UtilitiesSerializer(serializers.HyperlinkedModelSerializer):

    def validate_date(self, value):
        owner = self.initial_data['owner'].split('/')[-2]
        if not is_date_valid(owner, value):
            msg = u'This entry already exists!'
            raise serializers.ValidationError(msg)
        return value

    def validate(self, data):
        if not is_data_valid(data):
            raise serializers.ValidationError(
                    'Amount to pay != sum(services price)',
                )

        return data

    class Meta:
        model = Utilities
        fields = '__all__'

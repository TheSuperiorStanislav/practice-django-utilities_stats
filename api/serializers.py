from rest_framework import serializers

from users.models import UtilitiesUser
from utilities.models import Utilities
from utilities.utils import is_data_validation_error, is_date_validation_error


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UtilitiesUser
        # Is it legal?
        fields = ('pk', 'username', 'password', 'email')


class UtilitiesSerializer(serializers.HyperlinkedModelSerializer):

    def validate_date(self, value):
        owner = self.initial_data['owner'].split('/')[-2]
        error = is_date_validation_error(owner, value)
        if error:
            msg = u'This entry(%s) already exists!' % (error)
            raise serializers.ValidationError(msg)
        return value

    def validate(self, data):
        error = is_data_validation_error(data)
        if error:
            raise serializers.ValidationError(error)

        return data

    class Meta:
        model = Utilities
        fields = '__all__'

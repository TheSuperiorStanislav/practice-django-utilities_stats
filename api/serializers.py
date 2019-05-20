from rest_framework import serializers

from users.models import UtilitiesUser
from utilities.models import Utilities
from utilities.utils import is_data_validation_error, is_date_validation_error


class empty:
    """
    This class is used to represent no data being provided for a given input
    or output value.
    It is required because `None` may be a valid input or output value.
    """
    pass


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UtilitiesUser
        # Is it legal?
        fields = ('pk', 'username', 'password', 'email')


class UtilitiesSerializer(serializers.HyperlinkedModelSerializer):
    def validate_date(self, value):
        owner = self.initial_data['owner'].split('/')[-2]
        if self.instance:
            edit_utilities = Utilities.objects.get(pk=self.instance.pk)
            if value.month == edit_utilities.date.month:
                return value
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

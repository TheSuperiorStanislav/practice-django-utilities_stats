from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UtilitiesUser


class UtilitiesUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UtilitiesUser
        fields = UserCreationForm.Meta.fields


class UtilitiesUserChangeForm(UserChangeForm):

    class Meta:
        model = UtilitiesUser
        fields = UserChangeForm.Meta.fields

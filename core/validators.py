from django.core.exceptions import ValidationError


def validate_norm(value):
    """Raise a ValidationError
        if the norm value lte zero.
    """
    if not value > 0:
        msg = u"Must be greater than zero"
        raise ValidationError(msg)

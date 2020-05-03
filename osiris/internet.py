from osiris import _
from osiris.osiris import osiris_validator
from osiris.exceptions import ValidationException


@osiris_validator
def validate_email(func, *args, **kwargs):
    message = _('{0} must be valid.'.format(kwargs['field']))
    if 'message' in kwargs:
        message = kwargs['message']

    def wrapper(obj, arg1, arg2):
        if '@' not in arg2:
            raise ValidationException(kwargs['field'], message)
        else:
            return func(obj, arg1, arg2)

    return wrapper
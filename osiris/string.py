from osiris import _
from osiris.osiris import osiris_validator
from osiris.exceptions import ValidationException


@osiris_validator
def not_empty(func, *args, **kwargs):
    message = _('{0} may not be empty.'.format(kwargs['field']))
    if 'message' in kwargs:
        message = kwargs['message']

    def wrapper(obj, arg1, arg2):
        if arg2 is None or len(arg2) == 0:
            raise ValidationException(kwargs['field'], message)
        else:
            return func(obj, arg1, arg2)

    return wrapper


@osiris_validator
def not_blank(func, *args, **kwargs):
    message = _('{0} may not be blank.'.format(kwargs['field']))
    if 'message' in kwargs:
        message = kwargs['message']

    def wrapper(obj, arg1, arg2):
        if arg2 is None or len(arg2.strip()) == 0:
            raise ValidationException(kwargs['field'], message)
        else:
            return func(obj, arg1, arg2)

    return wrapper

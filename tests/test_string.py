import unittest
from osiris.string import *


class TestString(unittest.TestCase):

    def test_not_empty_str_null(self):
        @not_empty(field='field')
        def validation(obj, key, field_value):
            return field_value
        value = None
        self.assertRaises(ValidationException, validation, None, 1, value)

    def test_not_empty_str_empty(self):
        @not_empty(field='field')
        def validation(obj, key, field_value):
            return field_value
        value = ''
        self.assertRaises(ValidationException, validation, None, 1, value)

    def test_not_empty_str_blank(self):
        @not_empty(field='field')
        def validation(obj, key, field_value):
            return field_value
        value = '    '
        self.assertEqual(validation(None, 1, value), value)

    def test_not_empty_str_filled(self):
        @not_empty(field='field')
        def validation(obj, key, field_value):
            return field_value
        value = '1234 45a123'
        self.assertEqual(validation(None, 1, value), value)

    def test_not_blank_str_null(self):
        @not_blank(field='field')
        def validation(obj, key, field_value):
            return field_value
        value = None
        self.assertRaises(ValidationException, validation, None, 1, value)

    def test_not_blank_str_empty(self):
        @not_blank(field='field')
        def validation(obj, key, field_value):
            return field_value
        value = ''
        self.assertRaises(ValidationException, validation, None, 1, value)

    def test_not_blank_str_blank(self):
        @not_blank(field='field')
        def validation(obj, key, field_value):
            return field_value
        value = '    '
        self.assertRaises(ValidationException, validation, None, 1, value)

    def test_not_blank_str_filled(self):
        @not_blank(field='field')
        def validation(obj, key, field_value):
            return field_value
        value = '1234 45a123'
        self.assertEqual(validation(None, 1, value), value)

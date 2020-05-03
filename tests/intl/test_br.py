import unittest
from osiris.intl.br import *


class TestBR(unittest.TestCase):

    def test_cpf_random_string(self):
        @valid_cpf(field='field')
        def validation(obj, key, field_value):
            return field_value
        value = 'a6712gdsa!das1'
        self.assertRaises(ValidationException, validation, None, 1, value)

    def test_cpf_invalid_len(self):
        @valid_cpf(field='field')
        def validation(obj, key, field_value):
            return field_value
        value = '1234'
        self.assertRaises(ValidationException, validation, None, 1, value)

    def test_cpf_invalid_cpf(self):
        @valid_cpf(field='field')
        def validation(obj, key, field_value):
            return field_value
        value = '12345678911'
        self.assertRaises(ValidationException, validation, None, 1, value)

    def test_cpf_repeated_numbers(self):
        @valid_cpf(field='field')
        def validation(obj, key, field_value):
            return field_value
        value = '11111111111'
        self.assertRaises(ValidationException, validation, None, 1, value)

    def test_cpf_valid_cpf(self):
        @valid_cpf(field='field')
        def validation(obj, key, field_value):
            return field_value

        value = '36041181404'
        self.assertEqual(validation(None, 1, value), value)


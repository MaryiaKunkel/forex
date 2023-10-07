from unittest import TestCase
from currency_converter import is_valid_amount, is_valid_currency_from, get_exchange_rate, get_currency_symbol

class TestCurrencyConversion(TestCase):
    def test_is_valid_amount(self):
        valid_amount = "100"
        self.assertTrue(is_valid_amount(valid_amount))
        
        invalid_amount = "abc"
        self.assertFalse(is_valid_amount(invalid_amount))

    def test_is_valid_currency_from(self):
        valid_currency='USD'
        self.assertTrue(is_valid_currency_from(valid_currency))

        invalid_currency='AAA'
        self.assertFalse(is_valid_currency_from(invalid_currency))

    def test_is_valid_exchange_rate(self):
        valid_convert_from='USD'
        valid_convert_to='RUB'
        valid_amount='50'
        access_key='fdf7087eb3fc3227ef65d44d43688757'

        self.assertTrue(get_exchange_rate(valid_convert_from, valid_convert_to, access_key, valid_amount))

    def test_is_invalid_exchange_rate(self):
        valid_convert_from='USD'
        invalid_convert_to='AAA'
        valid_amount='50'
        access_key='fdf7087eb3fc3227ef65d44d43688757'

        self.assertFalse(get_exchange_rate(valid_convert_from, invalid_convert_to, access_key, valid_amount))

    def test_get_currency_symbol(self):
        valid_currency='USD'
        self.assertTrue(get_currency_symbol(valid_currency))

        invalid_currency='AAA'
        self.assertTrue(get_currency_symbol(invalid_currency))




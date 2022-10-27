import unittest
from unittest import TestCase
from unittest.mock import patch

import exchange_rate

class TestExchangeRates(TestCase):

    @patch('exchange_rate.request_rates')
    def test_dollas_to_target(self, mock_rates):
        mock_rate = 13.4567
        example_api_response = {"rates":{"CAD":mock_rate},"base":"USD","date":"2020-10-02"}
        mock_rates.side_effect = [ example_api_response ]
        converted = exchange_rate.convert_dollars_to_target(100, 'CAD')
        expected = 1345.67
        self.assertEqual(expected, converted)

    # todo -test error conditions
    # examples - check for error when currency symbol is not found
    # dollar value is not a number
    # connection errors to exchange rate API
    # assertRaise
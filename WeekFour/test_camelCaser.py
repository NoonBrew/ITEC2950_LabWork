import camelCaser
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloWorld', camelCaser.ccConverter('Hello World'))
        self.assertEqual('', camelCaser.ccConverter(''))
        self.assertEqual('helloWorld', camelCaser.ccConverter('          Hello             World   '))
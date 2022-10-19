from django.test import TestCase


class AnimalTestCase(TestCase):
    def setUp(self):
        print("Hello")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        test = "hello"
        self.assertEqual(test, 'hello')

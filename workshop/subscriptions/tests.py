from django.test import TestCase

class SubscriptionTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/subscription/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

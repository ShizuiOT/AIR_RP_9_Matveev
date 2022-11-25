from django.test import TestCase
from django.urls import reverse
import json
from rest_framework.test import APITestCase

class SoftwareTests(APITestCase):
    def test_get_correct(self):
        url = reverse('Getter', args=["Corporate_architecture", "Windows", "Archi", '2'])
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content), [{
            "id": 6,
            "Discipline": "Corporate_architecture",
            "OpSys": "Windows",
            "Name": "Archi",
            "Practicum_Num": "2"
        }])
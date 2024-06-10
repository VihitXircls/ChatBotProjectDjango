from django.test import TestCase,Client
from django.urls import reverse

class ProcessInputTestCase(TestCase):
    def test_process_input(self):
        client = Client()
        data = {"query":"The product received is damaged. I want to return it."}
        response = client.post(reverse('index'),data=data)
        self.assertEqual(response.status_code,200)



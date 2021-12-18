from django.test import TestCase
from .models import Table


class TestTable(TestCase):
    def setUp(self):
        self.post_1 = Table.objects.create(
            name='Test 1',
            date='2000-01-01',
            quantity=100,
            distance=500,
        )
        self.response = self.client.get('/')
    
    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_page_contain_data(self):
        self.assertContains(self.response, 'Test 1')
        self.assertContains(self.response, '1 января 2000 г.')
        self.assertContains(self.response, 100)
        self.assertContains(self.response, 500)

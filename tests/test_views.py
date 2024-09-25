from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title="Lamb Ribs", price=30.00, inventory=15)

    def test_getall(self):
        self.setup()

        client = APIClient()
        response = client.get("/restaurant/menu/items/")

        assert response.status_code == 200
        lamb_id = Menu.objects.get(title="Lamb Ribs")
        self.assertEqual([{"id": lamb_id.id, "title": "Lamb Ribs", "price": "30.00", "inventory": 15}], response.data)
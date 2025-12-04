from django.test import Client,TestCase
from django.urls import reverse
from .models import Product
# Create your tests here.
class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name = "Laptop",price=10000)
    def test_str_method(self):
        self.assertEqual(str(self.product),"Laptop")
    def test_discount_price(self):
        discount = self.product.discount_price(10)
        self.assertEqual(discount,9000)
    


class ProductViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        Product.objects.create(name="Phone", price=800)

    def test_homepage_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_shows_product(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Phone")

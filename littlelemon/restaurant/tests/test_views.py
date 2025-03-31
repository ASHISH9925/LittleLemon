from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):  
        Menu.objects.create(Title="Candy", Price=10, Inventory=50)
        Menu.objects.create(Title="Popsicle", Price=10, Inventory=50)
        Menu.objects.create(Title="Pizza", Price=105, Inventory=50)

    def test_getall(self):
        queryset = Menu.objects.all()
        serialized_data = MenuSerializer(queryset, many=True).data  
        self.assertEqual(len(serialized_data), 3)  
        self.assertEqual(serialized_data[0]["Title"], "Candy")  
        self.assertEqual(serialized_data[1]["Title"], "Popsicle") 
        self.assertEqual(serialized_data[2]["Title"], "Pizza")  
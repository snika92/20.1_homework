from django.core.management import BaseCommand
from products.models import Product, Category
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        with open("data.json", "r", encoding="utf-8") as json_file:
            items_list = json.load(json_file)

        products_to_create = []
        categories_to_create = []
        for item in items_list:
            if item["model"] == "products.category":
                categories_to_create.append(Category(**item["fields"]))
        Category.truncate_table_restart_id()
        Category.objects.bulk_create(categories_to_create)
        for item in items_list:
            if item["model"] == "products.product":
                item['fields']['category'] = Category.objects.get(id=item['fields']['category'])
                products_to_create.append(Product(**item["fields"]))
        Product.objects.bulk_create(products_to_create)

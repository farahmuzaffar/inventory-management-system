from exceptions.product_exists import ProductExistsError
from models.grocery import Grocery

class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        # Check if product with the same ID already exists in inventory
        if product._product_id in self._products:
            # If you want to skip adding the product instead of raising an error, you can:
            # print(f"❌ Product with ID {product._product_id} already exists. Skipping...")
            # return
            raise ProductExistsError(f"❌ Product with ID {product._product_id} already exists.")
        self._products[product._product_id] = product

    def remove_product(self, product_id):
        if product_id in self._products:
            del self._products[product_id]

    def search_by_name(self, name):
        return [p for p in self._products.values() if p._name.lower() == name.lower()]

    def search_by_type(self, product_type):
        return [p for p in self._products.values() if isinstance(p, product_type)]

    def list_all_products(self):
        return list(self._products.values())  # This returns a list of all products

    def sell_product(self, product_id, quantity):
        if product_id in self._products:
            self._products[product_id].sell(quantity)

    def restock_product(self, product_id, quantity):
        if product_id in self._products:
            self._products[product_id].restock(quantity)

    def total_inventory_value(self):
        return sum(p.get_total_value() for p in self._products.values())

    def remove_expired_products(self):
        to_remove = [pid for pid, p in self._products.items() if isinstance(p, Grocery) and p.is_expired()]
        for pid in to_remove:
            del self._products[pid]


# clothing.py
from models.base_product import Product

class Clothing(Product):
    def __init__(self, _product_id, _name, _price, _quantity_in_stock, size, material):
        super().__init__(_product_id, _name, _price, _quantity_in_stock)
        self.size = size
        self.material = material

    def __str__(self):
        return f"[Clothing] {self._name}, Size: {self.size}, Material: {self.material}, Stock: {self._quantity_in_stock}, Price: ${self._price}"

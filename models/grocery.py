from datetime import datetime
from models.base_product import Product

class Grocery(Product):
    def __init__(self, _product_id, _name, _price, _quantity_in_stock, expiry_date):
        super().__init__(_product_id, _name, _price, _quantity_in_stock)
        
        # Handle expiry_date with time
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d %H:%M:%S")  # Include time in the format
        
        # Or if you just want to handle the date part only:
        # self.expiry_date = datetime.strptime(expiry_date.split()[0], "%Y-%m-%d")

    def is_expired(self):
        return datetime.now() > self.expiry_date

    def __str__(self):
        return f"[Grocery] {self._name}, Expiry: {self.expiry_date.date()}, Stock: {self._quantity_in_stock}, Price: ${self._price}"

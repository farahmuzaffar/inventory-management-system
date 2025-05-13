import json
from models.electronics import Electronics
from models.grocery import Grocery
from models.clothing import Clothing

def save_to_file(filename, products):
    data = []
    for p in products:
        record = p.__dict__.copy()
        record["__type__"] = p.__class__.__name__
        data.append(record)
    with open(filename, "w") as f:
        json.dump(data, f, default=str)

# file_handler.py
# file_handler.py
# file_handler.py
def load_from_file(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)  # Load data from file
        products = []
        for item in data:
            print("Loaded item:", item)  # Debugging line to print loaded data
            product_type = item.pop("__type__")  # Get the type of the product from the saved data
            if product_type == "Electronics":
                p = Electronics(**item)
            elif product_type == "Grocery":
                p = Grocery(**item)
            elif product_type == "Clothing":
                p = Clothing(**item)
            products.append(p)
        print(f"Loaded products: {products}")  # Debugging line to see the list of products
        return products
    except json.JSONDecodeError:
        print("❌ Invalid JSON data in file.")
        return []  # Return an empty list if the JSON is invalid
    except FileNotFoundError:
        print("❌ File not found, starting with an empty inventory.")
        return []  # Return an empty list if the file doesn't exist

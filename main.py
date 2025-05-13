import streamlit as st  # type: ignore
from models.inventory import Inventory
from models.electronics import Electronics
from models.grocery import Grocery
from models.clothing import Clothing
from utils.file_handler import save_to_file, load_from_file
from exceptions.product_exists import ProductExistsError  # Import the exception

# Initialize the Inventory System
inventory = Inventory()

# Load existing products from file, if available
loaded_products = load_from_file("data/inventory_data.json")
for product in loaded_products:
    inventory.add_product(product)

# Set up Streamlit UI
st.title("📦 Inventory Management System")
menu = ["Add Product", "View Products", "Sell Product", "Restock Product", "Inventory Value", "Save Inventory", "Load Inventory"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Product":
    st.subheader("➕ Add New Product")
    product_type = st.selectbox("Product Type", ["Electronics", "Grocery", "Clothing"])
    product_id = st.text_input("Product ID")
    name = st.text_input("Name")
    price = st.number_input("Price", min_value=0.0)
    quantity = st.number_input("Quantity", min_value=1, step=1)

    if product_type == "Electronics":
        brand = st.text_input("Brand")
        warranty_years = st.number_input("Warranty Years", min_value=0, step=1)
    elif product_type == "Grocery":
        expiry_date = st.date_input("Expiry Date")
    elif product_type == "Clothing":
        size = st.selectbox("Size", ["S", "M", "L", "XL"])
        material = st.text_input("Material")

    if st.button("Add Product"):
        try:
            if product_type == "Electronics":
                p = Electronics(product_id, name, price, quantity, warranty_years, brand)
            elif product_type == "Grocery":
                p = Grocery(product_id, name, price, quantity, str(expiry_date))
            elif product_type == "Clothing":
                p = Clothing(product_id, name, price, quantity, size, material)

            # Attempt to add the product to the inventory
            inventory.add_product(p)
            st.success("✅ Product added successfully!")
        except ProductExistsError as e:
            st.error(f"❌ {e}")  # Display error message if product ID already exists
        except ValueError as e:
            st.error(f"❌ {e}")  # Handle other errors, such as empty product ID
        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")  # Catch all other exceptions

elif choice == "View Products":
    st.subheader("📋 All Products")
    # Ensure products are added to inventory after loading
    if len(inventory.list_all_products()) == 0:
        st.info("No products in inventory.")
    for p in inventory.list_all_products():
        st.text(str(p))

elif choice == "Sell Product":
    st.subheader("🛒 Sell Product")
    product_id = st.text_input("Enter Product ID")
    quantity = st.number_input("Quantity to Sell", min_value=1, step=1)
    if st.button("Sell"):
        try:
            inventory.sell_product(product_id, quantity)
            st.success("✅ Product sold successfully.")
        except Exception as e:
            st.error(f"❌ {e}")

elif choice == "Restock Product":
    st.subheader("📦 Restock Product")
    product_id = st.text_input("Enter Product ID")
    quantity = st.number_input("Quantity to Restock", min_value=1, step=1)
    if st.button("Restock"):
        try:
            inventory.restock_product(product_id, quantity)
            st.success("✅ Product restocked successfully.")
        except Exception as e:
            st.error(f"❌ {e}")

elif choice == "Inventory Value":
    st.subheader("💰 Total Inventory Value")
    value = inventory.total_inventory_value()
    st.info(f"Total Inventory Value: ${value:.2f}")

elif choice == "Save Inventory":
    st.subheader("💾 Save Inventory to File")
    if st.button("Save Now"):
        save_to_file("data/inventory_data.json", inventory.list_all_products())
        st.success("✅ Inventory saved successfully.")

elif choice == "Load Inventory":
    st.subheader("📂 Load Inventory from File")
    loaded_products = load_from_file("data/inventory_data.json")
    for product in loaded_products:
        inventory.add_product(product)
    st.success("✅ Inventory loaded successfully.")

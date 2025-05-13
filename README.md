# Inventory Management System

A simple Inventory Management System built with Python and Streamlit. This application allows users to manage products in an inventory, including adding, selling, restocking, and calculating the total inventory value. It also provides functionality to save and load inventory data from a file.

## Features

- **Add Product**: Allows users to add products to the inventory (Electronics, Grocery, and Clothing).
- **View Products**: Displays all products currently in the inventory.
- **Sell Product**: Enables the sale of products by reducing their quantity in stock.
- **Restock Product**: Restocks products by adding more quantity to the existing stock.
- **Inventory Value**: Calculates and displays the total value of the inventory.
- **Save Inventory**: Saves the current inventory data to a JSON file.
- **Load Inventory**: Loads the inventory data from a JSON file.

## Prerequisites

- Python 3.x
- Streamlit
- JSON file handling

## Installation

1. Clone the repository:

  
   git clone https://github.com/yourusername/inventory-management-system.git
   cd inventory-management-system
Install the required dependencies:


pip install streamlit
Run the Streamlit app:


streamlit run app.py
How It Works
Adding Products:

Select the product type (Electronics, Grocery, Clothing).

Provide the product details (ID, Name, Price, Quantity, etc.).

Click "Add Product" to add the product to the inventory. If the product already exists, an error message will appear.

Viewing Products:

View all the products currently in the inventory. If no products are available, a message will indicate that the inventory is empty.

Selling Products:

Enter the product ID and the quantity to sell.

Click "Sell" to reduce the stock quantity of the product.

Restocking Products:

Enter the product ID and the quantity to restock.

Click "Restock" to add the quantity to the product.

Total Inventory Value:

View the total value of the inventory based on the price and quantity of the products.

Saving Inventory:

Click "Save Now" to save the current inventory data to a file (data/inventory_data.json).

Loading Inventory:

Load previously saved inventory data from a JSON file.

File Structure

inventory-management-system/
│
├── main.py                  # Main Streamlit app
├── models/
│   ├── inventory.py        # Inventory class
│   ├── electronics.py      # Electronics class
│   ├── grocery.py          # Grocery class
│   └── clothing.py         # Clothing class
├── exceptions/
│   └── product_exists.py   # Custom exception for existing products
├── utils/
│   └── file_handler.py     # Functions to save and load data
└── data/
    └── inventory_data.json # Inventory data file
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Built with Streamlit for interactive web apps.

Inventory Management System uses Python and Object-Oriented Programming (OOP) principles for a structured approach.


"""
E-Commerce Product List – Python Exercises

Scenario:
You run a marketplace where partners send daily product data (like Amazon).
This script processes that data to identify pricing trends and sale issues.

Exercises:
1. Print products with price > 25
2. Show products that are on sale (name + price)
3. Create list of products on sale but missing a sale_price
4. Convert string prices to float and compare against threshold
"""

# Dataset
products = [
    {'id': 1, 'name': 't-shirt', 'price': '$12.99', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 2, 'name': 'shoes', 'price': '$22.45', 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 3, 'name': 'dress-shirt', 'price': '$43.00', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 4, 'name': 'socks', 'price': '$14.99', 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': 7.99},
    {'id': 5, 'name': 'trousers', 'price': '$32.50', 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 6, 'name': 'jacket', 'price': '$150.00', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
]

# Helper: Convert price string to float
def parse_price(price_str):
    return float(price_str.replace('$', ''))

# Exercise 1: Products with price > 25
print("\n🛍️ Products priced above $25:")
for product in products:
    if parse_price(product['price']) > 25:
        print(f"- {product['name']}")

# Exercise 2: Products on sale
print("\n🔥 Products currently on sale:")
for product in products:
    if product['is_on_sale']:
        print(f"- {product['name']}: {product['price']}")

# Exercise 3: Products on sale with missing sale price
print("\n⚠️ Products on sale but missing sale price:")
missing_sale_price = [
    product['name']
    for product in products
    if product['is_on_sale'] and not product['sale_price']
]
print(missing_sale_price)

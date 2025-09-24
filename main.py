import json
import os
import shutil

# List all available product from products (sample data)
def display_products(products):
    """Displays all available products with basic info."""
    print("--- Available Products ---")
    for item_id, item_data in products.items():
        print(f"[{item_id}] {item_data['name']}")
        print(f"    Price: ${item_data['price']:.2f} | Rating: {item_data['rating']}/5.0")
        print("-" * 20)

# Function 1: View product detail
def view_product(products):
    """Allows the user to view a product's details and reviews."""
    while True:
        display_products(products)
        item_id = input("\nEnter the product number to view (or 'q' to go back): ")
        if item_id.lower() == 'q':
            return

        if item_id in products:
            item = products[item_id]
            print("\n" + "=" * 30)
            print(f"Product: {item['name']}")
            print(f"Description: {item['description']}")
            print(f"Price: ${item['price']:.2f}")
            print(f"Rating: {item['rating']}/5.0")
            print("--- Reviews ---")
            if item['reviews']:
                for review in item['reviews']:
                    print(f"- \"{review}\"")
            else:
                print("No reviews yet.")
            print("=" * 30)
            break
        else:
            print("Invalid product number. Please try again.")

def main():
    """Main program loop."""
    # Copy products.sample.json to products.json when first time using this program
    if not os.path.exists('products.json'):
        shutil.copy('products.sample.json', 'products.json')
    with open('products.json', 'r') as f:
        products = json.load(f)
    print("Welcome to the Shopee Interactive Simulator!")
    while True:
        print("\nWhat would you like to do?")
        print("1. View Products")
        print("0. Exit")

        # Wait for user input
        choice = input("Enter your choice: ")

        if choice == "1":
            view_product(products)
        elif choice == "0":
            print("Thank you for using us. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

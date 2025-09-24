# Sample product data
products = {
    "1": {
        "name": "Cat T-shirt",
        "description": "A comfy, cotton t-shirt with a cute cat graphic.",
        "price": 15.00,
        "rating": 4.5,
        "reviews": [
            "Great shirt, soft material!",
            "Love the design, but the size is a bit small.",
        ],
    },
    "2": {
        "name": "Wireless Gaming Mouse",
        "description": "Ergonomic design with adjustable DPI.",
        "price": 50.00,
        "rating": 4.8,
        "reviews": [
            "Super responsive and comfortable to use.",
            "Battery life is fantastic.",
        ],
    },
    "3": {
        "name": "Reusable Coffee Mug",
        "description": "Eco-friendly, insulated mug for hot and cold drinks.",
        "price": 25.00,
        "rating": 4.2,
        "reviews": [
            "Keeps my coffee hot for hours. Highly recommend.",
            "Good quality, nice feel in my hand.",
        ],
    },
}

# List all available product from products (sample data)
def display_products():
    """Displays all available products with basic info."""
    print("--- Available Products ---")
    for item_id, item_data in products.items():
        print(f"[{item_id}] {item_data['name']}")
        print(f"    Price: ${item_data['price']:.2f} | Rating: {item_data['rating']}/5.0")
        print("-" * 20)

# Function 1: View product detail
def view_product():
    """Allows the user to view a product's details and reviews."""
    while True:
        display_products()
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
    print("Welcome to the Shopee Interactive Simulator!")
    while True:
        print("\nWhat would you like to do?")
        print("1. View Products")
        print("0. Exit")

        # Wait for user input
        choice = input("Enter your choice: ")

        if choice == "1":
            view_product()
        elif choice == "0":
            print("Thank you for using us. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

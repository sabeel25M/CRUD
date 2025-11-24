import uuid

# Global list to store the wishlist items.
# Each item is a dictionary: {'id': UUID, 'name': str, 'price': float, 'priority': str}
# We use a list to simulate a simple in-memory database.
wishlist = []

def generate_id():
    """Generates a unique, short UUID for the item ID."""
    # Using a shorter version of UUID for easier user input in the CLI
    return str(uuid.uuid4()).split('-')[0]

def add_item():
    """Prompts the user for item details and adds a new item to the wishlist."""
    print("\n--- Add New Item ---")
    name = input("Enter item name: ").strip()

    while True:
        try:
            price_input = input("Enter estimated price (e.g., 49.99): ").strip()
            # Convert to float, handling empty input as 0.0
            price = float(price_input) if price_input else 0.0
            if price < 0:
                print("Price cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid price format. Please enter a number.")

    while True:
        priority = input("Enter priority (High, Medium, Low): ").strip().capitalize()
        if priority in ['High', 'Medium', 'Low']:
            break
        print("Invalid priority. Must be 'High', 'Medium', or 'Low'.")

    new_item = {
        'id': generate_id(),
        'name': name,
        'price': price,
        'priority': priority
    }
    wishlist.append(new_item)
    print(f"\n✅ Item '{name}' added successfully with ID: {new_item['id']}\n")

def view_items():
    """Displays all items in the wishlist with formatting."""
    print("\n--- Your Shopping Wishlist ---")
    if not wishlist:
        print("Your wishlist is currently empty. Start adding some items!")
        return

    # Sort items by priority (High > Medium > Low) for better readability
    priority_order = {'High': 3, 'Medium': 2, 'Low': 1}
    sorted_wishlist = sorted(wishlist, key=lambda item: priority_order.get(item['priority'], 0), reverse=True)

    total_cost = sum(item['price'] for item in sorted_wishlist)

    print(f"{'ID':<8} {'Name':<35} {'Price':>10} {'Priority':<8}")
    print("-" * 62)

    for item in sorted_wishlist:
        price_str = f"${item['price']:.2f}"
        print(f"{item['id']:<8} {item['name'][:35]:<35} {price_str:>10} {item['priority']:<8}")

    print("-" * 62)
    print(f"Total Estimated Cost for {len(wishlist)} items: ${total_cost:.2f}\n")


def find_item_by_id(item_id):
    """Utility function to find an item dictionary by its unique ID."""
    for item in wishlist:
        if item['id'] == item_id:
            return item
    return None

def update_item():
    """Allows the user to modify an existing item's name, price, or priority."""
    print("\n--- Update Item ---")
    if not wishlist:
        print("Wishlist is empty. Nothing to update.\n")
        return

    view_items()
    item_id = input("Enter the ID of the item you want to update: ").strip()
    item = find_item_by_id(item_id)

    if not item:
        print(f"❌ Error: Item with ID '{item_id}' not found.\n")
        return

    print(f"Updating item: {item['name']} (Current Price: ${item['price']:.2f}, Priority: {item['priority']})")

    # Update Name
    new_name = input(f"Enter new name (or press Enter to keep '{item['name']}'): ").strip()
    if new_name:
        item['name'] = new_name

    # Update Price
    while True:
        new_price_input = input(f"Enter new price (or press Enter to keep ${item['price']:.2f}): ").strip()
        if not new_price_input:
            break
        try:
            new_price = float(new_price_input)
            if new_price < 0:
                 print("Price cannot be negative. Please try again.")
                 continue
            item['price'] = new_price
            break
        except ValueError:
            print("Invalid price format. Please enter a number.")

    # Update Priority
    while True:
        new_priority = input(f"Enter new priority (High, Medium, Low, or Enter to keep '{item['priority']}'): ").strip().capitalize()
        if not new_priority:
            break
        if new_priority in ['High', 'Medium', 'Low']:
            item['priority'] = new_priority
            break
        print("Invalid priority. Must be 'High', 'Medium', or 'Low'.")

    print(f"\n✅ Item '{item['name']}' (ID: {item_id}) updated successfully.\n")


def delete_item():
    """Allows the user to remove an item from the wishlist."""
    print("\n--- Delete Item ---")
    if not wishlist:
        print("Wishlist is empty. Nothing to delete.\n")
        return

    view_items()
    item_id = input("Enter the ID of the item you want to delete: ").strip()
    item_to_delete = find_item_by_id(item_id)

    if not item_to_delete:
        print(f"❌ Error: Item with ID '{item_id}' not found.\n")
        return

    # Remove the item from the list
    wishlist.remove(item_to_delete)
    print(f"\n🗑️ Item '{item_to_delete['name']}' (ID: {item_id}) deleted successfully.\n")


def main():
    """Main function to run the CLI application loop."""
    print("Welcome to the Python Shopping Wishlist CLI App!")

    while True:
        print("\n--- Menu ---")
        print("1. Add Item (Create)")
        print("2. View Wishlist (Read)")
        print("3. Update Item (Update)")
        print("4. Delete Item (Delete)")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_item()
        elif choice == '2':
            view_items()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            print("\nThank you for using the Wishlist App. Goodbye!")
            break
        else:
            print("\n❗ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
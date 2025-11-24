# CRUD
A Python CLI wishlist app that lets users add, view, update, and delete items. Each item has a name, price, priority, and unique ID. The app stores items in memory, sorts by priority, and provides an easy interactive shopping list manager.

🛍️ Python Shopping Wishlist CLI App

A simple, interactive command-line wishlist manager built in Python. Users can add, view, update, and delete wishlist items. Each item includes a name, price, priority, and unique ID. The program is perfect for beginners learning CRUD operations and CLI-based applications.

✨ Features

➕ Add items with auto-generated short UUIDs

📋 View wishlist in a formatted, priority-sorted table

✏️ Update any item’s name, price, or priority

🗑️ Delete items using their unique ID

📌 Priority sorting: High → Medium → Low

💾 No external libraries—fully in-memory

🚀 Getting Started
1. Save the script

Save your Python code as:

wishlist.py

2. Run the application
python wishlist.py

📜 Menu Options
Option	Description
1	Add Item
2	View Wishlist
3	Update Item
4	Delete Item
5	Exit
🧱 How Data Is Stored

Each item is stored as a Python dictionary:

{
  'id': 'abc123',
  'name': 'Item Name',
  'price': 49.99,
  'priority': 'High'
}

🧪 Example CLI Flow
--- Menu ---
1. Add Item
2. View Wishlist
3. Update Item
4. Delete Item
5. Exit
Enter your choice: 1


You are then guided through item details.

📂 Recommended Project Structure
wishlist.py
README.md

🛠 Requirements

Python 3.7 or higher

No external dependencies

🙌 Future Improvements (Optional Ideas)

Add file-based saving (JSON or CSV)

Add categories or tags

Add budgets or cost limits

Add a GUI or web version

📄 License

This project is free to use, modify, and share.

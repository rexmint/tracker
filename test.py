import tkinter as tk
from tkinter import ttk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import messagebox

class TrackerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tracker App")
        self.master.geometry("400x200")

        # create label
        label = tk.Label(self.master, text="Welcome to the Tracker App!", font=("Arial", 16))
        label.pack(pady=10)

        # create buttons
        add_item_btn = ttk.Button(self.master, text="Add new item", command=self.add_item)
        add_item_btn.pack(pady=5)

        view_items_btn = ttk.Button(self.master, text="View all items", command=self.view_items)
        view_items_btn.pack(pady=5)

    def add_item(self):
        pass

    def view_items(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TrackerApp(root)
    root.mainloop()

class AddItemForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Add New Item")

        # Create and place form fields
        date_label = Label(master, text="Date (YYYY-MM-DD): ")
        date_label.grid(row=0, column=0, padx=10, pady=10)
        self.date_entry = Entry(master, width=30)
        self.date_entry.grid(row=0, column=1)

        desc_label = Label(master, text="Item Description: ")
        desc_label.grid(row=1, column=0, padx=10, pady=10)
        self.desc_entry = Entry(master, width=30)
        self.desc_entry.grid(row=1, column=1)

        metal_label = Label(master, text="Precious Metal Class: ")
        metal_label.grid(row=2, column=0, padx=10, pady=10)
        self.metal_entry = Entry(master, width=30)
        self.metal_entry.grid(row=2, column=1)

        sealed_label = Label(master, text="Sealed (Yes/No): ")
        sealed_label.grid(row=3, column=0, padx=10, pady=10)
        self.sealed_entry = Entry(master, width=30)
        self.sealed_entry.grid(row=3, column=1)

        shipping_label = Label(master, text="Shipping Info (if sealed): ")
        shipping_label.grid(row=4, column=0, padx=10, pady=10)
        self.shipping_entry = Entry(master, width=30)
        self.shipping_entry.grid(row=4, column=1)

        weight_label = Label(master, text="Metal Weight (in troy oz): ")
        weight_label.grid(row=5, column=0, padx=10, pady=10)
        self.weight_entry = Entry(master, width=30)
        self.weight_entry.grid(row=5, column=1)

        storage_label = Label(master, text="Storage Location: ")
        storage_label.grid(row=6, column=0, padx=10, pady=10)
        self.storage_entry = Entry(master, width=30)
        self.storage_entry.grid(row=6, column=1)

        cost_label = Label(master, text="Cost: ")
        cost_label.grid(row=7, column=0, padx=10, pady=10)
        self.cost_entry = Entry(master, width=30)
        self.cost_entry.grid(row=7, column=1)

        # Add button to submit the form
        submit_button = Button(master, text="Add Item", command=self.submit_form)
        submit_button.grid(row=8, column=1, pady=20)

    def submit_form(self):
        # Get form values
        date = self.date_entry.get()
        desc = self.desc_entry.get()
        metal = self.metal_entry.get()
        sealed = self.sealed_entry.get()
        shipping = self.shipping_entry.get()
        weight = self.weight_entry.get()
        storage = self.storage_entry.get()
        cost = self.cost_entry.get()

        # Save the data to the database or file
        # ...

        # Show success message
        messagebox.showinfo("Success", "Item added successfully!")
        self.master.destroy()

def add_item():
    # Create an instance of the AddItemForm class
    form = AddItemForm(root)
    root.wait_window(form.top)  # Wait for the form to be closed

    # Get the values entered in the form
    date = form.date_entry.get()
    item_desc = form.item_desc_entry.get()
    metal_class = form.metal_class_entry.get()
    sealed = form.sealed_entry.get()
    shipping_info = form.shipping_info_entry.get()
    metal_weight = form.metal_weight_entry.get()
    storage_location = form.storage_location_entry.get()
    cost = form.cost_entry.get()

    # Save the values to the database or file
    # TODO: Implement this
    print(date, item_desc, metal_class, sealed, shipping_info, metal_weight, storage_location, cost)

def view_items():
    """Load a new window that displays a table of all the items in the database"""

    # Create a new window for displaying the table
    view_items_window = tk.Toplevel(root)
    view_items_window.title("View All Items")

    # Create a treeview widget for displaying the table
    table = ttk.Treeview(view_items_window)

    # Define the columns of the table
    table["columns"] = (
        "Date",
        "Item Description",
        "Metal Class",
        "Sealed",
        "Shipping Info",
        "Metal Weight (troy oz)",
        "Storage Location",
        "Cost"
    )

    # Set the column headings
    table.heading("#0", text="ID")
    table.heading("#1", text="Date")
    table.heading("#2", text="Item Description")
    table.heading("#3", text="Metal Class")
    table.heading("#4", text="Sealed")
    table.heading("#5", text="Shipping Info")
    table.heading("#6", text="Metal Weight (troy oz)")
    table.heading("#7", text="Storage Location")
    table.heading("#8", text="Cost")

    # Retrieve all items from the database and populate the table
    items = get_all_items()
    for item in items:
        table.insert(parent="", index="end", iid=item[0], text=item[0], values=item[1:])

    # Pack the table into the window and display it
    table.pack(expand=True, fill="both")

def get_all_items():
    items = []  # Define the items variable
    with open('items.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            items.append(row)
    return items
    
def add_new_items():
    # Create a new instance of the NewItem class
    new_item_window = NewItem()

    # Make the new item window modal
    new_item_window.grab_set()
    root.wait_window(new_item_window)

    # Reload the item list to show the newly added item
    load_items()

from tkinter import *
import tkinter as tk

def add_item_window():
    window = Toplevel(root)
    window.title("Add New Item")
    window.geometry("400x400")

    date_label = Label(window, text="Date")
    date_label.pack()

    date_entry = Entry(window)
    date_entry.pack()

    item_label = Label(window, text="Item Description")
    item_label.pack()

    item_entry = Entry(window)
    item_entry.pack()

    metal_label = Label(window, text="Precious Metal Class")
    metal_label.pack()

    metal_entry = Entry(window)
    metal_entry.pack()

    sealed_label = Label(window, text="Sealed (yes/no)")
    sealed_label.pack()

    sealed_entry = Entry(window)
    sealed_entry.pack()

    ship_label = Label(window, text="Shipping Info (if sealed)")
    ship_label.pack()

    ship_entry = Entry(window)
    ship_entry.pack()

    weight_label = Label(window, text="Metal Weight (in troy oz)")
    weight_label.pack()

    weight_entry = Entry(window)
    weight_entry.pack()

    storage_label = Label(window, text="Storage Location")
    storage_label.pack()

    storage_entry = Entry(window)
    storage_entry.pack()

    cost_label = Label(window, text="Cost")
    cost_label.pack()

    cost_entry = Entry(window)
    cost_entry.pack()

    submit_button = Button(window, text="Add Item", command=add_item)
    submit_button.pack()

def add_item():
    print("Adding new item")

def view_all_items():
    items = []

    with open("items.txt", "r") as f:
        for line in f:
            item = line.strip().split(",")
            items.append(item)

    for item in items:
        print(item)

root = Tk()
root.title("Precious Metals Tracker")
root.geometry("400x400")

add_item_button = Button(root, text="Add new item", command=add_item_window)
add_item_button.pack()

view_all_items_button = Button(root, text="View all items", command=view_all_items)
view_all_items_button.pack()

root.mainloop()
    

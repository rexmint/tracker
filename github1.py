import tkinter as tk
from tkinter import ttk

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

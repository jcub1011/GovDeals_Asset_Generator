import tkinter as tk
from tkinter import ttk


class DragReorderList(tk.Frame):
    """
    A list that the user can reorder by dragging and dropping items in the list.
    """
    def __init__(self, parent: tk.Widget):
        super().__init__(parent)
        print("Making drag reorder list.")
        self.items = []

    def add(self, item: tk.Widget):
        item_container = tk.Frame(self)
        drag_handle = tk.Box

        self.items.append(item)
        item.grid(row=len(self.items) - 1)



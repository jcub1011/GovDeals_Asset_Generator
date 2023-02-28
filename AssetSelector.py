import tkinter as tk
from tkinter import ttk
from Directories import Directories
import os
import json


class AssetSelector(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Init directories.
        self.dir = Directories()
        # Create Window
        self.grid(sticky=tk.W)
        # Create Brand Selector
        self.brand = tk.Frame(self)
        # Create Model Selector
        self.model = tk.Frame(self)
        # Create display.
        self.display = tk.Label(
            self,
            text="Asset will display here.",
            justify=tk.LEFT,
            padx=5,
            pady=10
        )
        # TODO: Use treeview to allow the user to pick out an asset.

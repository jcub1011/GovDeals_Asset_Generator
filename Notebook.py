import tkinter as tk
from tkinter import ttk
from TemplateSelector import TemplateSelector
from AssetSelector import AssetSelector
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GovDeals Asset Generator")
        # Gets window and display dimensions and calculates center position.
        window_width = 1000
        window_height = 800
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        self.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        # Create notebook.
        self.main_frame = ttk.Notebook(self)
        self.main_frame.pack(expand=True, fill=tk.BOTH)
        # Add frames.
        # self.main_frame.add(self.create_main_window(), text="Menu")
        self.main_frame.add(TemplateSelector(self.main_frame), text="Templates")
        self.main_frame.add(AssetSelector(self.main_frame), text="Asset Selector")
        self.mainloop()

    def create_main_window(self):
        """
        Creates the main window.
        :return: ttk.Frame
        """
        # Create Window
        window = ttk.Frame(self.main_frame)
        window.pack(expand=True, fill=tk.BOTH)
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)
        window.rowconfigure(2, weight=1)
        # Create Buttons
        template_asset = ttk.Button(
            window,
            text="Create Asset from Template"
        )
        template_asset.grid(
            column=0,
            row=0
        )

        reuse_asset = ttk.Button(
            window,
            text="Create Asset Using Existing Asset"
        )
        reuse_asset.grid(
            column=0,
            row=1
        )

        scratch_asset = ttk.Button(
            window,
            text="Create Asset From Scratch"
        )
        scratch_asset.grid(
            column=0,
            row=2
        )

        return window

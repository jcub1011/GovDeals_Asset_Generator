import tkinter as tk
from AssetGenerator import AssetGenerator
from TemplateWindow import TemplateWindow


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Asset Generator - GovDeals")

        # Gets window and display dimensions and calculates center position.
        window_width = 800
        window_height = 800
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        self.geometry_string = f"{window_width}x{window_height}+{center_x}+{center_y}"

        self.geometry(self.geometry_string)

        self.create_buttons()

        self.mainloop()

    def create_buttons(self):
        asset_button = tk.Button(
            self,
            text="Create Asset From Scratch",
            command=self.create_asset_from_scratch
        )
        template_button = tk.Button(
            self,
            text="Create Asset From a Template",
            command=self.create_asset_from_template
        )
        existing_asset_button = tk.Button(
            self,
            text="Create Asset From Existing Asset",
            command=lambda: print("Creating an asset from other asset.")
        )

        asset_button.pack(
            ipadx=2,
            ipady=2,
            expand=True
        )
        template_button.pack(
            ipadx=2,
            ipady=2,
            expand=True
        )
        existing_asset_button.pack(
            ipadx=2,
            ipady=2,
            expand=True
        )

    def create_asset_from_scratch(self):
        print("Creating an asset from scratch.")


    def create_asset_from_template(self):
        print("Creating an asset from template.")
        TemplateWindow(self.geometry_string).mainloop()




import tkinter as tk
from tkinter import ttk
import os
from Directories import Directories
from AssetGeneratorWindow import AssetGeneratorWindow
import json


class TemplateWindow(tk.Tk):
    def __init__(self, geometry_string: str):
        """
        Creates a new window that allows the user to select a template.
        :param geometry_string: The settings to insert into geometry.
        """
        super().__init__()
        self.title("Templates - GovDeals")
        self.geo_string = geometry_string
        self.geometry(geometry_string)
        self.dir = Directories()

        # Combobox
        self.template = ttk.Combobox(self)
        self.selected_template = {}

        # Initialize the combobox.
        self.init_template_combobox()

        # Template Display Area
        self.template_display = tk.Label(
            self,
            text="Template will display here.",
            justify=tk.LEFT,
            padx=5,
            pady=10
        )
        self.template_display.pack()

        # Init the selector button.
        self.select = tk.Button(
            self,
            text="Select This Template",
            command=self.select_template,
            state=tk.DISABLED
        )
        self.select.pack()

    def init_template_combobox(self):
        """
        Initializes the combobox.
        :return: None
        """
        # Get templates
        template_folder_files = os.listdir(self.dir.template)

        json_file_list = []
        for file in template_folder_files:
            file = file.split(".")
            # Checks if the file extension is json.
            if file[1] == "json":
                json_file_list.append(file[0])

        # Button Definitions
        template_label = tk.Label(
            self,
            text="Select a template:"
        )
        self.template["values"] = json_file_list
        self.template["state"] = "readonly"
        # Setup function bind.
        self.template.bind('<<ComboboxSelected>>', self.display_template)
        # Display Button
        template_label.pack()
        self.template.pack()

    def display_template(self, *args):
        """
        Displays the selected template in template_display.
        :param args: Never used.
        :return: None
        """
        print("Template changed.")
        file_name = self.template.get()
        template_string = ""

        # Get template text.
        with open(f"{self.dir.template}\\{file_name}.json") as template_file:
            try:
                self.selected_template = json.load(template_file)
                for item in self.selected_template.values():
                    for key, value in item.items():
                        template_string += f"{key}: {value}\n"

                self.select.configure(state=tk.NORMAL)

            except json.JSONDecodeError:
                self.select.configure(state=tk.DISABLED)
                template_string = "Selected template is empty or has invalid json."

        # Update Text
        self.template_display.configure(text=template_string)

    def select_template(self):
        print("Selected template.")
        AssetGeneratorWindow(self.geo_string, self.selected_template).mainloop()

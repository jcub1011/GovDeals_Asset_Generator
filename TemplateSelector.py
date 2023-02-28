import tkinter as tk
from tkinter import ttk
from Directories import Directories
from GenerateAsset import AssetGenerator
import os
import json


class TemplateSelector(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # Init directories.
        self.dir = Directories()
        # Create Window
        self.grid()
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        # Create Template Display
        self.display = tk.Label(
            self,
            text="Template will display here.",
            justify=tk.LEFT,
            padx=5,
            pady=10
        )
        # Get templates list.
        template_folder_files = os.listdir(self.dir.template)

        json_file_list = []
        for file in template_folder_files:
            file_name, file_extension = file.split(".", maxsplit=1)
            # Checks if the file extension is json.
            if file_extension == "json":
                json_file_list.append(file_name)

        # Make Combo Box
        self.template_label = tk.Label(
            self,
            text="Select a template:"
        )
        self.template_selector = ttk.Combobox(self)
        self.template_selector["values"] = json_file_list
        self.template_selector["state"] = "readonly"
        # Create selector button.
        self.select_button = tk.Button(
            self,
            state=tk.DISABLED,
            text="Select Template",
            command=self.select_template
        )
        # Setup function binds.
        self.template_selector.bind('<<ComboboxSelected>>', self.update_display)
        # Store Selected Asset
        self.selected_template = {}
        # Display Everything
        self.template_label.grid(column=0, row=0, sticky=tk.E)
        self.template_selector.grid(column=1, row=0, sticky=tk.W)
        self.select_button.grid(column=2, row=0, sticky=tk.W)
        self.display.grid(column=0, row=1, columnspan=3)

    def update_display(self, evt):
        print(evt)
        file_name = self.template_selector.get()
        template_string = ""

        # Get template text.
        with open(f"{self.dir.template}\\{file_name}.json") as template_file:
            try:
                # Load template.
                self.selected_template = json.load(template_file)
                for item in self.selected_template.values():
                    for key, value in item.items():
                        template_string += f"{key}: {value}\n"

                self.select_button.configure(state=tk.NORMAL)

            except json.JSONDecodeError:
                # When template is invalid.
                self.select_button.configure(state=tk.DISABLED)
                template_string = "Selected template is empty or has invalid json."

        # Update Text
        self.display.configure(text=template_string)

    def select_template(self):
        print("Selected template.")
        AssetGenerator(self.parent, self.selected_template)

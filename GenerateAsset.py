import tkinter as tk
from tkinter import ttk


class AssetGenerator(tk.Frame):
    def __init__(self, parent, asset_base: dict = None):
        super().__init__(parent)
        self.parent = parent
        self.name = "New Asset"

        # Add tab to notebook.
        parent.add(self, text=self.name)
        parent.select(self)
        close_button = tk.Button(self, text="Delete Tab", command=self.close)
        close_button.grid(sticky=tk.NE)

        # Add required keys.
        necessary_keys = ["Head", "Specs", "Foot"]
        for key in necessary_keys:
            if key not in asset_base.keys():
                asset_base[key] = {}

        # Load Asset Info
        self.asset = asset_base

        # Display Asset
        self.create_displays()

    def close(self, evt=None):
        print(f"Deleting '{self.name}'.")
        self.parent.forget(self)

    def update_tab_name(self, new_name: str):
        """
        Changes the name of the tab.
        :param new_name: Name of the tab.
        :return: None.
        """
        self.name = new_name
        self.parent.tab(self, text=new_name)

    def create_displays(self):
        """
        Creates the frames that hold the asset info.
        :return: None.
        """
        # Display header.
        self.display_paragraph("Header", self.asset["Head"])
        # Display specs.
        spec_container = tk.Frame(self)
        self.display_specs(spec_container, "Specifications", self.asset["Specs"])
        spec_container.grid()
        # Display footer.
        self.display_paragraph("Footer", self.asset["Foot"])

    def display_paragraph(self, name, paragraphs):
        """
        Displays an entry whose values have multiple lines.
        :param name: The label of the frame surrounding the entries.
        :param paragraphs: The the entries.
        :return: None
        """
        # Create asset frame.
        asset_frame = ttk.LabelFrame(self, text=name)
        asset_frame.grid()
        row = 0
        # Generate list of values.
        for key, value in paragraphs.items():
            name = tk.Entry(asset_frame)
            name.insert(index=0, string=key)
            name.grid(row=row, column=0)
            # Generate input box.
            paragraph = tk.Text(asset_frame, height=3)
            paragraph.insert("0.0", value)
            paragraph.grid(row=row, column=1)
            # Increment
            row += 1
            # TODO: NEEDS TESTING

        add_button = tk.Button(asset_frame, text="Add Entry")

    def add_multiline_entry(self, parent, name: str, value: str = ""):
        pass    # TODO: Implement

    def display_specs(self, container: tk.Frame, name: str, specs: dict):
        """
        Creates a frame whose entries use one line.
        :param container: Where to stick the specs in.
        :param name: The name of the frame surrounding the entries.
        :param specs: The entries to put within.
        :return: None
        """
        # Create asset frame.
        asset_frame = ttk.LabelFrame(container, text=name)
        columns = container.grid_size()[1]
        asset_frame.grid(row=1, column=columns)
        row = 0
        # Generate list of values.
        for key, value in specs.items():
            if type(value) is dict:
                value = {"Key": "Value"}  # For testing.
                self.display_specs(container, key, value)
                continue

            # Generate Name
            name = tk.Entry(asset_frame)
            name.insert(0, key)
            name.grid(row=row, column=0)
            # Generate Input Box
            spec = tk.Entry(asset_frame)
            spec.insert(0, value)
            spec.grid(row=row, column=1)
            # Increment row.
            row += 1

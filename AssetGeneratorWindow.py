import tkinter as tk
from tkinter import ttk


class AssetGeneratorWindow(tk.Tk):
    def __init__(self, geometry_string: str, asset: dict):
        super().__init__()
        self.title("Generator - GovDeals")
        self.geometry(geometry_string)
        self.asset = asset

        # Layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=3)
        self.rowconfigure(2, weight=1)

        # Frames
        self.head = ttk.LabelFrame(self, text="Header")
        self.specs = ttk.LabelFrame(self, text="Specifications")
        self.foot = ttk.LabelFrame(self, text="Footer")

        # Init Frames
        self.create_head_entries()
        self.create_spec_entries()

    def create_head_entries(self):
        # Create outline
        self.head.grid(column=0, row=0, sticky=tk.NW)
        self.head.columnconfigure(0, weight=1)
        self.head.columnconfigure(1, weight=3)
        self.head.rowconfigure(0, weight=1)

        row = 0
        for key, value in self.asset["Head"].items():
            # Create widgets.
            label = tk.Entry(
                self.head
            )
            label.insert(0, key)
            text_box = tk.Text(
                self.head,
                height=4,
                padx=5,
                pady=5
            )
            text_box.insert(index='1.0', chars=value)

            # Widget layout.
            label.grid(row=row, column=0)
            text_box.grid(row=row, column=1)

            row += 1

        add_button = tk.Button(
            self.head,
            text="Add Item",
            command=lambda: print("Adding item to head.")
        )
        add_button.grid(sticky=tk.NW)

    def create_spec_entries(self):
        self.specs.grid(column=0, row=1, sticky=tk.NW, columnspan=2)
        self.specs.columnconfigure(0, weight=1)
        self.specs.columnconfigure(1, weight=3)
        self.specs.rowconfigure(0, weight=1)

        self.create_new_sheet(self.asset["Specs"], "Specifications")
        # TODO: Fix the index error with accessing the new sheet.
        """
        for key, value in self.asset["Specs"].items():
            if type(value) is dict:
                self.create_new_sheet(value, key)
            if type(value) is dict:
                # Create container.
                print("dictionary")
                label_frame = tk.LabelFrame(
                    self.specs,
                    text=key
                )
                label_frame.grid(column=2, sticky=tk.NW)
                label_frame.columnconfigure(0, weight=1)
                label_frame.columnconfigure(1, weight=3)
                print("Created frame")

                # Insert entries into frame.
                inner_row = 0
                for inner_key, inner_value in self.asset["Specs"][key].items():
                    print("Inserting io")
                    label = tk.Label(
                        label_frame,
                        text=inner_key
                    )
                    entry = tk.Entry(
                        label_frame
                    )
                    entry.insert(0, inner_value)

                    label.grid(row=inner_row, column=0)
                    label.grid(row=inner_row, column=1)

                    inner_row += 1

                # Insert add button.
                add_button = tk.Button(
                    label_frame,
                    text="Add IO",
                    command=lambda: print("Adding IO.")
                )
                add_button.grid(column=0, sticky=tk.NW)
            else:
                # Create widgets.
                self.add_spec_entry(self.winfo_children()[1], key, value)
            


        # Create add button.
        add_button = tk.Button(
            self.specs,
            text="Add Item",
            command=lambda: self.add_spec_entry(self.winfo_children()[1])
            # Index 1 is the index of the spec frame.
        )
        add_button.grid(column=0, sticky=tk.NW)
        """

    def add_spec_entry(self, container_to_add_to, key="", value=""):
        # TODO: Make add button appear below the new entry.
        print(container_to_add_to)
        current_row = container_to_add_to.grid_size()[1]
        print(current_row)
        print("Adding spec entry.")
        # Name of entry.
        label = tk.Entry(
            container_to_add_to
        )
        label.insert(0, key)
        label.grid(
            row=current_row,
            column=0
        )
        # Value of entry.
        entry = tk.Entry(
            self.winfo_children()[1]
        )
        entry.insert(0, value)
        entry.grid(
            row=current_row,
            column=1
        )

    def create_new_sheet(self, dictionary: dict, sheet_name: str):
        print(f"Making {sheet_name} sheet.")
        # Create container.
        current_col = self.winfo_children()[1].grid_size()[0]

        label_frame = tk.LabelFrame(
            self.specs,
            text=sheet_name
        )
        label_frame.grid(
            column=current_col,
            sticky=tk.NW
        )
        label_frame.columnconfigure(0, weight=1)
        label_frame.columnconfigure(1, weight=3)
        print("Created frame")

        # Insert entries into frame.
        for key, value in dictionary.items():
            if type(value) is dict:
                self.create_new_sheet(value, key)

            else:
                print(f"Inserting item {key}: {value}")
                self.add_spec_entry(
                    self.winfo_children()[1].winfo_children()[current_col],
                    key, value
                )

        # Insert add button.
        add_button = tk.Button(
            label_frame,
            text="Add Entry",
            command=lambda: print("Adding entry.")
        )
        add_button.grid(column=0, sticky=tk.NW)


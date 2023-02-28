import json
import os
from Directories import Directories
from Asset import Asset
from InputProcessor import InputProcessor as Input


class AssetGenerator:
    def __init__(self):
        print("Asset Generator Started")
        self.directory = Directories()

    def generate_laptop(self, template=False, existing=False):
        if template:
            with open(f"{self.directory.template}\\Laptop.json") as json_file:
                laptop = Asset(json_file)
                laptop.fill_out_asset()
        


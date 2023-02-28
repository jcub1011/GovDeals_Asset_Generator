import os


class Directories:
    def __init__(self):
        self.program = os.getcwd()
        self.disclaimer = self.program + "\\Disclaimers"
        self.index = self.program + "\\Index"
        self.template = self.program + "\\AssetTemplates"

    @classmethod
    def make_directory(cls, directory):
        if os.path.exists(directory):
            print("Directory already exists!")
        else:
            print("Making directory.")
            os.mkdir(directory)
    
    def init_directories(self):
        self.make_directory(self.disclaimer)
        self.init_disclaimers()
        self.make_directory(self.index)

    def init_disclaimers(self):
        # Creates any missing text files if necessary.
        file_names = [
            "inspection_instructions",
            "long_desc_retire_disclaimer",
            "long_desc_pickup_disclaimer",
            "payment_instructions",
            "removal_instructions",
            "special_instructions"
        ]
        for name in file_names:
            with open(f"{self.disclaimer}\\{name}.txt", mode='a') as temp:
                print(temp.name)

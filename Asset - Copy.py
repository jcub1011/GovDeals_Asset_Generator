import json

class Asset:
    def __init__(self):
        print("Making new asset.")
        self.yes_input = {"y", ""}
        self.body = {}
        self.specs = {}
        self.name = self.get_safe_input("Enter item name: ")
        
    def __init__(self, json_file):
        print("Making new asset.")
        self.yes_input = {"y", ""}
        self.name = self.get_safe_input("Enter item name: ")
        self.body = {}
        self.specs = {}
        temp = json.loads(json_file.read())
        for key, value in temp.items():
            if key == "Specifications":
                self.specs = value
            else:
                self.body[key] = value
        
    def print(self):
        for key, value in self.body.items():
            print(key, value)
        for key, value in self.specs.items():
            print(key, value)

    def get_safe_input(self, prompt):
        """Gets an input from the user that they must then approve."""
        user_input = input(prompt)
        if user_input == "":
            print("This field will be left blank.")
        else:
            print("You entered: '" + user_input + "'")

        # Check if user wants to submit input.
        if input("Use this input? (enter 'y' or leave blank and press enter for yes) ").lower() in self.yes_input:
            return user_input
        else:
            return self.get_safe_input(prompt)
            
    def read_in_json(self, json_file):
        """Creates an asset using a JSON File."""
        print("Reading in template.")
        print(json.loads(json_file.read()))

    def add_compute(self):
        """Adds a CPU, RAM, and Storage attribute to the asset."""
        print("Adding CPU, RAM, and Storage attributes.")
        self.specs["CPU"] = self.get_safe_input("Enter the CPU spec: ")
        self.specs["RAM"] = self.get_safe_input("Enter the RAM spec: ")
        self.specs["Storage"] = self.get_safe_input("Enter the Storage spec: ")

    def add_display(self):
        """Adds display size and resolution attributes to the asset."""
        print("Adding Size and Resolution attributes.")
        self.specs["Size"] = self.get_safe_input("Enter the diagonal dimension: ")
        self.specs["Resolution"] = self.get_safe_input("Enter the resolution: ")

    def add_battery(self):
        """Adds a battery attribute to the asset."""
        print("Adding battery attribute.")
        self.specs["Battery Capacity"] = self.get_safe_input("Enter the battery capacity: ")

    def add_io(self):
        """Adds an io sheet to the asset."""
        print("Adding IO attribute.")
        print("To stop adding IO, leave the 'IO Type: ' entry blank.")
        user_input = self.get_safe_input("IO Type")
        io_sheet = {}
        while user_input != "":
            # Empty string is how user stops adding io.
            try:
                io_sheet[user_input] = int(self.get_safe_input("Enter quantity (number only): "))
                user_input = self.get_safe_input("IO Type")
            except ValueError:
                print("That isn't a valid number.")

        self.specs["IO"] = io_sheet

    def add_custom(self, attribute_name, attribute_value):
        """Adds a custom attribute to the asset."""
        print("Adding custom attribute '" + attribute_name + "'.")
        self.specs[attribute_name] = attribute_value




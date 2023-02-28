import json
from InputProcessor import InputProcessor as Input


class Asset:
    def __init__(self):
        """
        Creates an asset.
        """
        print("Making new asset.")
        self.name = Input.get_safe_input("Enter item name: ")
        self.header = {}
        self.specs = {}
        self.footer = {}

    def __init__(self, json_file):
        """
        Creates a new asset.
        :param json_file: The json file to base the asset on.
        """
        print("Making new asset.")
        self.name = Input.get_safe_input("Enter item name: ")
        self.header = {}
        self.specs = {}
        self.footer = {}
        temp = json.loads(json_file.read())
        for key, value in temp.items():
            if key.lower() == "head":
                self.header = value
            elif key.lower() == "specs":
                self.specs = value
            elif key.lower() == "foot":
                self.footer = value
            else:
                print("Unknown identifier: '" + key + "'.")
                print("Valid specifiers are: 'head', 'specs', and 'foot'.")

    def print(self):
        """
        Prints the asset.
        :return: None.
        """
        for key, value in self.header.items():
            print(key, value, sep=" - ")

        for key, value in self.specs.items():
            if type(value) is dict:
                print(key + ":")
                for inner_key, inner_value in value.items():
                    print(inner_key, inner_value, sep=" | ")
            else:
                print(key, value, sep=": ")

        for key, value in self.footer.items():
            print(key, value, sep=" - ")

    @classmethod
    def fill_out_dict(cls, dictionary):
        """Uses user input to fill out information fields.
        :param dictionary: The dictionary to fill in values for.
        :return: Dictionary
        """
        empty_values = ("", " ")
        temporary_dict = {}
        for key, value in dictionary.items():
            if type(value) is dict:
                temporary_dict[key] = cls.fill_out_dict(value)
            else:
                if value in empty_values:
                    temporary_dict[key] = Input.get_safe_input("Enter value for '" + key + "':")
                else:
                    if Input.get_bool_input("Would you like to replace\n'" + value + "'\n in '" + key + "'? "):
                        temporary_dict[key] = Input.get_safe_input("Enter value for '" + key + ":")
                    else:
                        temporary_dict[key] = value

        return temporary_dict

    def fill_out_asset(self):
        """Gets user input to fill out information fields.
        """
        self.specs = self.fill_out_dict(self.specs)
        self.footer = self.fill_out_dict(self.footer)
        self.header = self.fill_out_dict(self.header)

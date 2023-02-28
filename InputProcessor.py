class InputProcessor:
    @classmethod
    def get_safe_input(cls, prompt, yes_input=("y", "")):
        """
        Gets an input from the user that they must then approve.
        :param prompt: What to ask the user.
        :param yes_input: What is considered yes.
        :return: String.
        """
        user_input = input(prompt + "\n")
        if user_input == "":
            print("This field will be left blank.")
        else:
            print("You entered: '" + user_input + "'")

        # Check if user wants to submit input.
        if input("Use this input? (enter 'y' or leave blank and press enter for yes)\n").lower() in yes_input:
            return user_input
        else:
            return cls.get_safe_input(prompt)

    @staticmethod
    def get_bool_input(prompt, yes_input=("y", "")):
        """
        Gets a bool input from the user.
        :param prompt: What to ask the user.
        :param yes_input: What is considered a yes.
        :return: Boolean.
        """
        if input(prompt + "(enter 'y' or leave blank to select yes)\n") in yes_input:
            return True
        else:
            return False

    @staticmethod
    def lowercase(string):
        return string.lower()

    @classmethod
    def get_input_from_list(cls, prompt, options):
        print("Select one of these options:\n")
        options_lower = map(cls.lowercase, options)
        for number, value in enumerate(options, 1):
            print(number, value, sep=". - ")

        user_input = cls.get_safe_input(prompt)
        print("You entered: '" + user_input + "'")

        if user_input.lower() in options_lower:
            return user_input
        elif user_input.lower() in map(str, range(1, len(options) + 1)):
            return options[int(user_input)]
        else:
            return cls.get_input_from_list(prompt, options)

class RomanNumeral: 
    """A class to represent our roman numerals or integers."""
    def __init__(self, input): 
        """Initializes the user's input, a counter, and standard values for each roman numeral."""
        self.input = input
        self.rom_dict = {u'M\u0305': 1000000, u'C\u0305M\u0305': 900000, u'D\u0305': 500000, \
                    u'C\u0305D\u0305': 400000, u'C\u0305': 100000, u'X\u0305C\u0305': 90000, \
                    u'L\u0305': 50000, u'X\u0305L\u0305': 40000, u'X\u0305': 10000, \
                    u'I\u0305X\u0305': 9000, u'V\u0305': 5000, u'I\u0305V\u0305': 4000, 'M': 1000, \
                    'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, \
                    'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    
    @classmethod
    def user_input(cls):
        while True:
                print("Press 'Enter' without an input to exit program.")
                ui = (input("Enter a Roman Numeral or integer to convert: "))
                if ui == "":
                    return  # return > exit(), because this is in a function
                x = RomanNumeral(ui)
                x.rom_or_int()
                # will continue to loop, until user enters a null string as input

    def rom_or_int(self):
            """Checks if user input is a roman numeral, integer, or not."""
            # Checks if user input is a integer
            if self.input.isdigit():
                number = int(self.input)
                print("The equivalent Roman Numeral is: " + self.int_to_rom(number) + ".\n")
            # Checks if user input is a roman numeral, if so run method 
            elif self.isroman():
                self.rom_to_int()
            # If not, print this statement
            else:
                print("Entry is neither in roman numerals or an integer.\n")

    def isroman(self):
        """Checks if user input is a roman numeral."""
        for i in self.input:
            if i not in self.rom_dict.keys():
                return False
        return True

    def int_to_rom(self, number):
        """Takes the user input of integer and converts it to Roman Numerals."""
        # Create a list of tuples for the standard values of the roman numerals
        roman_numeral = "" # empty string to create roman numeral

        for k,v in self.rom_dict.items():
            if number - v >= 0: # finds the greatest integer value that can be subtracted from input
                x = number // v # x is the number of times the current roman numeral appears
                number -= x*v # subtract the input from the roman numeral to be added to the string
                roman_numeral += x * k # the string is now x amount of the roman numeral
        return roman_numeral
            
    def rom_to_int(self): # next() function? LXD and DXL give wrong answers.
        """Takes in user_input in roman numerals and return the equivalent integer."""
        rom_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        integer = 0 # counter

        # Iterates the user's input
        for i in range(len(self.input)):
            roman_value = rom_dict[self.input[i]] # checks the integer value of the current iteration

            # if the subceding roman numeral is of greater value, subtract
            if i+1 < len(self.input) and roman_value < rom_dict[self.input[i+1]]:
                integer -= roman_value
            else: # if not add
                integer += roman_value
        
        # checks to see if this is a valid Roman Numeral by comparing to the output of the int_to_rom method
        check_value = self.int_to_rom(integer)
        if self.input == check_value:
            print("The equivalent integer value is: " + str(integer) + ".\n")
            return integer
        else:
            print("This is not a proper roman numeral.\n")

if __name__ == '__main__':
    start_program = RomanNumeral.user_input()
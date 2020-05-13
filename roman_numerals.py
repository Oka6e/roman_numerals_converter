class RomanNumeral: 
    """A class to represent our roman numerals or integers."""
    def __init__(self, number): 
        """Initializes the user's input, a counter, and standard values for each roman numeral."""
        self.number = number
        self.int_num = 0 # counter
        self.rom_num = ''
        self.rom_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} 

    def rom_to_int(self): # next() function? LXD and DXL give wrong answers.
        """Takes in user_input in roman numerals and return the equivalent integer."""
        for i in range(len(self.number)-1): # iterates through the string of roman numerals.
            # subtraction rules
            if self.number[i] == 'I' and (self.number[i+1] == 'V' or self.number[i+1] == 'X'):
                self.int_num -= 1
                continue
            elif self.number[i] == 'X' and (self.number[i+1] == 'L' or self.number[i+1] == 'C'):
                self.int_num -= 10
                continue
            elif self.number[i] == 'C' and (self.number[i+1] == 'D' or self.number[i+1] == 'M'):
                self.int_num -= 100
                continue
            # or add roman numerals normally
            else:
                for k, v in self.rom_dict.items():
                    if self.number[i] == k:
                        self.int_num += v

        # Add the last roman numeral
        for k,v in self.rom_dict.items():
            if self.number[-1] == k:
                self.int_num += v
  
        return self.int_num
    
    def int_to_rom(self):
        """Takes the user input of integer and converts it to Roman Numerals."""
        self.rom_lst = list(self.rom_dict.items()) # creates a list of the values of roman numerals
        rev_rom_lst = self.rom_lst[::-1] # reverse the list order from greatest to least
        number = int(self.number)
        lst_len = len(rev_rom_lst)
        i = 0
        while i < lst_len:
            if number - rev_rom_lst[i][1] >= 0:
                number -= rev_rom_lst[i][1]
                self.rom_num += rev_rom_lst[i][0]
            elif i%2 == 0 and i < lst_len - 2 and number - (rev_rom_lst[i][1] - rev_rom_lst[i+2][1]) >= 0:
                number -= rev_rom_lst[i][1] - rev_rom_lst[i+2][1]
                self.rom_num += rev_rom_lst[i+2][0] + rev_rom_lst[i][0]
                i += 1
            elif i < lst_len - 1  and number - (rev_rom_lst[i][1] - rev_rom_lst[i+1][1]) >= 0:
                number -= rev_rom_lst[i][1] - rev_rom_lst[i+1][1]
                self.rom_num += rev_rom_lst[i+1][0] + rev_rom_lst[i][0]
                i += 1
            else:
                i += 1
        return self.rom_num
        
    def isroman(self):
        """Checks if user input is a roman numeral."""
        for i in self.number:
            if i not in self.rom_dict.keys():
                return False
        if self.IXC_triple_rules():
            return False
        elif self.precedence_rules():
            return False
        return True

    def roman_or_int(self):
        """Checks if user input is a roman numeral, integer, or not."""
        if self.number.isdigit():
            print(self.int_to_rom())
        elif self.isroman():
            print("The integer value is: " + str(self.rom_to_int()) + ".\n")
        else:
            print("Entry is neither in roman numerals or an integer.\n")
    
    def IXC_triple_rules(self):
        """Tag if user input has more than 3 I, X, or C in a row."""
        if "IIII" in self.number or "XXXX" in self.number or "CCCC" in self.number:
            print("You cannot have more than three I, X, or Cs in a row")
            return True

    # def VLD_double_rules(self):
    #     """Tag if user input has more than 2 V, L , or D in a row."""
    #     if "VV" in self.number or "LL" in self.number or "DD" in self.number:
    #         print("You cannot have more than two V, L, or Ds in a row")
    #         return True


    # {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} 
    def precedence_rules(self):
        for i in range(len(self.number) - 1):
            if self.number[i] == 'I' and (self.number[i+1] == 'L' or self.number[i+1] == 'C' or \
                self.number[i+1] == 'D' or self.number[i+1] == 'M'):
                print("'I' cannot precede 'L', 'C', 'D', and 'M'.")
                return True
            elif self.number[i] == 'X' and (self.number[i+1] == 'D' or self.number[i+1] == 'M'):
                print("'X' can only precede itself, 'I', 'V', 'L', and 'C'.")
                return True
            elif self.number[i] == 'C' and (self.number[i+1] == 'C' or self.number[i+1] != 'D' or self.number[i+1] != 'M'):
                print("'C' can only precede itself, 'D', and 'M'.")
                return True
            elif self.number[i] == 'V' and self.number[i+1] != 'I':
                print("'V' can only precede 'I'.")
                return True
            elif self.number[i] == 'L' and (self.number[i+1] != 'I' or self.number[i+1] != 'V' or \
                self.number[i+1] != 'X'):
                print("'L' can only precede 'I', 'V', or 'X'.")
                return True
            elif self.number[i] == 'D' and (self.number[i+1] == 'D' or self.number[i+1] == 'M'):
                print("'V' can only precede 'I', 'V', 'X', 'L', or 'C'.")
                return True
        return False

if __name__ == '__main__':
    while True:
        user_input = input("Enter a number in roman numerals: ")
        if user_input == "":
            exit()
        x = RomanNumeral(user_input)
        x.roman_or_int()

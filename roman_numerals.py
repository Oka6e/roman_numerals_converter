class RomanNumeral: 
    """A class to represent our roman numerals or integers."""
    def __init__(self, number): 
        """Initializes the user's input, a counter, and standard values for each roman numeral."""
        self.number = number
        self.int_num = 0 # counter
        self.rom_num = ''
        self.rom_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} 

    def rom_to_int(self): # next() function? BUG: LXD and DXL give wrong answers.
        """Takes in user_input in roman numerals and return the equivalent integer."""
        rom_lst = list(self.rom_dict.items()) # DXL
        for i in range(len(self.number)-1):
            for j in range(len(rom_lst)): 
                if self.number[i] == rom_lst[j][0]: 
                    self.int_num += rom_lst[j][1]
                    print(self.int_num)
                    # if i == len(self.number) - 1:
                    #     self.int_num += rom_lst[j][1]
                    for k in range(j+1, len(rom_lst)):
                        if self.number[i+1] == rom_lst[k][0]:
                            if self.number[i]=='I' or self.number[i]=='X' or \
                                self.number[i]=='C' or self.number[i]=='M':
                                self.int_num -= 2*rom_lst[j][1]
                            else:
                                return "V, L, and D cannot be before Roman Numerals of greater value."
                                
        for l in range(len(rom_lst)):
            if self.number[-1] == rom_lst[l][0]:
                self.int_num += rom_lst[l][1]  
        return self.int_num 

    def int_to_rom(self):
        """Takes the user input of integer and converts it to Roman Numerals."""
        rom_lst = list(self.rom_dict.items()) # creates a list of the values of roman numerals
        rev_rom_lst = rom_lst[::-1] # reverse the list order from greatest to least
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
        return True

    def roman_or_int(self):
        """Checks if user input is a roman numeral, integer, or not."""
        if self.IXC_triple_rules():
            return
        elif self.VLD_double_rules():
            return
        elif self.isroman():
            print(self.rom_to_int())
        elif self.number.isdigit():
            print(self.int_to_rom())
        else:
            print("Entry is neither roman numerals or integers.")
    
    def IXC_triple_rules(self):
        """Tag if user input has more than 3 I, X, or C in a row."""
        if "IIII" in self.number or "XXXX" in self.number or "CCCC" in self.number:
            print("You cannot have more than three I, X, or Cs in a row")
            return True

    def VLD_double_rules(self):
        """Tag if user input has more than 2 V, L , or D in a row."""
        if "VV" in self.number or "LL" in self.number or "DD" in self.number:
            print("You cannot have more than two V, L, or Ds in a row")
            return True

if __name__ == '__main__':
    while True:
        user_input = input("Enter a number in roman numerals: ")
        if user_input == "":
            exit()
        x = RomanNumeral(user_input)
        x.roman_or_int()

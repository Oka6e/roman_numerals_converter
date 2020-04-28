class RomanNumeral:
    def __init__(self, number):
        self.number = number
        self.int_num = 0
    
    def roman_to_int(self):
        for i in self.number:
            if i is "I":
                self.int_num += 1
            elif i is "V":
                self.int_num += 5
            elif i is "X":
                self.int_num += 10
            elif i is "L":
                self.int_num += 50
            elif i is "C":
                self.int_num += 100
            elif i is "D":
                self.int_num += 500
            elif i is "M":
                self.int_num += 1000
            else:
                print("Please enter I, V, X, L, C, D, and/or M only.")
        return self.int_num

user_input = input("Enter a number in roman numerals: ")
x = RomanNumeral(user_input)
print(x.roman_to_int())

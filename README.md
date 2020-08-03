# Roman Numeral Converter

A program to convert your input of a roman numeral to integer and vice-versa.

<p align="center"> 
    <img src="https://github.com/Oka6e/roman_numerals_converter/blob/master/images/roman_numeral_pic.jpg?raw=true" alt="Roman Numerals Project Banner">
</p>

## Table of Contents
1. [Getting Started](README.md#getting-started)
    * [Prerequisites](README.md#prerequisites)
    * [Installation](README.md#installation)
    * [How to run the game](README.md#how-to-run-the-game)
2. [Game Rules](README.md#game-rules)
3. [File Descriptions](README.md#file-descriptions)
4. [Bugs](README.md#bugs)
5. [Credits](README.md#credits)

## Getting Started
Please follow these instructions to download the converter on your local machine. 

### Prerequisites
You will need to install the following:

```
Python 3.7.3
```

### Installation

**Roman Numerals Converter**

Enter the following into a Linux terminal and `cd` into the repository.

```
git clone https://github.com/frank-quoc/roman_numerals_converter.git
```

**Python 3**

Install Python 3.7.3
```
cd scripts
./install_python3.7.sh
```

### How to run the converter

Move back to the root directory of the repository and execute

```
python3.7 roman_numerals_converter.git
```

## Roman Numeral Rules

> The digit or digits of lower value is/are placed after or before the digit of higher value. 
The value of digits of lower value is added to or subtracted from the value of digit of higher value. 
Using the certain rules for formation of Roman-numerals is given below. \
**Rule 1:** The roman digits I, X and C are repeated upto three times in succession to form the numbers. \
**Rule 2:** When a digit of lower value is written to the right or after a digit of higher value, the 
values of all the digits are added. Value of similar digits are also added as indicated in rule 1 \
**Rule 3:** When a digit of lower value is written to the left or before a digit of higher value, then the 
value of the lower digit is subtracted from the value of the digit of higher value. \
**Rule 4:** If we have to write the numbers beyond 10 we should write the number 10 or groups of number 10 
and then number 1 or 5 as the case may be. Then these numbers are used to change to the corresponding Roman numerals. Numbers higher than number 40 are also formed. \
**Rule 5:** If a horizontal line is drawn over the symbols or digits of Roman numerals, then the value of the numerals becomes 1000 times.

## File Descriptions
---
File|Task
---|---
__pycache__ | Folder of bytcode .pyc files
images | Roman Numerals Banner
roman_numerals.py | Runs the Converter
test_roman_numerals.py | Test file for converter (unfinished)

## Bugs

test_roman_numerals.py file is currently unfinished.

## Credits

Made by Frank Ho | [@frank_quoc](https://twitter.com/frank_quoc)

Credit [Paul M. Winkler](https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s24.html)

[Roman Numeral Rules](https://www.math-only-math.com/rules-for-formation-of-roman-numerals.html)


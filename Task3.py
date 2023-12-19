"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# This variable will hold codes/prefixes with the count
set_of_codes_prefixes = {}


def updateCountInSet(key):
    if key in set_of_codes_prefixes:
        set_of_codes_prefixes[key] += 1
    else:
        set_of_codes_prefixes[key] = 1


def parseCodePrefix(number):
    if number.startswith("(080)"):
        updateCountInSet("080")
    elif "(" not in number and ")" not in number and number[5] == ' ':
        prefix = number[0:4]
        updateCountInSet(prefix)
    elif number.startswith("(0"):
        indexOfClosingBracket = number.find(')')
        prefix = number[1:indexOfClosingBracket]
        updateCountInSet(prefix)
    elif number.startswith("140"):
        updateCountInSet("140")


total = 0
for record in calls:
    if record[0].startswith("(080)"):
        total += 1
        parseCodePrefix(record[1])


# Solution A: Print the set generated
print("The numbers called by people in Bangalore have codes:")
for code in sorted(set_of_codes_prefixes.keys()):
    print(code)


# Solution B
percentage = (set_of_codes_prefixes["080"] / total) * 100
print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))

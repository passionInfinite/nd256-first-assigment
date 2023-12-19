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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

"""
Note: Something that we can improve upon in this solution is taking format of numbers in consider.
For example: (XXX) XXX XXXX can be there in addition to XXXXXXXXXX or XXX XXX XXXX
Adding cleanup and extract only digits and then check/append in unique numbers will resolve that issue.
Something which can be improved apart from the requirements in this task.
"""


unique_numbers = set()

# Check in texts records
for record in texts:
    unique_numbers.add(record[0])
    unique_numbers.add(record[1])

# Check in call records.
for record in calls:
    unique_numbers.add(record[0])
    unique_numbers.add(record[1])

print("There are "+str(len(unique_numbers)) +
      " different telephone numbers in the records.")

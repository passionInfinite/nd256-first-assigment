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



total_diff_numbers = 0
unique_texts_numbers = []
unique_calls_numbers = []

# Check in texts records
for record in texts:
    if record[0] not in unique_texts_numbers:
        unique_texts_numbers.append(record[0])
        total_diff_numbers += 1
    if record[1] not in unique_texts_numbers:
        unique_texts_numbers.append(record[1])
        total_diff_numbers += 1

# Check in call records.
for record in calls:
    if record[0] not in unique_calls_numbers:
        unique_calls_numbers.append(record[0])
        total_diff_numbers += 1
    if record[1] not in unique_calls_numbers:
        unique_calls_numbers.append(record[1])
        total_diff_numbers += 1

print("There are "+str(total_diff_numbers)+" different telephone numbers in the records.")
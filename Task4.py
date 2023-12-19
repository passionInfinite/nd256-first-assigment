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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

telemarketers = set()

for record in calls:
    if record[0].startswith("140"):
        telemarketers.add(record[0])

# Also check in texts to filter out the telemarketers numbers based on criteria
# numbers that make outgoing calls but never send texts, receive texts or receive incoming calls.
for record in texts:
    if record[0] in telemarketers:
        telemarketers.discard(record[0])
    if record[1] in telemarketers:
        telemarketers.discard(record[1])

print("These numbers could be telemarketers: ")
for number in sorted(telemarketers):
    print(number+'\n')

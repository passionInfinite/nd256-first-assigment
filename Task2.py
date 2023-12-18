"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

log_book = {}

for record in calls:
    if record[0] not in log_book:
        log_book[record[0]] = int(record[3])
    else:
        log_book[record[0]] += int(record[3])
    
    # Do same at the receiver side as well so we build log book for both numbers at once.
    if record[1] not in log_book:
        log_book[record[1]] = int(record[3])
    else:
        log_book[record[1]] += int(record[3])

# Sort the logbook to get the highest call duration number

highest_duration_number = None
highest_duration = 0
for number in log_book:
    duration = log_book[number]
    if highest_duration_number == None:
        highest_duration_number = number
        highest_duration = duration
    else:
        if highest_duration < duration:
            highest_duration_number = number
            highest_duration = duration 

print(highest_duration_number+" spent the longest time, "+str(highest_duration)+" seconds, on the phone during September 2016.")
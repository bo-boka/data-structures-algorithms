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

unique_callers = set()
unique_others = set()
for c in calls:
    unique_callers.add(c[0])
    unique_others.add(c[1])
for t in texts:
    unique_others.update([t[0], t[1]])

print("These numbers could be telemarketers: \n{}".format('\n'.join(sorted(unique_callers - unique_others))))


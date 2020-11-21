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

num_call_times = {}
for c in calls:
    if c[0] in num_call_times.keys():
        num_call_times[c[0]] += int(c[3])
    else:
        num_call_times[c[0]] = int(c[3])
    if c[1] in num_call_times.keys():
        num_call_times[c[1]] += int(c[3])
    else:
        num_call_times[c[1]] = int(c[3])
max_num = max(num_call_times, key=lambda k:num_call_times[k])

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_num,num_call_times[max_num]))

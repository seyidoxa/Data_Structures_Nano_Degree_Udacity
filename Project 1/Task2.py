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
def soln():
    counter = {}
    for record in calls:
        for i in range(2):
            counter[record[i]] = int(counter.get(record[i],0)) + int(record[3])
    max_key_val = max(counter.items(), key= lambda x : x[1])

    print("{} spent the longest time, {} seconds, on the phone during September \
        2016.".format(max_key_val[0],max_key_val[1]))

soln()
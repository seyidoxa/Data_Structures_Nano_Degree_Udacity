"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from subprocess import call

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
callers = []
call_receivers = []
messagers = []
msg_receivers = []

def soln():
    for record in calls:
        callers.append(record[0])
        call_receivers.append(record[1])


    for record in texts:
        messagers.append(record[0])
        msg_receivers.append(record[1])
        
    tele_markerter = []
    for tele in callers:
        if tele in call_receivers:
            continue
        if tele in messagers:
            continue
        if tele in msg_receivers:
            continue
        tele_markerter.append(tele)

    telem = set(tele_markerter)
    tele_m = list(telem)

    print("These numbers could be telemarketers: \n")
    for val in sorted(tele_m):
        print(val+'\n')

soln()
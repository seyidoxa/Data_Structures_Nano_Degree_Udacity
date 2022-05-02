"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
import pandas as pd

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def count_num(records, found =[]):
    for record in records:
        for i in range(2):
            if " " in record[i]:
                record[i] = record[i].replace(" ","")
            if '(' in record[i]:
                record[i] = record[i].replace('(',"")
            if ')' in record[i]:
                record[i] = record[i].replace(')',"")
            if record[i] not in found:
                found.append(record[i])
    return set(found)

def soln():
    a = count_num(texts)    # unique numbers in texts records
    b = count_num(calls)    # unique numbers in call records
    c = a & b               # numbers common to both records
    num = len(a)+ len(b) - len(c)

    print("There are {} different telephone numbers in the records.".format(num))

soln()


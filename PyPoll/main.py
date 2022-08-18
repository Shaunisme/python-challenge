# PyPoll
import os
import csv

totalVotes=0
canditate[]
number[]

scriptpath=os.path.dirname(os.path.realpath('__file__'))
csvpath=os.path.join(scriptpath,"Resources","election_data.csv")
with open(csvpath,encoding='utf') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    # Skip the first title line
    next(csvreader)

    # Read each row
    for row in csvreader:
        totalVotes=totalVotes+1

print('Election Resluts')
print('----------------------------------')
print(f'Total Votes: {totalVotes}')
print('----------------------------------')
print('----------------------------------')
print('----------------------------------')
# PyPoll
import os
import csv
from collections import Counter

def printline():
        print('----------------------------------')

canditate=[]

scriptpath=os.path.dirname(os.path.realpath('__file__'))
csvpath=os.path.join(scriptpath,"Resources","election_data.csv")
with open(csvpath,encoding='utf') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    # Skip the first title line
    next(csvreader)

    # Read each row
    for row in csvreader:
        canditate.append(row[2])
    
    voteCount=Counter(canditate)
    
    print('Election Resluts')
    printline()

    totalVotes=sum(voteCount.values())
    print(f'Total Votes: {totalVotes}')
    printline()

    for name in voteCount.keys():
        voteNumber=voteCount[name]
        print(f'{name}: {round(voteNumber/totalVotes*100,3)}% ({voteNumber})')
    printline()
    maxVotes=max(voteCount.values())
    winner=[i for i in voteCount.keys() if voteCount[i] == maxVotes]
    print(f'Winner: {winner[0]}')
    printline()

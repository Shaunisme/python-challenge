# PyPoll
import os
import csv
from collections import Counter

def printline():
        print('----------------------------------')

# init list
canditate=[]

# open data file to read
scriptPath=os.path.dirname(os.path.realpath('__file__'))
csvPath=os.path.join(scriptPath,"Resources","election_data.csv")
with open(csvPath,encoding='utf') as csvFile:
    csvReader=csv.reader(csvFile,delimiter=",")
    # Skip the first title line
    next(csvReader)

    # Read each row
    for row in csvReader:
        canditate.append(row[2])
    
    # Call Counter() to sum votes, get a dictionary voteCount
    voteCount=Counter(canditate)
    
    # Print Results
    print('Election Resluts')
    printline()

    # Calc total votes
    totalVotes=sum(voteCount.values())
    print(f'Total Votes: {totalVotes}')
    printline()

    # Print each one name, percent and vote count
    for name in voteCount.keys():
        voteNumber=voteCount[name]
        print(f'{name}: {round(voteNumber/totalVotes*100,3)}% ({voteNumber})')
    printline()

    # Choose the max votes and print winner
    maxVotes=max(voteCount.values())
    winner=[i for i in voteCount.keys() if voteCount[i] == maxVotes]
    print(f'Winner: {winner[0]}')
    printline()

# The end

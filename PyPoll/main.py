import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter ='')

    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

# The total number of votes cast

total_votes = int(len(column(0))) 

# A complete list of candidates who received votes
canidates =[row(1)]

names= (name for name in canidates)

# The percentage of votes each candidate won

canidate_percent = canidate_votes / total_votes

# The total number of votes each candidate won
canidate_votes = 


# The winner of the election based on popular vote

winner = max()


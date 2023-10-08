import os
import csv

my_report = open(os.path.join("analysis","election_report.txt"), "w")
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile)

    # print(csvreader)
    csv_header = next(csvreader)
    votes = 0
    cans = {}
    
    for row in csvreader:
        # votes = votes + 1
        votes += 1
        
        can = row[2]
        
        if can not in cans.keys():
                cans[can] = 0
        cans[can] += 1
                

output = f'''
Election Results
-------------------------
Total Votes: {votes:,}
-------------------------
'''

winner = ["",0]

for can in cans.keys():
        output += f"{can}: {cans[can]/votes * 100: .3f}% ({cans[can]:,})\n"

        if cans[can] > winner[1]:
                winner[0] = can 
                winner[1] = cans[can]

output += f"-------------------------\n Winner: {winner[0]}\n-------------------------"

print(output)
my_report.write(output)
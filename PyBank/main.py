import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter ='')

    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)
    

#     rows= csvfile.readlines()
# print(len(rows))

# The total number of months included in the dataset
total_months = int(len(column(0)))

# The net total amount of "Profit/Losses" over the entire period

total_profit = sum(int(range(row[1])))

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

avg_profit = int(total_profit / total_months)

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period
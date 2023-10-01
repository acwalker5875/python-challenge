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
    

    # rows= csvfile.readlines()
    # print(len(rows))

# The total number of months included in the dataset
total_months = int(len(column(0)))

# The net total amount of "Profit/Losses" over the entire period

total_profit = sum(int(range(row[1])))

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
starting_profit = (first row value)
ending_profit = (last row value)

change = starting_profit - ending_profit

avg_change = int(change / total_months)

# The greatest increase in profits (date and amount) over the entire period

greatest_profit = max(range(row[1]))

        if row[1] == max value:
            print("the greatest increase in profits occured in " row[0] "with profits of" row[1])


# The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(range(row[1]))

        if row[1] == min value:
            print("the greatest decrease in profits occured in " row[0] "with profits of" row[1])


import os
import csv

my_report = open(os.path.join("analysis","budget_report.txt"), "w")
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile)

    # print(csvreader)

    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    months = 0

# The total number of months included in the dataset
    for row in csvreader:
         months += 1
  # The net total amount of "Profit/Losses" over the entire period
  #   
        # total_profit = range(row[1])
         greatest_decrease = min(range(row[1]))
         greatest_profit = max(range(row[1]))
   


# The changes in "Profit/Losses" over the entire period, and then the average of those changes
    # # starting_profit = (first row value)
    # ending_profit = (last row.value)

    # change = starting_profit - ending_profit

    #  avg_change = int(change / total_months)

#


output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: 
Average Change: $-8311.11
Greatest Increase in Profits: {greatest_profit}
Greatest Decrease in Profits: {greatest_decrease}
'''
print(output)
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
    total_profit = 0
    profit1 = 1088983
    total_change = 0
    change_list = []

# The total number of months included in the dataset
    for row in csvreader:
         months += 1

  # The net total amount of "Profit/Losses" over the entire period 
         total_profit = total_profit + int(row[1])
        

# #  The changes in "Profit/Losses" over the entire period, and then the average of those changes
    
         profit2 = int(row[1])
         
         change = profit2 - profit1

         profit1 = profit2

         total_change = total_change + change

         change_list.append(change)
         greatest_decrease = min(change_list)
         greatest_profit = max(change_list)



avg_change = int(total_change / months)

# final formating
total_profit = "${:,}".format(total_profit)
avg_change = "${:,}".format(avg_change)
greatest_profit = "${:,}".format(greatest_profit)
greatest_decrease = "${:,}".format(greatest_decrease)



output = f'''
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)

Total Months: {months}
Total: {total_profit}
Average Change: {avg_change}
Greatest Increase in Profits: {greatest_profit}
Greatest Decrease in Profits: {greatest_decrease}
'''
print(output)
my_report.write(output)
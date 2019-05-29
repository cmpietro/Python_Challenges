# import needed modules for HOMEWORK3 PYBANK

import os
import csv

#define Variables for counting month, total revenue, revenue changes goals 1-5
filename = input("budget_data.csv")
month_count = 0
total_revenue = 0
this_month_revenue = 0
last_month_revenue = 0
revenue_change = 0
revenue_changes = []
months = []

# open csv file, read only with os.path.join for TA
budge_data = os.path.join("budget_data.csv")
with open("budget_data.csv",'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    # gather monthly changes in revenue, goals 1 - 5
    for row in csvreader:
        month_count = month_count + 1
        months.append(row[0])
        this_month_revenue = int(row[1])
        total_revenue = total_revenue + this_month_revenue
        if month_count > 1:
            revenue_change = this_month_revenue - last_month_revenue
            revenue_changes.append(revenue_change)
        last_month_revenue = this_month_revenue

# analyze the month by month changes, goals 1 - 5
sum_rev_changes = sum(revenue_changes)
average_change = sum_rev_changes / (month_count - 1)
max_change = max(revenue_changes)
min_change = min(revenue_changes)
max_month_index = revenue_changes.index(max_change)
min_month_index = revenue_changes.index(min_change)
max_month = months[max_month_index]
min_month = months[min_month_index]

# print summary to user goal 6
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Revenue Change: ${average_change}")
print(f"Greatest Increase in Revenue: {max_month} (${max_change})")
print(f"Greatest Decrease in Revenue: {min_month} (${min_change})")

# save summary as text file   Goal 6 - 
save_file = filename.strip(".csv") + "_results.txt"
filepath = os.path.join(".", save_file)
with open(filepath,'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------------------------" + "\n")
    text.write(f"Total Months: {month_count}" + "\n")
    text.write(f"Total Revenue: ${total_revenue}" + "\n")
    text.write(f"Average Revenue Change: ${average_change}" + "\n")
    text.write(f"Greatest Increase in Revenue: {max_month} (${max_change})" + "\n")
    text.write(f"Greatest Decrease in Revenue: {min_month} (${min_change})" + "\n")	
	

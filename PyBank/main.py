from operator import index
import os
import csv
from pdb import line_prefix

csvpath = os.path.join("Documents", "python-challenge", "PyBank", "Resources", "budget_data.csv")


profit_list = []
months = []
sum_months = 0
monthly_change = []
total = 0
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader, None)
    for row in csv_reader:
        profit_list.append(int(row[1]))
        months.append(row[0])
        sum_months = sum_months + 1
        total = total + int(row[1])

    for i in range(1, len(profit_list)):
        monthly_change.append(profit_list[i] - profit_list[i - 1])

    max_change = 0
    min_change = 0
    max_month = ""
    for months, change in zip(months[1:], monthly_change):
        if change > max_change:
            max_change = change
            max_month = months
        if change < min_change:
            min_change = change
            min_month = months

    print("Financial Analysis")
    print("---------------------------------")

    print("Total Months:", str(sum_months))
    print("Total: " + "$" + str(total))

    print("Greatest Increase in Profits:", str(max_month), '$' + str(max_change))
    print("Greatest Decrease in Profits:", str(min_month), "$" +  str(min_change))

    output = os.path.join("Documents", "python-challenge", "PyBank", "analysis", "budget_data.txt")
    with open(output, "w") as analysis:
        analysis.write("Financial Analysis" + "\n")
        analysis.write("---------------------------------" + "\n")
        analysis.write("Total Months: " + str(sum_months) + "\n")
        analysis.write("Total: " + "$" + str(total) + "\n")
        analysis.write("Greatest Increase in Profits: " + str(max_month) +  "$" + str(max_change) + "\n")
        analysis.write("Greatest Decrease in Profits: " + str(min_month) +  "$" + str(min_change))












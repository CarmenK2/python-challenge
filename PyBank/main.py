import os
import csv

from sympy import preview

DATE_INDEX = 0
PROFIT_LOSS_INDEX = 1

# Set path for file
budgetdata_csv = os.path.join(".", "Resources", "budget_data.csv")
print(budgetdata_csv)

#Set the value for calculation
number_of_months = 0
total_PNL = 0
Date_Greatest_profit = 0
Greatest_profit = 0
Date_Greatest_decrease = 0
Greatest_decrease = -0
Average_change = 0
Changes_in_profit=[]
Previous_profit = 0

# Open the CSV
with open(budgetdata_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)   # skip header row
    firstrow = next(csvreader)
    number_of_months = number_of_months + 1
    total_PNL = int(firstrow[1])
    Previous_profit = int(firstrow[1])

#Loop through all rows to find out answers  
    for row in csvreader:
        current_month = row[DATE_INDEX]
        current_PNL = int(row[PROFIT_LOSS_INDEX])
        
        #work out the months, total profit and loss and average changes
        number_of_months = number_of_months + 1
        total_PNL = total_PNL + current_PNL 
        change = int(row[1])-Previous_profit
        Changes_in_profit.append(change)
        Previous_profit = int(row[1])

        Average_change=round(sum(Changes_in_profit)/len(Changes_in_profit),2)
        Greatest_profit=max(Changes_in_profit)
        Greatest_decrease=min(Changes_in_profit)

        
print("Financial Analysis")
print(f"Total months: {number_of_months}")
print(f"Total Profit & Loss: ${total_PNL}")
print(f"Average Change: ${Average_change}")
print(f"Greatest Increase in Profit: ${Greatest_profit}")
print(f"Greatest Decrease in Profit: ${Greatest_decrease}")

  
     








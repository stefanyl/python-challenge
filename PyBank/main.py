#Import the os module
import os

#Module for reading in CSV file
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
#print(csvpath)


#Read in the csv and stores the header row
with open(csvpath) as budget_data:
    csvreader = csv.reader(budget_data, delimiter=',')
    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"Header Row: {csv_header}")

    for row in csvreader:
       #print(row)

print("Financial Analysis")
print("---------------------------")

#set variables for Financial Analysis
        total_months = []
        total_profit = []
        profit_change = []

        #Calculate the total number of months included in the dataset. Print.
        total_months.append(row[0])
        print(f"Total Months: {len(total_months)}")
        
        #calculate the net total amount of "Profit/Losses" over the entire period
        total_profit.append(int(row[1]))
        print(f"Total: ${sum(total_profit)}")
        
        #calculate the changes in "Profit/Losses" over the entire period. Iterate.Then, find average of those changes.
        for i = 2 to 87
            profit_change.append(total_profit[i+1]-total_profit[1])
#find the greatest increase in profits over the entires period
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)
#find the greatest decrease in profits over the entire period
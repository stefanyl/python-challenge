#Import the os module
import os

#Import module for reading in CSV file and set path.
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

#Set variables for Financial Analysis
total_months = []
total_profit = []
profit_change = []

#Read in the CSV and store the header row.
with open(csvpath, newline="", encoding='utf-8-sig') as budget_data:
    csvreader = csv.reader(budget_data, delimiter=',')

    header = next(csvreader)

    #For loop to iterate through the rows
    for row in csvreader:

        #Calculate the total number of months included in the dataset. 
        total_months.append(row[0])
        
        #Calculate the net total amount of "Profit/Losses" over the entire period
        total_profit.append(int(row[1]))
      
    #Calculate the changes in "Profit/Losses" over the entire period. 
    #Iterate through profits to find average of those changes. 
    for i in range(len(total_profit)-1):
        profit_change.append(total_profit[i+1]-total_profit[i])

#Find the greatest increase in profits over the entire period
max_increase = max(profit_change)
max_increase_period = profit_change.index(max(profit_change)) + 1


#Find the greatest decrease in profits over the entire period
max_decrease = min(profit_change)
max_decrease_period = profit_change.index(min(profit_change)) + 1 

#Print statement and export text file to analysis folder
print("Financial Analysis")  
print("--------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_period]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_period]} (${(str(max_decrease))})")



#Assemble your output string 
analysis_text = (
    f'Financial Analysis\n'
    f'--------------------------\n'
    f'Total Months: {len(total_months)}\n'
    f'Total: ${sum(total_profit)}\n'
    f'Average Change: ${round(sum(profit_change)/len(profit_change),2)}\n'
    f'Greatest Increase in Profits: {total_months[max_increase_period]} (${(str(max_increase))}\n'
    f'Greatest Decrease in Profits: {total_months[max_decrease_period]} (${(str(max_decrease))}'
    )


#Write your output string to a text file
with open('analysis_text.txt', "w") as txt_file:
    txt_file.write(analysis_text)

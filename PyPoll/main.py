#Import the os module
import os 

#Import the csv file and set path
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

#Declare variables with initial count 
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

khan_percentage = 0
correy_percentage = 0
li_percentage = 0
otooley_percentage = 0

#Open csv and skip the header.
with open(csvpath, newline="", encoding="utf-8") as election_data:
    csvreader = csv.reader(election_data, delimiter=',')

    header = next(csvreader)

    #Find the total number of votes cast. 
    for row in csvreader:
        total_votes += 1
    print(f"Total Votes: {total_votes}")

#List the candidates who received votes - Khan, Correy, Li, Otooley. 
#Find the total number of votes each candidate won.
        if row[2] == "Khan": 
            khan_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Li": 
            li_votes += 1
        elif row[2] == "O'Tooley":
            otooley_votes += 1 
        
#Find the percentage of votes each candidate won.
    khan_percentage = (khan_votes/total_votes) *100
    correy_percentage = (correy_votes/total_votes) * 100
    li_percentage = (li_votes/total_votes)* 100
    otooley_percentage = (otooley_votes/total_votes) * 100

#The winer of the election based on popular vote - need to fix 
#winner = max.total_votes

#Print your analysis 
votingresults = {
    "Khan":[khan_percentage, khan_votes],
    "Correy": [correy_percentage, correy_votes],
    "Li": [li_percentage, li_votes],
    "O'Tooley": [otooley_percentage, otooley_votes]
}
print(f"voting results": {votingresults})

#Export analysis as a text file
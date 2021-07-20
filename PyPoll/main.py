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


#Open csv and skip the header.
with open(csvpath, newline="", encoding="utf-8") as election_data:
    csvreader = csv.reader(election_data, delimiter=',')

    header = next(csvreader)

    #Find the total number of votes cast. 
    for row in csvreader:
        total_votes += 1

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

#The winner of the election based on popular vote - need to fix 
    election_winner = max(khan_votes, correy_votes, li_votes, otooley_votes)
    
    if election_winner == khan_votes:
        winner_name = "Khan"
    elif election_winner == correy_votes:
        winner_name = "Correy"
    elif election_winner == li_votes:
        winner_name = "Li"
    elif election_winner == otooley_votes:
        winner_name = "O'Tooley"

#Find the percentage of votes each candidate won.
khan_percentage = (khan_votes/total_votes) 
correy_percentage = (correy_votes/total_votes) 
li_percentage = (li_votes/total_votes)
otooley_percentage = (otooley_votes/total_votes) 

#Make a dictionary with results
#votingresults = {
    #"Khan": khan_percentage, (khan_votes),
    #"Correy": correy_percentage, (correy_votes),
    #"Li": li_percentage, (li_votes),
    #"O'Tooley": otooley_percentage, otooley_votes),
    #}
    
#Print your analysis 
print(f"Election Results")
print(f"-----------------------------")
print(f"Total Votes: {total_votes}")
print(f"-----------------------------")
print(f"Khan: {khan_percentage:.3%}, ({khan_votes})")
print(f"Correy: {correy_percentage:.3%}, ({correy_votes})")
print(f"Li: {li_percentage:.3%}, ({li_votes})")
print(f"O'Tooley: {otooley_percentage:.3%}, ({otooley_votes})")
print(f"-----------------------------")
print(f"Winner: {winner_name}")
print(f"-----------------------------")

#Export analysis as a text file
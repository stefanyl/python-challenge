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

#List the candidates who received votes.

#The percentage of votes each candidate won.

#The total number of votes each candidate won.

#The winer of the election based on popular vote


#Print your analysis 

#Export analysis as a text file
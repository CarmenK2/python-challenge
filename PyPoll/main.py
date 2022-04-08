import os
import csv

from sklearn.tree import ExtraTreeClassifier

# Set path for file
election_data_csv = os.path.join(".", "Resources", "election_data.csv")
print(election_data_csv)

#set the value for calucluation 
Number_of_Votes_casted = 0
Candidate_INDEX = 2
Candidate_list=[]
Candidate_votes={}
Khan_votesPercentage = 0
Correry_votesPercentage = 0
Li_votesPercentage = 0 
OTooley_votesPercentage = 0
Khan_votes = 0
Correry_vote = 0
Li_votes = 0 
OTooley_votes = 0 

 # Open the CSV
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)   # skip header row
    
#Looping through all rows to find out answers
    for row in csvreader:
        
        # (1) The total number of votes cast
        Number_of_Votes_casted = Number_of_Votes_casted + 1
        Candidate_name = row[Candidate_INDEX]

        # (2) A complete List of candidate who received votes & the total number of votes each candidate won
        if Candidate_name not in Candidate_list:
            Candidate_list.append(Candidate_name)
            Candidate_votes[Candidate_name] = 0 
    
        Candidate_votes[Candidate_name] += 1

                    
    #using max key method to find the max value from the dictionary
    max_key = max(Candidate_votes,key=Candidate_votes.get)


print("Election Results")
print("--------------------")
print(f"Total Votes: {Number_of_Votes_casted}")
print("--------------------")
print(Candidate_votes)
print("--------------------")
print(f"Winner: {max_key}")


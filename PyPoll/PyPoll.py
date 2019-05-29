

#import needed modules for HOMEWORK3 PyPoll

import sys
import os
import csv

#file name and variables

filename = input("election_data.csv")
total_votes = 0
candidate = ""
candidate_votes = {}
candidate_percentages ={}
winner_votes = 0
winner = ""

# open csv file USE os.path.join for TA 
filepath = os.path.join("election_data.csv")
with open(filepath,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    # tally votes Goals 1-4
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1

# calculate vote percentage and identify winner  goals 3 and 5 
for person, vote_count in candidate_votes.items():
    candidate_percentages[person] = '{0:.0%}'.format(vote_count / total_votes)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person

dashbreak = "-------------------------"

# print out results Goal 6
print("Election Results")
print(dashbreak)
print(f"Total Votes: {total_votes}")
print(dashbreak)
for person, vote_count in candidate_votes.items():
    print(f"{person}: {candidate_percentages[person]} ({vote_count})")
print(dashbreak)
print(f"Winner: {winner}")
print(dashbreak)

# save summary to text file Goal 6 
save_file = filename.strip(".csv") + "_results.txt"
filepath = os.path.join(".", save_file)
with open(filepath,'w') as text:
    text.write(dashbreak + "\n")
    text.write(f"Total Votes: {total_votes}" + "\n")
    text.write(dashbreak + "\n")
    for person, vote_count in candidate_votes.items():
        text.write(f"{person}: {candidate_percentages[person]} ({vote_count})" + "\n")
    text.write(dashbreak + "\n")
    text.write(f"Winner: {winner}" + "\n")
    text.write(dashbreak + "\n")
#import csv
import os
import csv
election_data = os.path.join('PyPoll', 'Resources', 'election_data.csv')
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

#variables
    vote_count = 0
    candidates = ["Khan", "Correy", "Li", "O'Tooley"]
    khan_votes = 0 
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    

    #loop
    for row in csvreader:

        #total votes
        vote_count = vote_count + 1

        # calculate candidate votes
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

        #perecntages
        khan_percent = (khan_votes/vote_count) *100
        correy_percent = (correy_votes/vote_count) * 100
        li_percent = (li_votes/vote_count)* 100
        otooley_percent = (otooley_votes/vote_count) * 100

    #calculate winner
    highest_vote = max(khan_votes, correy_votes, li_votes, otooley_votes)
    if highest_vote == khan_votes:
        highest_vote = "Khan"
    elif highest_vote == correy_votes:
        highest_vote = "Correy"
    elif highest_vote == li_votes:
        highest_vote = "Li"
    elif highest_vote == otooley_votes:
        highest_vote = "O'Tooley"
        

#print output
output = (
    f'Election Resuluts\n'
    f'-----------------\n'
    f'Total Votes: {vote_count}\n'
    f'-----------------\n'
    f'Khan: {khan_percent}% ({khan_votes})\n'
    f'Correy: {correy_percent}% ({correy_votes})\n'
    f'Li: {li_percent}% ({li_votes})\n'
    f"O'Tooley: {otooley_percent}% ({otooley_votes})\n"
    f'-----------------\n'
    f'Winner: {highest_vote}\n'
    f'-----------------\n'
)
print(output)

#export to analysis
analysis_txt = os.path.join('PyPoll', 'Analysis', 'vote_analysis.txt')
with open(analysis_txt, "w") as txt_file:
    txt_file.write(output)


   
#import csv
import os
import csv
election_data = os.path.join('PyPoll', 'Resources', 'election_data.csv')
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

#variables
    vote_count = 0
    win_vote = 0
    total_candidates = 0
    greatest_vote = ["", 0]
    candidate = []
    candidate_vote{}

    #loop
    for row in csvreader:

        #total votes
        vote_count = vote_count + 1
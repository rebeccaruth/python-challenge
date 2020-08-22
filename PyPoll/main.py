#import csv
import os
import csv
election_data = os.path.join('PyPoll', 'Resources', 'election_data.csv')
with open(election_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

#total votes
vote_count = -1
for row in election_data:
    vote_count += 1
print(vote_count)



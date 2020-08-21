#import csv
import os
import csv
budget_csv = os.path.join('PyBank','Resources', 'budget_data.csv')
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')


#total number of months
date = str(budget_csv[0])
month_count = -1
for row in open(budget_csv):
    month_count += 1
print('Total Months:', month_count)



#net total of profit/losses
#profit_loss = int(budget_csv[1])

#average change of profit/ losses


#greatest increase



#greatest decrease





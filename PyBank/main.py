#import csv
import os
import csv
budget_csv = os.path.join('PyBank','Resources', 'budget_data.csv')
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)

#print analysis
    print("Financial Analysis")
    print("------------------------------------")

#total number of months
    month_count = -1
    for row in open(budget_csv):
        month_count += 1
    print('Total Months:', month_count)

#net total of profit/losses
    total = 0
    #for row in budget_csv:
       #total = total + int(row[1])
    print('Total: ', total)



#average change of profit/ losses
    #average = total / (month_count - 1)

#greatest increase



#greatest decrease
#def min()


#OUTPUTS PRINTED
    
    
   
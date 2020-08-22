#import csv
import os
import csv
budget_csv = os.path.join('PyBank','Resources', 'budget_data.csv')
with open(budget_csv) as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    header = next(csvreader)

#variables
    month_total = 1
    pl_total = 0
    last_pl = 0
    pl_change = 0
    pl_change_list = []
    month_change = []
    greatest_inc = ["", 0]
    greatest_dec = ["", 99999999]


#loop
    for row in csvreader:

        #totals
        month_total = month_total + 1
        pl_total = pl_total + int(row["Profit/Losses"])   

        #revenue changes
        pl_change = int(row["Profit/Losses"]) - last_pl
        last_pl = int(row["Profit/Losses"])
        month_change = month_change + [row["Date"]]

        #greatest increase
        if (pl_change > greatest_inc[1]):
            greatest_inc[1] = pl_change
            greatest_inc[0] = [row["Date"]]

         #greatest decrease
        if (pl_change < greatest_dec[1]):
            greatest_dec[0] = [row["Date"]] 
            greatest_dec[1] = pl_change
               
        

#average        
pl_avg = pl_total / month_total

#print results
output = (
    f'Financial Analysis\n'
    f'------------------\n'
    f'Total Months: {month_total}\n'
    f'Total: ${pl_total}\n'
    f'Average Change: ${pl_avg}\n'
    f'Greatest Increase in Profits: {greatest_inc}\n'
    f'Greatest Decrease in Profits: {greatest_dec}\n'
)
print(output)

#export to analysis
analysis_txt = os.path.join('PyBank', 'Analysis', 'budget_analysis.txt')
with open(analysis_txt, "w") as txt_file:
    txt_file.write(output)


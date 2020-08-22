#import csv
import os
import csv
budget_csv = os.path.join('PyBank','Resources', 'budget_data.csv')
with open(budget_csv) as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    #header = next(csvreader)

#variables
    month_total = 0
    pl_total = 0
    last_pl = 0
    pl_change = 0
    pl_change_list = []
    month_change = []
    greatest_inc = ["", 0]
    greatest_dec = ["", 99999999]
    total_change = 0

#loop
    for row in csvreader:

        #totals
        month_total = month_total + 1
        #net_total = net_total + profit 
        pl_total = pl_total + int(row["Profit/Losses"])   

        #revenue changes
        if last_pl != 0:
            pl_change = int(row["Profit/Losses"]) - last_pl           
            total_change = total_change + pl_change
       
            #greatest increase
            if (pl_change > greatest_inc[1]):
                greatest_inc[1] = pl_change
                greatest_inc[0] = [row["Date"]]

            #greatest decrease
            if (pl_change < greatest_dec[1]):
                greatest_dec[0] = [row["Date"]] 
                greatest_dec[1] = pl_change
        last_pl = int(row["Profit/Losses"])   
        

#average 
pl_avg = total_change / (month_total - 1)

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


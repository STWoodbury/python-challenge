#import the csv and os modules
import csv
import os

#read in csv file
csv_file = os.path.join('Resources', 'budget_data.csv')

#create list from csv_file
with open(csv_file, 'r') as profit_loss:
    reader = csv.reader(profit_loss, delimiter = ",")

#store and skip header
    header = next(reader)

#initialize variables and lists
    total = 0
    month_count = 0
    iteration = 0
    months = []
    change = []

#loop through datalist
    for row in reader:

        #increase the total by the present P&L column value
        total += int(row[1])
        
        #increase the count of months by 1
        month_count += 1
        
        #check if reader is on the first row
        if iteration > 0:
            
            #if not on first row, append current month to months list
           months.append(row[0]) 

           #if not on first row, calculate the month over change from the previous month and append the result to the changes list
           change.append(int(row[1]) - int(previous_month))
        
        #increment the iteration counter 
        iteration += 1

        #set the value of this month's P&L to previous month variable for next iteration
        previous_month = row[1]

    #calculate the average change from the change list
    average_change =  round(sum(change) / len(change),2)
    
    #find the maximum and minimum change in the change list
    change_max = max(change)
    change_min = min(change)

    #match indexes of max and min changes to indexes of their respective months in months list
    max_month = months[change.index(change_max)]
    min_month = months[change.index(change_min)]

#print all values to terminal
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months:  {month_count}')
    print(f'Total: ${total}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {max_month} (${change_max})')
    print(f'Greatest Decrease in Profits: {min_month} (${change_min})')

    #create new text file in the analysis directory
    write_path = os.path.join('analysis', "analysis.txt")

    #open new file in write mode
    with open(write_path, 'w') as txt_file:

        #write results to txt file  
        txt_file.write('Financial Analysis \n')      
        txt_file.write('---------------------------- \n')
        txt_file.write(f'Total Months:  {month_count} \n')
        txt_file.write(f'Total: ${total}\n')
        txt_file.write(f'Average Change: ${average_change}\n')
        txt_file.write(f'Greatest Increase in Profits: {max_month} (${change_max})\n')
        txt_file.write(f'Greatest Decrease in Profits: {min_month} (${change_min})\n') 
     
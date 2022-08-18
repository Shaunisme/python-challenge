import os
import csv
# PyBank


# init months, totalAmount, flag, etc.
months=0
totalAmount=0
lastProfit=0
greatIncrease=0
greatDecrease=0
greatIncreaseMonth=""
greatDecreaseMonth=""
firstMonthFlag=True

# Read data from Resources file: ~/Resources/budget.data.csv
scriptpath=os.path.dirname(os.path.realpath('__file__'))
csvpath=os.path.join(scriptpath,"Resources","budget_data.csv")
with open(csvpath,encoding='utf') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    # Skip the first title line
    next(csvreader)

    # Read each row
    for row in csvreader:
        months=months+1
        profit=int(row[1])
        totalAmount=totalAmount + profit
        
        # Mark the profit of the first month, and turn the flag False
        if (firstMonthFlag):
            firstMonthProfit=profit
            firstMonthFlag=False
        
        increase=profit-lastProfit
        
        # Remember the profit for next month
        lastProfit=profit

        # Calc the greatest increase and the greatest decrease
        if (increase > greatIncrease):
            greatIncrease=increase
            greatIncreaseMonth=row[0]
        if (increase < greatDecrease):
            greatDecrease=increase
            greatDecreaseMonth=row[0]

# Print Result
print('Finacial Analysis')
print('\n------------------------\n')
print(f'Total Months: {months}\n')
print(f'Total: {totalAmount}\n')

print(f'Average Change: {round((profit-firstMonthProfit)/(months-1),2)}\n')

print(f'Greatest Increase in Profits: {greatIncreaseMonth} (${greatIncrease})\n')
print(f'Greatest Decrease in Profits: {greatDecreaseMonth} (${greatDecrease})')
import os
import csv
# PyBank

# Init months, totalAmount, flag, etc.
months=0
totalAmount=0
lastProfit=0
greatIncrease=0
greatDecrease=0
greatIncreaseMonth=""
greatDecreaseMonth=""
firstMonthFlag=True

# Read data from Resources file: ~/Resources/budget.data.csv
scriptPath=os.path.dirname(os.path.realpath('__file__'))
csvPath=os.path.join(scriptPath,"Resources","budget_data.csv")
with open(csvPath,encoding='utf') as csvFile:
    csvReader=csv.reader(csvFile,delimiter=",")
    # Skip the first title line
    next(csvReader)

    # Read each row and sum total profit
    for row in csvReader:
        months=months+1
        profit=int(row[1])
        totalAmount=totalAmount + profit
        
        # Mark the profit of the first month, and turn the flag False
        if (firstMonthFlag):
            firstMonthProfit=profit
            firstMonthFlag=False
        
        # Calc increase than last month
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
print('------------------------')
print(f'Total Months: {months}')
print(f'Total: {totalAmount}')

print(f'Average Change: {round((profit-firstMonthProfit)/(months-1),2)}')

print(f'Greatest Increase in Profits: {greatIncreaseMonth} (${greatIncrease})')
print(f'Greatest Decrease in Profits: {greatDecreaseMonth} (${greatDecrease})')
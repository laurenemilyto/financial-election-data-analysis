
# Import dependancies
import os
import csv

# Import pybank.csv file
pybank_csv = os.path.join("Resources", "budget_data1.csv")

# Initialize null lists
dates = []
profits = []
changes = []

# Read in the CSV file
with open (pybank_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row
    csv_header = next(csvreader)
    
    #Set last month to 0
    last_month = 0
    
    # Loop through columns, adding data from csv to lists after header
    for row in csvreader:
        
        # Define profit and date variables
        profit = int(row[1])
        date = str(row[0])
        
        # Add data to dates and profits lists
        dates.append(date)
        profits.append(profit)
        
        # Change = current profit - last months profit
        change = profit - last_month 
        
        # Reset last month
        last_month = profit  
        
        # Add data to changes list
        changes.append(change)

# Use len to find the total number of months 
total_months = len(dates)

# Use sume to find the total amount of "Profit/Losses" over the entire period
net_total = sum(profits)

# Use sum to add up monthly changes within the changes list
sum_changes = sum(changes)

# Find total average change of changes list over the entire period
avg = round(sum_changes/total_months,2) 

# Use max to find the greatest increase in profits (amount) over the entire period
greatest_increase_amount = max(profits)

# Use min to find the greatest decrease in losses (amount) over the entire period
greatest_decrease_amount = min(profits)

# Use index of greatest_increase_amount to find greatest increase date
increase_index = profits.index(greatest_increase_amount)
greatest_increase_date = dates[increase_index]

# Use index of greatest_decrease_amount to find greatest decrease date
decrease_index = profits.index(greatest_decrease_amount)
greatest_decrease_date = dates[decrease_index]

# Open & write txt to pybank_results.txt
with open ("pybank_results.txt", "w") as file:
        file.write("Financial Analysis" + "\n") 
        file.write("------------------------------------"+ "\n")
        file.write(f"Total Months: {total_months} \n")
        file.write(f"Total: ${net_total} \n")
        file.write(f"Average Change: ${avg} \n")
        file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount}) \n")
        file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount}) \n")

file = open("pybank_results.txt", "r")
print(file.read())

# close txt file





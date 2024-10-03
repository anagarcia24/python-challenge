
# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("/Users/ana/Desktop/python-challenge/PyBank/Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("/Users/ana/Desktop/python-challenge/PyBank/analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
avgChange = 0.00
maxIncr = 0
maxLoss = 0

amounts = []
date = []
changes = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    
  
    # Track the total and net change
    # Eliminate "," and save data into a list
    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1
        
        # Track the net change
        total_net += int(row[1])

        date.append(row[0])
        amounts.append(int(row[1]))
        

for i in range(len(amounts) -1):
    changes.append(amounts[i+1] - amounts[i])


# Calculate the average net change across the months
avgChange = sum(changes) / len(changes)

# Calculate the greatest increase and decrease in profits (month and amount)
maxIncr = max(changes)
maxLoss = min(changes)

# Generate the output summary

# Print the output
print("Financial Analysis\n------------------------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_net}')
print(f'Average Change: ${avgChange:.2f}')
print(f'Greatest Increase in Profits: {date[changes.index(maxIncr)+1]} (${maxIncr})')
print(f'Greatest Decrease in Profits: {date[changes.index(maxLoss)+1]} (${maxLoss})')

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n------------------------------------------------"
                   f'\nTotal Months: {total_months}'
                   f'\nTotal: ${total_net}'
                   f'\nAverage Change: ${avgChange:.2f}'
                   f'\nGreatest Increase in Profits: {date[changes.index(maxIncr)+1]} (${maxIncr})'
                   f'\nGreatest Decrease in Profits: {date[changes.index(maxLoss)+1]} (${maxLoss})')

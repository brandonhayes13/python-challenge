import os
import csv
# Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")
budget_txt = os.path.join("analysis", "budget_analysis.txt")
months_list = []
amount_list = []
change_list = []
counter = 1
max_change = 0
min_change = 10000000000
max_month = ""
min_month = ""

#Read in CSV file
with open(budget_csv) as csvfile:
    # Split the data on commas
    csv_reader = csv.reader(csvfile, delimiter=",")

    header = next(csv_reader)
    for row in csv_reader: 
        months_list.append(row[0])
        amount_list.append(int(row[1]))


        if counter > 1: 
            change= int(row[1]) - previous_amount
            change_list.append(change)

            if change > max_change: 
                max_change = change
                max_month = row[0]

            if change < min_change: 
                min_change = change
                min_month = row[0]


        counter += 1
        previous_amount = int(row[1])

average_change = round(sum(change_list)/len(change_list) , 2)
   
budget_output = (
f"Financial Analysis\n"
f"---------------------------\n"
f"Total Months: {len(months_list)}\n"
f"Total: ${sum(amount_list)}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profits: {max_month} (${max_change})\n"
f"Greatest Decrease in Profits: {min_month} (${min_change})"
)
print(budget_output)
with open(budget_txt,"w") as txtfile:
    txtfile.write(budget_output)

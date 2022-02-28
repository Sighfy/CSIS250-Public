"""
The Payroll Department keeps a list of employee information for each pay period in a text file.
The format of each line of the file is the following:
<last name> <hours worked> <hourly wage>

Write a program that inputs a filename from the user and prints to the terminal
a report of the wages paid to the employees for the given period.
- The report should be in tabular format with the appropriate header.
-Each line should contain:
    - An employee’s name
    - The hours worked
    - The wages paid for that period.

example:
Enter the file name: data.txt

Name            Hours      Total Pay
Lambert            34         357.00
Osborne            22         137.50
Giacometti          5         503.50
"""

# get the file input
fileName = input("Enter the file name: ")
f = open(fileName, 'r')

# format the header line
print("{:<15s}" "{:<10s}" "{:<10s}".format("Name", "Hours", "Total Pay"))

# loop through the file line by line
for line in f:
    name, hours, wage = line.split()  # separate info in each line
    hours = float(hours)
    wage = float(wage)
    total = wage * hours  # calculate the total wage
    formatHours = int(hours)  # format the hours to truncate the decimal point
    formatTotal = "{:.2f}".format(total)  # format the total to add 2 decimal places
    print("{:<15s}" "{:<10}" "{:<10}".format(name, formatHours, formatTotal))

f.close()

"""
Teachers in most school districts are paid on a schedule that
provides a salary based on their number of years of teaching experience.
For example, a beginning teacher in the Lexington School District might
be paid $30,000 the first year. For each year of experience after this
first year, up to 10 years, the teacher receives a 2% increase over the
preceding value.
Write a program that displays a salary schedule, in tabular format,
for teachers in a school district. The inputs are:
1. Starting salary
2. Annual percentage increase
3. Number of years for which to print the schedule
Each row in the schedule should contain the year number and the salary for that year
example:
Enter the starting salary: $30000
Enter the annual % increase: 2
Enter the number of years: 10

Year   Salary
-------------
 1    30000.00
 2    30600.00
 3    31212.00
 4    31836.24
 5    32472.96
 6    33122.42
 Module7    33784.87
 8    34460.57
 9    35149.78
10    35852.78
"""

# get the inputs
startSalary = float(input("Enter the starting salary: "))
percentIncrease = float(input("Enter the annual % increase: "))
numOfYears = int(input("Enter the number of years: "))

# start the prints
print("Year \t Salary")
print("----------------")

# create the for loop
for i in range(numOfYears):
    # the output display each increment
    print(i + 1, "\t\t", "%0.2f" % startSalary)
    # creating the percent to add to the starting number
    salaryPercent = startSalary * (percentIncrease / 100)
    # the next in the sequence
    startSalary = startSalary + salaryPercent
    # increment the sentinel i
    i += 1

"""
I created the while loop first.
Decided to use a for loop for readability and speed
# create the while loop for the math
# sentinel i for the counter
i = 1
# while loop to increase the output each time
while i < numOfYears + 1:
    # the output display each increment
    print(i, "\t\t", "%0.2f" % startSalary)
    # creating the percent to add to the starting number
    salaryPercent = startSalary * (percentIncrease / 100)
    # the next in the sequence
    startSalary = startSalary + salaryPercent
    # increment the sentinel i
    i += 1
"""

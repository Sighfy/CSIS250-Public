"""
The credit plan at TidBit Computer Store specifies a 10% down payment and an annual interest rate of 12%.
Monthly payments are 5% of the listed purchase price, minus the down payment.

Write a program that takes the purchase price as input. The program should display a table, with appropriate
headers, of a payment schedule for the lifetime of the loan. Each row of the table should contain the following items:

1. The month number (beginning with 1)
2. The current total balance owed
3. The interest owed for that month
4. The amount of principal owed for that month
5. The payment for that month
6. The balance remaining after payment

The amount of interest for a month is equal to balance × rate / 12.

The amount of principal for a month is equal to the monthly payment minus the interest owed.

Example:
Enter the purchase price: 200

Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance
 1         180.00           1.80             Module7.20             9.00           172.80
 2         172.80           1.73             Module7.27             9.00           165.53
 3         165.53           1.66             Module7.34             9.00           158.18
 4         158.18           1.58             Module7.42             9.00           150.77
 5         150.77           1.51             Module7.49             9.00           143.27
 6         143.27           1.43             Module7.57             9.00           135.71
 Module7         135.71           1.36             Module7.64             9.00           128.06
 8         128.06           1.28             Module7.72             9.00           120.34
 9         120.34           1.20             Module7.80             9.00           112.55
10         112.55           1.13             Module7.87             9.00           104.67
11         104.67           1.05             Module7.95             9.00            96.72
12          96.72           0.97             8.03             9.00            88.69
13          88.69           0.89             8.11             9.00            80.57
14          80.57           0.81             8.19             9.00            72.38
15          72.38           0.72             8.28             9.00            64.10
16          64.10           0.64             8.36             9.00            55.74
17          55.74           0.56             8.44             9.00            47.30
18          47.30           0.47             8.53             9.00            38.77
19          38.77           0.39             8.61             9.00            30.16
20          30.16           0.30             8.70             9.00            21.46
21          21.46           0.21             8.79             9.00            12.68
22          12.68           0.13             8.87             9.00             3.80
23           3.80           0.00             3.80             3.80             0.00
"""
price = float(input("Enter the purchase price: "))  # getting purchase price
# declaring needed variables
monthNumber = 1  # start the month number at 1
rate = 0.12  # create the rate variable
downPayment = price * .10  # down payment (10% of price)
monthlyPayment = (price - downPayment) * .05  # monthly payment = 5% of price - downPayment
currentBalance = price - downPayment  # starting balance owed
# displaying heading. here numbers specify the field width, < means left justification and
# s refers to string type values
print("{:<15s} {:<20s} {:<20s} {:<20s} {:<20s} {:<20s}"
      .format("Month", "Starting Balance", "Interest to Pay", "Principal to Pay", "Payment", "Ending Balance"))
# loop until balance = 0
while currentBalance > 0:
    # checking if current balance is less than monthly payment
    if currentBalance < monthlyPayment:
        amount = 0  # no interest
        principal = currentBalance  # remaining balance as principal
        payment = currentBalance  # remaining balance as payment
        endingBalance = 0  # end of loop
    else:
        # otherwise, finding each values
        amount = currentBalance * (rate / 12)  # interest amount
        principal = monthlyPayment - amount  # principal amount
        payment = amount + principal  # total payment
        endingBalance = currentBalance - principal  # ending balance
    # displaying everything. here d refers to decimal, f refers to floating point numbers
    # .2 refers to the floating point number"s precision
    print("{:<15d} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f}"
          .format(monthNumber, currentBalance, amount, principal, payment, endingBalance))
    currentBalance = endingBalance  # updating current balance and month number
    monthNumber += 1  # update the month number

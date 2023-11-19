'''1. Write a function to calculate compund interest. Help the user save money by displaying the interest they 
can earn by saving certain % of thier salary, for 3 different interest rates and for 3 different % of salary
eg
  Input Rs50000
  Output - If you save 10% of your salary, with 5% interest rate, you will get (display the amount)
           If you save 10% of your salary, with 6.5% interest rate, you will get (display the amount)

           If you save 15% of your salary, with 5% interest rate, you will get (display the amount)
           If you save 15% of your salary, with 6.5% interest rate, you will get (display the amount)

           If you save 15% of your salary, with 5% interest rate, you will get (display the amount)
           If you save 15% of your salary, with 6.5% interest rate, you will get (display the amount)'''
'''
Formula:-
A = P(1 + R/100) t 
Compound Interest = A – P '''
def compound_interest(principal_amount,interest_rate,time):
    amount=principal_amount*(1+(interest_rate/100))**time
    com_interest=amount-principal_amount
    return com_interest
   
n=int(input("Enter the total number of times to find compund interest:"))
for i in range(n):
    a=float(input(f"Enter the principal amount {i+1}: "))
    b=float(input(f"Enter the rate of interest {i+1}:"))
    c=int(input(f"Enter the time (in terms of years) {i+1}:"))
    d=compound_interest(a,b,c)
    print(f"If your principal amount is {a} with interest rate {b}, then you will get {d:.2f} in time of {c} year.")

OUTPUT:-
Enter the total number of times to find compund interest:3
Enter the principal amount 1: 50000
Enter the rate of interest 1:5.6
Enter the time (in terms of years) 1:1
If your principal amount is 50000.0 with interest rate 5.6, then you will get 2800.00 in time of 1 year.
Enter the principal amount 2: 50000
Enter the rate of interest 2:6
Enter the time (in terms of years) 2:1
If your principal amount is 50000.0 with interest rate 6.0, then you will get 3000.00 in time of 1 year.
Enter the principal amount 3: 60000
Enter the rate of interest 3:6
Enter the time (in terms of years) 3:1
If your principal amount is 60000.0 with interest rate 6.0, then you will get 3600.00 in time of 1 year.

#1.1 - Display the data from the above problem in a table format.
  
# pip install prettytable
from prettytable import PrettyTable
def compound_interest(principal_amount,interest_rate,time):
    amount=principal_amount*(1+(interest_rate/100))**time
    com_interest=amount-principal_amount
    return com_interest
   
n=int(input("Enter the total number of times to find compund interest:"))
output=[]
for i in range(n):
    a=float(input(f"Enter the principal amount {i+1}: "))
    b=float(input(f"Enter the rate of interest {i+1}:"))
    c=int(input(f"Enter the time (in terms of years) {i+1}:"))
    d=compound_interest(a,b,c)
    output.append([a,b,c,d]) #appending it as a list in tuple to store all values
t=PrettyTable(['Principal Amount','Interest Rate','Time(in years)','Final Amount']) #creating the row header
for row in output:
    t.add_row(row)
print(t)

OUTPUT:-
Enter the total number of times to find compund interest:3
Enter the principal amount 1: 50000
Enter the rate of interest 1:5.6
Enter the time (in terms of years) 1:1
Enter the principal amount 2: 50000
Enter the rate of interest 2:6
Enter the time (in terms of years) 2:1
Enter the principal amount 3: 60000
Enter the rate of interest 3:6
Enter the time (in terms of years) 3:1
+------------------+---------------+----------------+--------------+
| Principal Amount | Interest Rate | Time(in years) | Final Amount |
+------------------+---------------+----------------+--------------+
|     50000.0      |      5.6      |       1        |    2800.0    |
|     50000.0      |      6.0      |       1        |    3000.0    |
|     60000.0      |      6.0      |       1        |    3600.0    |
+------------------+---------------+----------------+--------------+

'''2. You have a message that you want to send to your friend. You don't want others to see the message. You code the message and send it.
The alg to code is - split each word in half and reverse it (eg cricket becomes ketccri), if the word ends with a vowel, split at the 
last letter and reverse (eg cinema becomes acinem), if the word has numbers, spell the number but add A as first and last letters
 (8 pm becomes AeightA pm ).
 Write an app that can code and decode the message.'''












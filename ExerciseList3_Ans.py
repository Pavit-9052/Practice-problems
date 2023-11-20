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

'''You have a message that you want to send to your friend. You don't want others to see the message. You code the message and send it.
The alg to code is - split each word in half and reverse it (eg cricket becomes ketccri), if the word ends with a vowel, split at the 
last letter and reverse (eg cinema becomes acinem), if the word has numbers, spell the number but add A as first and last letters
 (8 pm becomes AeightA pm ).'''
import inflect
def split_string_in_half(s):
    length = len(s)
    midpoint = length // 2

    first_half = s[:midpoint]
    second_half = s[midpoint:]

    return first_half, second_half

def encode(sen):
    words=sen.split()
    for word in words:
        if word.isalpha():
            first_half,second_half=split_string_in_half(word)
            if first_half[-1] in 'aieouAEIOU':
                out1=first_half[-1]+first_half[:-1]
            else:
                out1=first_half
            if second_half[-1] in 'aieou' or 'AEIOU':
                out2=second_half[-1]+second_half[:-1]
            else:
                out2=second_half
            print(out1+out2,end=" ")
        elif word.isdigit():
            p=inflect.engine()
            out3='A'+p.number_to_words(word)+'A'
            print(out3 , end=" ")

sentence=input("Enter the sentence:")
encode(sentence)

'''OUTPUT:-
Enter the sentence:Lets meet you by 7 pm in google meet
eLst emte yuo by AsevenA pm in ogoegl emte'''
                
            
''' 3.Sort the numbers in an array (ascending or descending). Write a function that finds the largest number in an array'''
def find_large(a):
    max=int(a[0])
    for i in a:
        if int(i)>max:
            max=int(i)
    return max
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
numbers=[45,63,52,78,37,99,40,91]
bubble_sort(numbers)
print("Ascending order of numbers:", numbers)
out=find_large(numbers)
print("The largest number in the given sequence is",out)

OUTPUT:-
Ascending order of numbers: [37, 40, 45, 52, 63, 78, 91, 99]
The largest number in the given sequence is 99

'''4.THere are two arrays of numbers. the numbers are sorted in ascending order. 
Find the numbers that are common in both arrays. 
Eg - array 1 = [1,3,7,9,13,14], array2 [1,2,7,13,15]. answer - [1,7,13]'''
a=[45,63,78,59,65,99,75,12]
b=[78,12,96,32,99,65]
a.sort()
b.sort()
print("The array 1 is:",a)
print("The array 2 is:",b)
output=[]
for i in a:
    for j in b:
        if i==j:
            output.append(i)
print("The common numbers:",*output)

OUTPUT:-
The array 1 is: [12, 45, 59, 63, 65, 75, 78, 99]
The array 2 is: [12, 32, 65, 78, 96, 99]
The common numbers: 12 65 78 99

















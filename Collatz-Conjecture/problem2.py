'''
Problem #1
Write a program for Collatz_conjecture.
Collatz_conjecture means -  start with the input number. 
For even number , divide by 2 (n/2)
For odd number - 3n + 1
apply the above for the result number until the answer is 1.

Problem #2
Same as above.
Input two numbers.
Print which number has less steps to reach 1.'''

#Problem 2
def Leastnum(n):
    count=0
    while n!=1:
        if n%2==0:
            n=n/2
            count+=1
        elif n%2!=0:
            n=(3*n)+1
            count+=1
    return count
n1=int(input("Enter the number1:"))
n2=int(input("Enter the number2:"))
a=Leastnum(n1)
b=Leastnum(n2)
if a<b:
    print("The number",n1,"has the less step to reach one.")
else:
     print("The number",n2,"has the less step to reach one.")

Output:-
Enter the number1:8
Enter the number2:2
The number 2 has the less step to reach one.

'''
Problem #1
Write a program for Collatz_conjecture.
Collatz_conjecture means -  start with the input number. 
For even number , divide by 2 (n/2)
For odd number - 3n + 1
apply the above for the result number until the answer is 1.'''

n=int(input("Enter the number:"))
while n!=1:
    if n%2==0:#checking for even number
        n=n/2
    elif n%2!=0:#checking for odd number
        n=(3*n)+1
    print(int(n),end=" ") #using int() to print as a whole number
       
Output:-
Enter the number:9
28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1


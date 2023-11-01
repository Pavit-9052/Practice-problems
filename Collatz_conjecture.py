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
Print which number has less steps to reach 1.

#Problem #3
Get a input. Create a sequence of numbers from that input using the above alg.
Find the largest number in the sequence. 

Eg, input is 8
8, 4,2, 1
input is 9
9,28,14,7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1


Program #1
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



Program #2
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

Program #3

n=int(input("Enter the number:"))
l1=[]
max=0
while n!=1:
    if n%2==0:
        n=n/2
    elif n%2!=0:
        n=(3*n)+1
    l1.append(int(n))
for i in l1:
    if i > max:
        max=i
print("The largest number in the sequence is",max)
        
        
Output:-
Enter the number:9
The largest number in the sequence is 52

       


'''


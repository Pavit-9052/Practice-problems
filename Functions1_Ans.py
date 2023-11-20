Problem 1:
Write a program to calculate your avg marks in CS subject in the last 3 exams.
def avg_cal(a,b,c):
    avg=(a+b+c)/3
    print("The average marks in last 3 exams is:",avg)
a=int(input("Enter the CS mark in exam 1:"))
b=int(input("Enter the CS mark in exam 2:"))
c=int(input("Enter the CS mark in exam 3:"))
avg_cal(a,b,c)

OUTPUT:-
Enter the CS mark in exam 1:65
Enter the CS mark in exam 2:87
Enter the CS mark in exam 3:96
The average marks in last 3 exams is: 82.66666666666667

Problem 2:
Write a program to calculate avg marks of your class, in CS subject in the last 3 exams.
def calculate_average_marks(subject_marks):
    total_marks = sum(subject_marks)
    num_exams = len(subject_marks)
    average_marks = total_marks / num_exams
    return average_marks

def total_avg(a, b, c):
    toa_avg = (a + b + c) / 3
    return toa_avg

cs_marks_exam1 = [75, 80, 85]
cs_marks_exam2 = [90, 85, 88]
cs_marks_exam3 = [78, 92, 87]

a = calculate_average_marks(cs_marks_exam1)
b = calculate_average_marks(cs_marks_exam2)
c = calculate_average_marks(cs_marks_exam3)
d = total_avg(a, b, c)

print("Average marks in Exam 1:", a)
print("Average marks in Exam 2:", b)
print("Average marks in Exam 3:", c)
print("Total Average marks:", d)

OUTPUT:-
Average marks in Exam 1: 80.0
Average marks in Exam 2: 87.66666666666667
Average marks in Exam 3: 85.66666666666667
Total Average marks: 84.44444444444446

Problem 3:
Write a program to calculate avg marks for each student and no of students whose avg is above 75%
 in CS subject in the last 3 exams.

Problem 4:
You are reponsible for making dinner for your family. Wrtie all the functions and its input/output.
Eg - buying ingredients, cutting veg, etc.
    
def buy_ingredients():
    return ["rice", "carrots", "peppers", "green beans", "onions", "soy sauce", "oil", "salt"]

def cook_rice():
    return "Cooked rice"

def chop_vegetables(carrots,onions):
    return "Chopped " + vegetables

def cook_vegetables(chopped_vegetables, oil, garlic):
    return f("cooked {chopped_vegetables} in {oil}")

def mix_all(cooked_rice, cook_vegetables salt, pepper):
    return f("Mixed {cooked_rice}, {cook_vegetables}, salt, and pepper")

def serve_dinner(fried_rice):
    print("Dinner is served: " + fried_rice)

def sauce(soy_sauce):
    return f("Added{soy_sauce}")

#call all functions

#Problem 5:
#Write a program to sort an array of numbers in ascending order. Use functions.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
numbers=[45,63,52,78,37,99,40,91]
bubble_sort(numbers)
print("Ascending order of numbers:", numbers)
OUTPUT:-
Ascending order of numbers: [37, 40, 45, 52, 63, 78, 91, 99]
Problem 6:
You are running a cafe. Write a program (only the functions with input and output) that you need to run the cafe.

Problem 7:

Its is a single player game where the user starts with 0 points. User keeps rolling the 
dice.If the rolled number is 0, game ends. If the rolled number is even, then 2 points are
 added. If the number is odd, then if the number is 1,3 then the user has to jump. 
 If the number is 5, then 3 points are added. The game ends when the user has 50 points.'''

'''Problem #2
you have a list of student names and another list with their marks in CS. 
hard code the values. no need to get it as input
Pass mark is 50.
Print a new list with all the students with pass marks along with their mark in the format name:mark.
Also print the number of students who failed.'''

names=["Pavithra","Abisha","Sanjana","Karthic Selvi","Abirami","DhanuSri","Sangetha","Madhu","Anu","Vidhya","Vishaka"]
marks=[80,53,12,45,32,96,78,23,56,26,3]
count=0
print("Passed students:-")
for i,j in zip(names,marks):  #zip to iterate over tow list at a time
    if j < 50:
        count+=1
    else:
        print("Name:",i," Mark :",j)
print("No of failed students :",count)

Output:-
Passed students:-
Name: Pavithra  Mark : 80
Name: Abisha  Mark : 53
Name: DhanuSri  Mark : 96
Name: Sangetha  Mark : 78
Name: Anu  Mark : 56
No of failed students : 6

'''Problem #3
you have a list of student names. you have one list each for their marks in CS, Math and English. 
hard code the values. no need to get it as input
Pass mark is 50.
Grade A is, mark 90 or above
Grade B , 80 or above
Fail is < 50
Print the name of the students who got A in all subjects or atleast one A and the rest B.
Try to use only one if statement.'''

names=["Pavithra","Abisha","Sanjana","Karthic Selvi","Abirami","DhanuSri"]
cs_marks=[78,99,56,88,60,40]
math_marks=[32,98,45,89,70,86]
eng_marks=[65,99,76,81,74,3]
for n,cs,mat,eng in zip(names,cs_marks,math_marks,eng_marks):
  if ((cs>=90 and mat>=90 and eng>=90)or cs>=80 or mat>=80 or eng>=80):
    print(n)


'''problem #4
write a program to find if two strings are same.
two string are considered same if both strings have same letters in same order, but from different starting point
eg abcd is same as bcda (a is moved to the right)
abcd is same as cdab 
abcd is  not same as cdba

123456 = 456123
123456 not = 412356
hint - 
there are many simple answers. you can try with slice function'''
def is_same(str1, str2):
    if (len(str1) != len(str2)):
        return False
    temp = str1 + str1
    return (str2 in temp)

str1 = "ABCD"
str2 = "CDAB"
if (is_same(str1, str2)):
    print("Strings are same")
else:
    print("Strings are not same")

'''problem #5
In your college Python is taught in 3 different departments by the same professor. 
For each dept, get the no of students stutying Python and their marks in the final exam 
Get the input as comma seperated string

Find the top 3 marks in each class
Find the top 3 marks if all classes are combined.
Find the avg mark of students with passing mark in each class and the classes combined.
Find which class has the best average mark and least number of failed students.'''

def is_correct(dep,value,total):
    if len(value)< total:
        print(f"You have left some marks in class{dep}.")
        print(f"The total marks is {total}. But you have entered {len(value)} marks.")
    elif len(value)> total:
        print(f"You have added some extra marks in class{dep}.")
        print(f"The total marks is {total}. But you have entered {len(value)} marks.")

def pass_or_fail(marks):
    passmark=50
    pass_std=[]
    fail_std=[]
    for mark in marks:
        if int(mark)>=passmark:
            pass_std.append(int(mark))
        else:
            fail_std.append(int(mark))
    return pass_std,fail_std

#getting the total no of students in each department
dep_1_tot=int(input("Enter the no of students in dep 1:"))
dep_2_tot=int(input("Enter the no of students in dep 2:"))
dep_3_tot=int(input("Enter the no of students in dep 3:"))

#getting their marks in exam for each department
print("Enter the marks separated by commas")
marks_dep_1=input("Enter the final exam mark of student of dep 1:").split(',')
cr1=is_correct(1,marks_dep_1,dep_1_tot)
marks_dep_2=input("Enter the final exam mark of student of dep 2:").split(',')
cr2=is_correct(2,marks_dep_2,dep_2_tot)
marks_dep_3=input("Enter the final exam mark of student of dep 3:").split(',')
cr3=is_correct(3,marks_dep_3,dep_3_tot)
marks_tot= marks_dep_1+marks_dep_2+marks_dep_3

#sorting them in ascending order
marks_dep_1.sort()
marks_dep_2.sort()
marks_dep_3.sort()
marks_tot.sort()

#finding the maximum 3 marks
top_of_dep1=marks_dep_1[-3:]
top_of_dep2=marks_dep_2[-3:]
top_of_dep3=marks_dep_3[-3:]
top_of_all_dep=marks_tot[-3:]

#function pass or fail calling
a=pass_or_fail(marks_dep_1)
b=pass_or_fail(marks_dep_2)
c=pass_or_fail(marks_dep_3)
d=pass_or_fail(marks_tot)

#finding the average
avg_1=sum(a[0])/len(a[0])
avg_2=sum(b[0])/len(b[0])
avg_3=sum(c[0])/len(c[0])
tot_avg=sum(d[0])/len(d[0])

#finding the least number of students
least_1=len(a[1])
least_2=len(b[1])
least_3=len(c[1])
tot_least=len(d[1])

print(f"The top 3 marks in class 1 ={top_of_dep1}")
print(f"The top 3 marks in class 2 ={top_of_dep2}")
print(f"The top 3 marks in class 3 ={top_of_dep3}")
print(f"The top 3 marks in total class of combination ={top_of_all_dep}")
print(f"Average mark in class 1 ={avg_1}")
print(f"Average mark in class 2 ={avg_2}")
print(f"Average mark in class 3 ={avg_3}")
print(f"Average mark in  total classes ={tot_avg}")
print(f"Least number of failed students in class 1 ={least_1}")
print(f"Least number of failed students in class 2 ={least_2}")
print(f"Least number of failed students in class 3 ={least_3}")
print(f"Least number of failed students in total class  ={tot_least}")

OUTPUT:-

Enter the no of students in dep 1:7
Enter the no of students in dep 2:5
Enter the no of students in dep 3:6
Enter the marks separated by commas
Enter the final exam mark of student of dep 1:45,65,87,96,35,99,63
Enter the final exam mark of student of dep 2:78,69,83,45,56,63
You have added some extra marks in class2.
The total marks is 5. But you have entered 6 marks.
Enter the final exam mark of student of dep 3:78,65,95,89,96,87
The top 3 marks in class 1 =['87', '96', '99']
The top 3 marks in class 2 =['69', '78', '83']
The top 3 marks in class 3 =['89', '95', '96']
The top 3 marks in total class of combination =['96', '96', '99']
Average mark in class 1 =82.0
Average mark in class 2 =69.8
Average mark in class 3 =85.0
Average mark in  total classes =79.3125
Least number of failed students in class 1 =2
Least number of failed students in class 2 =1
Least number of failed students in class 3 =0
Least number of failed students in total class  =3












    










    




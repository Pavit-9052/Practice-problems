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




    




'''Problem #2
Write a program that reads a passage or string and counts the occurrences of two consecutive words 
that are the same without any other specific word in between.
 For example, count the occurrences of "apple apple" but not "apple orange apple."'''


sentence='pavi abi pavi pavi abi abi abi pavi'
words = sentence.split()
count=0
for i in range(len(words) - 1): #To iterate from the 1st word to the word befor last
    if words[i] == words[i + 1]: #Comparing the current and next word
        count += 1
print(f"Count of Occurrences: {count}")


'''
OUTPUT:-
Count of Occurrences: 3
'''

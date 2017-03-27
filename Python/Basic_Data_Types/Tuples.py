'''
Task 
Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).
Input Format
The first line contains an integer, n, denoting the number of elements in the tuple. 
The second line contains n space-separated integers describing the elements in tuple t.
Output Format
Print the result of hash(t).

https://www.hackerrank.com/challenges/python-tuples
'''

n = input()
i = 0
tmpList = []

allNumbers = raw_input().split()

while i < len(allNumbers):
    tmpList.append(int(allNumbers[i]))
    i += 1
  
tpl = tuple(tmpList)

print hash(tpl)

'''
You are given one set A and a number of other sets, N. 
Your job is to find whether set A is a strict superset of all the N sets. 
Print True, if A is a strict superset of all of the N sets. Otherwise, print False.
A strict superset has at least one element that does not exist in its subset.
Input Format
The first line contains the space separated elements of set A.
The second line contains integer N, the number of other sets.
The next N lines contains the space separated elements of the other sets.
Output Format
Print True if set A is a strict superset of all other N sets. Otherwise, print False.
https://www.hackerrank.com/challenges/py-check-strict-superset
'''

A = set(map(int, raw_input().split()))
isStrictSet = True

for i in range(input()):
    tempSet = set(map(int, raw_input().split()))
    if not tempSet.issubset(A):
        isStrictSet = False
    if len(tempSet) >= len(A):
        isStrictSet = False
print(isStrictSet)

'''
Task
You are given a string s. 
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.
Input Format
A single line containing the string s and integer value k separated by a space.
Output Format
Print the combinations with their replacements of string s on separate lines.
https://www.hackerrank.com/challenges/itertools-combinations-with-replacement
'''

from itertools import combinations_with_replacement

s, k = raw_input().split()
for each in combinations_with_replacement(sorted(s), int(k)):
    print ''.join(each)

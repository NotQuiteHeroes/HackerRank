'''
Task
You are given a string S. 
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
Input Format
A single line containing the string S and integer value k separated by a space.
Output Format
Print the different combinations of string S on separate lines.
https://www.hackerrank.com/challenges/itertools-combinations
'''

from itertools import combinations

instructions = raw_input().split()
for i in range(1, int(instructions[1])+1):
    for j in combinations(sorted(instructions[0]), i):
        print ''.join(j)

'''
Task
You are given a string S. 
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
Input Format
A single line containing the space separated string S and the integer value k.
Output Format
Print the permutations of the string S on separate lines.
https://www.hackerrank.com/challenges/itertools-permutations
'''

from itertools import permutations

instructions = raw_input().split()
print('\n'.join("".join(i) for i in permutations(sorted(instructions[0]), int(instructions[1]))))

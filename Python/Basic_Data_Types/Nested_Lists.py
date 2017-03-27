'''
Given the names and grades for each student in a Physics class of n students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
Input Format
The first line contains an integer, n, the number of students. 
The  subsequent 2n lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.
Constraints
2 <= n <= 5
There will always be one or more students having the second lowest grade.
Output Format
Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

https://www.hackerrank.com/challenges/nested-list
'''

students = [[raw_input(), float(raw_input())] for _ in range(input())]

second_highest = sorted(set([b for a,b in students]))[1]
print '\n'.join(sorted([a for a,b in students if b == second_highest]))

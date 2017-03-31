'''
Task
You have a non-empty set s, and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.
Input Format
The first line contains integer n, the number of elements in the set s. 
The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9. 
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.
Output Format
Print the sum of the elements of set s on a single line.
https://www.hackerrank.com/challenges/py-set-discard-remove-pop
'''

input()
s = set(map(int, raw_input().split())) 
totalCmds = input()
for _ in range(totalCmds):
    cmd = (raw_input() + " ").split(" ")
    eval('s.'+cmd[0]+'('+cmd[1]+')') 
print sum(s)

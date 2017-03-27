'''
Consider a list (list = []). You can perform the following commands:
1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.
Input Format
The first line contains an integer, n, denoting the number of commands. 
Each line i of the n subsequent lines contains one of the commands described above.
Constraints
The elements added to the list must be integers.
Output Format
For each command of type print, print the list on a new line.

https://www.hackerrank.com/challenges/python-lists
'''

L = []
n = input()
i = 0

while i < n:
    commandList = raw_input().split()
    
    command = commandList[0]
    
    if command == 'insert':
        x = int(commandList[1])
        y = int(commandList[2])
        L.insert(x, y)
    elif command == 'remove':
        x = int(commandList[1])
        L.remove(x)
    elif command == 'append':
        x = int(commandList[1])
        L.append(x)
    elif command == 'print':
        print L
    elif command == 'pop':
        L.pop()
    elif command == 'sort':
        L.sort()
    elif command == 'reverse':
        L.reverse()
        
    i+=1

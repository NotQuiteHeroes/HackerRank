'''
Read an integer N.
Without using any string methods, try to print the following: 123...N
Note that "..." represents the values in between.
Input Format 
The first line contains an integer N.
Output Format 
Output the answer as explained in the task.

https://www.hackerrank.com/challenges/python-print
'''

from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    for x in range(1,n+1):
        print(x,end='')

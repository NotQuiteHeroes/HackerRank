'''
Task
You are given a two lists A and B. Your task is to compute their cartesian product AXB.
Note:  and  are sorted lists, and the cartesian product's tuples should be output in sorted order.
Input Format
The first line contains the space separated elements of list A. 
The second line contains the space separated elements of list B.
Both lists have no duplicate integer elements.
Output Format
Output the space separated tuples of the cartesian product.
https://www.hackerrank.com/challenges/itertools-product
'''

from itertools import product

A = map(int, raw_input().split())
B = map(int, raw_input().split())
AxB = list(product(A, B))
print(' '.join(map(str, AxB)))

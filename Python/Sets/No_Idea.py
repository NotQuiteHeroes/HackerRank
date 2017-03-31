'''
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i is an element of set A, you add  to your happiness. If i is an element of set B, you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.
Input Format
The first line contains integers n and m separated by a space. 
The second line contains n integers, the elements of the array. 
The third and fourth lines contain m integers, A and B, respectively.
Output Format
Output a single integer, your total happiness.
https://www.hackerrank.com/challenges/no-idea?h_r=next-challenge&h_v=zen
'''

happiness = 0

# n and m are uneccesary, use throw away raw_input for first line of input
raw_input()

arr = map(int, raw_input().split())

# set lookup is O(1) vs list O(n)
A = set(map(int, raw_input().split()))
B = set(map(int, raw_input().split()))

# list comprehension - noting true = 1 false = 0, simply subtract total instances of i in B from total instances of i in A
print(sum([(i in A)-(i in B) for i in arr]))

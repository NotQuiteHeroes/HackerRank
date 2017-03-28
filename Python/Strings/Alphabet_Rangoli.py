'''
You are given an integer, n. Your task is to print an alphabet rangoli of size n. (Rangoli is a form of Indian folk art based on creation of patterns.)
Example:
#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
https://www.hackerrank.com/challenges/alphabet-rangoli
'''

from string import ascii_lowercase as letters

if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)
    
def print_rangoli(size):
    for i in range(size - 1, 0, -1):
        row = ["-"] * (size * 2 - 1)
        for j in range(0, size - i):
            row[size - 1 - j] = letters[j + i]
            row[size - 1 + j] = letters[j + i]
        print("-".join(row))

    for i in range(0, size):
        row = ["-"] * (size * 2 - 1)
        for j in range(0, size - i):
            row[size - 1 - j] = letters[j + i]
            row[size - 1 + j] = letters[j + i]
        print("-".join(row))

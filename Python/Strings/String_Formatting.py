'''
Given an integer, n, print the following values for each integer i from 1 to n:
-Decimal
-Octal
-Hexadecimal (capitalized)
-Binary
The four values must be printed on a single line in the order specified above for each i from 1 to n. Each value should be space-padded to match the width of the binary value of n.
Input Format
A single integer denoting n.
Output Format
Print n lines where each line i (in the range 1 <= i <= n ) contains the respective decimal, octal, capitalized hexadecimal, and binary values of i. Each printed value must be formatted to the width of the binary value of n.
https://www.hackerrank.com/challenges/python-string-formatting
'''

if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)
    
def print_formatted(number):
    width = len("{0:b}".format(number))
    for i in range(1,number+1):
        print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width)

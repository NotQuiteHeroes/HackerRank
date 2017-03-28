'''
Task
You are given a string  and width . 
Your task is to wrap the string into a paragraph of width .
Input Format
The first line contains a string, s. 
The second line contains the width, w.
https://www.hackerrank.com/challenges/text-wrap
'''

import textwrap
if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result

def wrap(string, max_width):
    result = textwrap.wrap(string, max_width)
    result = textwrap.fill(string, max_width)
    return result

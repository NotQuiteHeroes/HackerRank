'''
You are given a string s. Your task is to capitalize each word of s.
Input Format
A single line of input containing the string, s.
Preserve whitespace
https://www.hackerrank.com/challenges/capitalize
'''

if __name__ == '__main__':
    string = raw_input()
    capitalized_string = capitalize(string)
    print capitalized_string

def capitalize(string):
    s = string.split(' ')
    return ' '.join(word.capitalize() for word in s)

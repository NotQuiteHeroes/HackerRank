'''
Task 
Read a given string, change the character at a given index and then print the modified string.
Input Format 
The first line contains a string, S. 
The next line contains an integer i, denoting the index location and a character c separated by a space.
https://www.hackerrank.com/challenges/python-mutations
'''

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new
    
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

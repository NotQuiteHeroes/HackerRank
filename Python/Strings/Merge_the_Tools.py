'''
Consider the following:
A string, s, of length n where s = c0c1...cn-1.
An integer, k, where k is a factor of n.
We can split s into n/k subsegments where each subsegment, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:
The characters in ui are a subsequence of the characters in ti.
Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index <j in ti, then do not include the character in string ui.
Given s and k, print n/k lines where each line i denotes string ui.
Input Format
The first line contains a single string denoting s. 
The second line contains an integer, k, denoting the length of each subsegment.
It is guaranteed that n is a multiple of k.
Output Format
Print n/k lines where each line i contains string ui.
Sample input: 
AABCAAADA
3
Sample output:
AB
CA
AD
https://www.hackerrank.com/challenges/merge-the-tools
'''

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    
def merge_the_tools(string, k):
    u = []
    kCounter = 0
    for letter in string:
        kCounter+=1
        if letter not in u:
            u.append(letter)
        if kCounter == k:
            print(''.join(u))
            kCounter = 0
            u = []

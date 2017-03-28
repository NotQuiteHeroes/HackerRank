'''
You are given a string S. Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
https://www.hackerrank.com/challenges/swap-case
'''

if __name__ == '__main__':
  s = raw_input()
  result = swap_case(s)
  print result
  
#using built-in swapcase function
def swap_case(s):
  return s.swapcase()
  
#without built-in swapcase function
def swap_case(s):
  result = ''.join([i.lower() if i.isupper() else i.upper() for i in s])

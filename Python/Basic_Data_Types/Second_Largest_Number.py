'''
You are given n numbers. Store them in a list and find the second largest number.
Input Format 
The first line contains n. The second line contains an array A[] of n integers each separated by a space.
Output Format 
Output the value of the second largest number.

https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
'''

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    print(sorted(set(arr))[-2])

'''
Task: Given an integer, n, perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
Input Format
A single line containing a positive integer, n.
Output Format
Print Weird if the number is weird; otherwise, print Not Weird.
'''

if __name__ == '__main__':
    n = int(raw_input())
    
    if(n % 2 != 0):
        print("Weird")
    elif(n == 2 or n == 4):
        print("Not Weird")
    elif(n % 2 == 0 and n in range(6, 21)):
        print ("Weird")
    elif(n%2 == 0 and n > 20):
        print("Not Weird")

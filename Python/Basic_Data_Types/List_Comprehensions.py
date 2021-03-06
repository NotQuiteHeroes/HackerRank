'''
Let's learn about list comprehensions! You are given three integers x, y, and z representing the dimensions of a cuboid along with an integer n. You have to print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n. Here, 0 <= i <= x, 0 <= j <= y, 0 <= k <= z.
Input Format
Four integers x, y, z and n each on four separate lines, respectively.
Constraints
Print the list in lexicographic increasing order.

https://www.hackerrank.com/challenges/list-comprehensions
'''

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

    results = []
    for i in range(0, x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                if(i+j+k != n):
                    results.append([i, j, k])
    print(results)

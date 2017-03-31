'''
Task
Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
Formula used:
Average = sum of distinct heights / total number of distinct heights
Input Format
The first line contains the integer, N, the total number of plants.
The second line contains the N space separated heights of the plants.
Output Format
Output the average height value on a single line.
https://www.hackerrank.com/challenges/py-introduction-to-sets
'''

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
    
def average(array):
    distinctHeights = set(array)
    return(sum([int(x) for x in distinctHeights])/(float(len(distinctHeights))))

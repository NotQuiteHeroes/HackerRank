'''
ABC is a right triangle, 90° at B.
Therefore, the angle of ABC = 90°.
Point M is the midpoint of hypotenuse AC.
You are given the lengths AB and BC. 
Your task is to find the angle of MBC in degrees.
Input Format
The first line contains the length of side AB.
The second line contains the length of side BC.
Output Format
Output angle MBC in degrees. 
Note: Round the angle to the nearest integer.
https://www.hackerrank.com/challenges/find-angle
'''

import math

AB = input()
BC = input()

hypotenuse = math.pow(((AB*AB)+(BC*BC)), 0.5)

# use acos to find angle: cosine of angle = A/H, acos(A/H) = angle
# acos gives angle in radians, use math.degrees to convert to degrees
angle = math.degrees(math.acos(BC/hypotenuse))
print(str(int(round(angle)))+ "°")


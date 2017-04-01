'''
Task 
You are given a complex z. Your task is to convert it to polar coordinates.
Input Format
A single line containing the complex number z.
Output Format
Output two lines: 
The first line should contain the value of r. 
The second line should contain the value of the phase angle.
https://www.hackerrank.com/challenges/polar-coordinates
'''

import cmath

toTranslate = raw_input()
r = abs(complex(toTranslate))
phaseAngle = cmath.phase(complex(toTranslate))
print("%f\n%f" % (r, phaseAngle))

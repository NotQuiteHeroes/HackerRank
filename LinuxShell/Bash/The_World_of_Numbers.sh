# Given two integers, x and y, find their sum, difference, product, and quotient.
# Input Format 
# Two lines containing one integer each (x and y, respectively).
# Output Format 
# Four lines containing the sum (), difference (), product (), and quotient (), respectively. 
# https://www.hackerrank.com/challenges/bash-tutorials---the-world-of-numbers

read x
read y
echo $(($x + $y))
echo $(($x - $y))
echo $(($x*$y))
echo $(($x/$y))

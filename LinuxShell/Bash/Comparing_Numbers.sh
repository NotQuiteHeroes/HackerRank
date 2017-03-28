# Given two integers, x and y, identify whether x > y or x < y or x=y .
# Comparisons in a shell script may either be accomplished using regular operators (such as < or >) 
# or using (-lt, -gt, -eq, i.e. less than, greater than, equal to) for POSIX shells.
# Input Format 
# Two lines containing one integer each ( x and y, respectively).
# Output Format 
# Exactly one of the following lines: 
# - X is less than Y 
# - X is greater than Y 
# - X is equal to Y
# https://www.hackerrank.com/challenges/bash-tutorials---comparing-numbers

read x
read y
if (($x > $y))
then
    echo 'X is greater than Y'
elif (($x < $y))
then
    echo 'X is less than Y'
else
    echo 'X is equal to Y'
fi

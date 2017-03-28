#Your task: 
#Given three integers (x, y, and z) representing the three sides of a triangle, 
# identify whether the triangle is Scalene, Isosceles, or Equilateral.
# Input Format 
# Three integers, each on a new line.
# Input Constraints 
# Sum of any two sides will be greater than the third.
# Output Format 
# One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).
# https://www.hackerrank.com/challenges/bash-tutorials---more-on-conditionals

read a
read b
read c
if [ ! $a = $b ] && [ ! $a = $c ] && [ ! $b = $c ]
then
    echo "SCALENE"
elif [ $a = $b ] && [ $b = $c ]
then
    echo "EQUILATERAL"
else
    echo "ISOSCELES"
fi

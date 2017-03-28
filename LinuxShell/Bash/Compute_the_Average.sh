# Given N integers, compute their average correct to three decimal places.
# Input Format 
# The first line contains an integer, N. 
# N lines follow, each containing a single integer.
# Output Format 
# Display the average of the N integers, rounded off to three decimal places.
# https://www.hackerrank.com/challenges/bash-tutorials---compute-the-average

read i
x=0
while [ $x -lt $i ];
do
    read num
    sum=$((sum + num))
    x=$((x + 1))
done
printf "%.3f" `echo "$sum/$i" | bc -l`

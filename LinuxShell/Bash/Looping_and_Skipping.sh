# for loops in Bash can be used in several ways: 
# - iterating between two integers, a and  b
# - iterating between two integers, a and b, and incrementing by  each time 
# - iterating through the elements of an array, etc.
# Your task is to use for loops to display only odd natural numbers from 1 to 99.
# https://www.hackerrank.com/challenges/bash-tutorials---looping-and-skipping

for i in {1..99..2}
    do
        echo $i
    done

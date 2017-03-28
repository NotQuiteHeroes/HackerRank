# There are several ways of making simple numerical calculations in Bash. 
# Just trying to echo an expression wrapped in quotation marks will not work. 
# Wrapping the expression in double parenthesis $((..)) evaluates it, but this is confined to integer computations. 
# To evaluate expressions involving decimal places (floating points) "bc -l" is very useful.
# Task
# We provide you with expressions containing +,-,*,^, / and parenthesis. 
# None of the numbers in the expression involved will exceed 999. 
# Your task is to evaluate the expression and display the output correct to  decimal places.
# https://www.hackerrank.com/challenges/bash-tutorials---arithmetic-operations

read expression
printf "%.3f" `echo "$expression" | bc -l`


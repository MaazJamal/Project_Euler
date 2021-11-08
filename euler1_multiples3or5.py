# Multiples of 3 or 5
# Submit

#  Show HTML problem content 
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

"""
the sum of multiple of a number is simply a series of addition of the same number. 
For example if we take multiple of 3 up to a number k , we get:
    3 + 6 + 9+ .... + n

Where n is the quotient of the division k/3 
This can be written as:
    3 + (3+3) + (3+3+3)+ ....
if we take 3 a common we get:
    3( 1 + (1+1) + (1+1+1) + ...
    3( 1 + 2 + 3 + ....
Which turns our problem into a simple multiplication with the sum of the series:
    1 + 2 + 3 + 4 + ... + n
The parties sum of this divergent series is:
    n(n+1)/2

The sum of multiples of a number m until a number k is then simply:
    m*(n*n+1)/2

we can now find the sum of the multiples of two numbers and add them toether. 
Using this method there will be duplicates at all points where both number have common multiples.
The sum of the common multiple can be subtracted by taking the LCM of the numbers and findings its sum upto 1000.
We now get correct answer.  
"""


no_3 =  999//3
no_5 =  999//5
no_15 = 999//15

def series_addition(multiplicant, n):
    partial_sum = (n*(n+1))/2
    sum = multiplicant*partial_sum
    return sum

sum_of_3 = series_addition(3,no_3)
sum_of_5 = series_addition(5,no_5)
duplicates = series_addition(15,no_15)

total = sum_of_3+sum_of_5-duplicates
print("The sum is : ",total)

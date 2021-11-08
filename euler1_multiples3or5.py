# Multiples of 3 or 5
# Submit

#  Show HTML problem content 
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


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

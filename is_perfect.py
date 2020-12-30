# To identify whether a number is a perfect number or not,
# we need to check whether the sum of the divisors of the number except itself is equal to number or not.
def is_perfect(number):
    sum_of_divisors = 0
    for i in range(1,number):
        if number%i == 0:
            sum_of_divisors += i
    if sum_of_divisors == number:
        return True
    else:
        return False

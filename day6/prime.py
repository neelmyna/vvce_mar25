import math

def check_is_prime(number):
    for i in range(2, math.ceil(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True
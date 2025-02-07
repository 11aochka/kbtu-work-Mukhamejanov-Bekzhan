import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 3, 5, 8, 13, 17, 20, 23]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers) 

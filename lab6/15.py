import math
import time

def multiply_list(numbers):
    return math.prod(numbers)

def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

def is_palindrome(s):
    return s == s[::-1]

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    return math.sqrt(number)

def all_true(t):
    return all(t)

nums = [2, 3, 4, 5]
result = multiply_list(nums)
print(result)
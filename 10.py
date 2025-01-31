def custom_sort(x):
    return abs(x - 30)

numbers = [10, 45, 60, 25, 5]
numbers.sort(key=custom_sort)
print(numbers)
#sort_list
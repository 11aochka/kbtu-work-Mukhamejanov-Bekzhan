def it_num(n):
    for i in range(0, n + 1, 12):
        yield i
        
n = int(input('Enter a number: '))

print(", ".join(map(str, it_num(n))))
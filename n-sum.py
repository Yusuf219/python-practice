def sum (n):
    if n == 0:
        return 0
    else:
        value = sum(n - 1)
        print(value)
        return n + value
result = sum(5)
print(result)
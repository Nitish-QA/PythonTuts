n = int(input("Enter a number n where,  (n > 0): "))
result = sum(i / (i + 1) for i in range(1, n + 1))
print(round(result, 2))
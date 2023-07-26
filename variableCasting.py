print('--------------1----------------')
# sometimes we need to convert the data type explicitly

x = int(4)
print(x)

y = str(5)
print(y)

# print(x + y) -- this will give type error
# so we need to convert it to same data type as below

y = int(y)
print(x + y)

x = int(1)   # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3
print(x, y, z)


x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2")  # w will be 4.2
print(x, y, z, w)


x = str("s1")  # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x, y, z)



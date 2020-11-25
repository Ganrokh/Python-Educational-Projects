x = [1, 2, 3, 4]
y = [7 , 6, 2, 1]
z = ['a', 'b', 'c', 'd']

# for a, b, c in zip(x, y, z):
#     print(a,b)

print(zip(x, y, z))

for i in zip(x, y, z):
    print(i)

print(list(zip(x, y)))

print(dict(zip(x, y)))

# Will not overwrite values
[print(a, b, c) for a, b, c in zip(x, y, z)]

# Will overwrite values
for x, y in zip(x, y):
    print(x, y)
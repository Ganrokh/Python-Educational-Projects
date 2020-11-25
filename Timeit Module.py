import timeit

# print(timeit.timeit('1+3', number=50000000))

# input_list = range(100)

# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False

# xyz = (i for i in input_list if div_by_five(i))

# Think of timeit as its own script separate from your script, like a VM in a computer.
# timeit must include ALL code that you wish to time. It won't pull any variables from outside of it.
# The number variable is how many times your code will be executed.

print(timeit.timeit('''input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i))''', number=5000))
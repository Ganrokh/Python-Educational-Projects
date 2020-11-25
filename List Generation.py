# # x = [i for i in range(5)] # Normal List
# # y = (i for i in range(5)) # List Generator

# # print(x)
# # print(y)

# # for i in y:
# #     print(i)

# input_list = [5,6,2,10,15,20,5,1,3]

# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False

# xyz = (i for i in input_list if div_by_five(i))
# # The line above is the same as below, but simplified
# # xyz = []
# # for i in input_list:
# #     if div_by_five(i):
# #         xyz.append(i)


# [print(i) for i in xyz]

# [[print(i,ii) for ii in range(5)] for i in range(5)]
# # The line above is the same as below, but simplified
# # for i in range(5):
# #     for ii in range(5):
# #         print(i, ii)

# zyx = (((i,ii) for ii in range(5)) for i in range(5))
# print(zyx) # This just prints the above generator, not iterating over it

# for i in zyx:
#     for ii in i:
#         print(ii)



# More on Generators!

# def simple_gen():
#     yield 'Oh'
#     yield 'hello'
#     yield 'there'

# for i in simple_gen():
#     print(i)


CORRECT_COMBO = (3, 6, 1)
# found_combo = False

# for c1 in range(10):
#     if found_combo:
#         break
#     for c2 in range(10):
#         if found_combo:
#             break
#         for c3 in range(10):
#             if (c1, c2, c3) == CORRECT_COMBO:
#                 print(f'Found the combo: ({c1}, {c2}, {c3})')
#                 found_combo = True
#                 break
#             print(c1, c2, c3)


def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == CORRECT_COMBO:
        print(f'Found the combo: ({c1}, {c2}, {c3})')
        break
    print(c1, c2, c3)
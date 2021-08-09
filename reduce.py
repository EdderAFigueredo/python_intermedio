#Uso con Reduce.

from functools import reduce

my_list = [2, 2, 2, 2, 2]

all_multipled = reduce(lambda a, b: a * b, my_list)

print(all_multipled)

# my_list = [2, 2, 2, 2, 2]

# all_multipled = 1

# for i in my_list:
#     all_multipled = all_multipled * i

# print(all_multipled)


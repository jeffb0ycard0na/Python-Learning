# list_1 = []
# list_2 = list()
#
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal")

# print(list("The lists are equal"))
#
# another_even = sorted(even, reverse=True)
#
# print(another_even is even)
#
# another_even.sort(reverse=True)
# print(even)
even = [2, 4, 6, 8]
odd = [1, 3, 7, 9]

numbers = [even, odd]

for numbers_set in numbers:
    print(numbers_set)

    for value in numbers_set:
        print(value)
